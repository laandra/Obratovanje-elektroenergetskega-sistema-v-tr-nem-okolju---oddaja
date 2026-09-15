"""One module every figure in this repo goes through: style, geometry, export.

A figure cell used to end in `plt.tight_layout(); plt.show()`, which drops the
`Figure` on the floor -- so nothing could ever be saved without rewriting the
cell. Here the terminator is `pf.show(fig, "name")` instead: it lays the figure
out, writes the article's PDF with its provenance, and displays it. One line
replaces two, and the body of the cell is untouched.

Three things are settings of this module rather than decisions taken per figure,
because they are properties of the *article*, not of any one chart:

  STYLE     one rcParams block for all eleven notebooks. The nine copy-pasted
            style cells this replaces had drifted -- 9 pt against 10 pt, three
            title sizes, two spellings of the same grey -- for no reason anyone
            recorded.
  PRESET    one standard figure width. A figure asked for at a different width
            is BOTH shown and saved at that width, so the inline preview is
            never a different picture from the one in the paper.
  LANG      labels are written in Slovenian; `LANG = "en"` translates them
            through GLOSSARY, again in both the preview and the PDF.

Two resolutions, because they are two different questions:

  DISPLAY_DPI   what the inline PNG in the .ipynb is rendered at. IPython passes
                `fig.dpi` to `print_figure`, so this is the knob for the picture
                you see in the notebook -- and for what a right-click "save
                image as" gives you. Raising it to 600 would multiply every
                stored output in these already 1-4 MB notebooks by ~30x.
  EXPORT_DPI    what `savefig` writes. This is the article's resolution, and it
                is independent of the inline preview.

Two formats:

  pdf   always written. Self-contained vector art with the fonts embedded as
        TrueType outlines (`pdf.fonttype: 42`, never Type 3, which IEEE rejects).
  png   opt-in (`png=True`). 600 dpi raster, for anywhere that cannot take
        vector art.

(A `.pgf` route -- LaTeX source whose text is typeset by the article itself --
was dropped from this pass. It buys automatic font matching at the cost of
needing a TeX install at save time, and the style is decided here anyway.)

Every export gets its own folder holding the image files plus the provenance
needed to find the code that drew it again: `source.json`, the producing
notebook cell as `cell.py`, and the git commit -- with the uncommitted diff
alongside it when the tree was dirty, because a commit id alone does not
reproduce a figure exported from a modified working tree.
"""
import json
import math
import os
import re
import subprocess
import sys
import textwrap
from datetime import date, datetime, timezone
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import warnings
from matplotlib import rc_context
from matplotlib.collections import Collection
from matplotlib.font_manager import FontProperties
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.text import Text
from matplotlib.ticker import FuncFormatter

EXPORT_DPI = 600          # raster resolution for the article
DISPLAY_DPI = 110         # inline preview in the notebook, unchanged

REPO_ROOT = Path(__file__).resolve().parent

# Where exports land. Kept beside the CSV results rather than in the notebook's
# working directory, so a re-run overwrites the article's figures in place.
FIGURE_DIR = REPO_ROOT / "Results" / "Figures"

# A dirty-tree diff is written into the figure folder so the exact source can be
# recovered later. Notebooks are excluded from it: an .ipynb diff is mostly
# base64 of the previous run's stored images, so a handful of them fills the cap
# below with noise and pushes the .py changes -- the ones that actually decide
# what the figure shows -- past the truncation point. The producing cell is
# captured exactly, as `cell.py`, which is the notebook half of the answer.
MAX_DIFF_BYTES = 1_000_000
DIFF_EXCLUDE = (":(exclude)*.ipynb",)

# --- IEEE conference geometry ---------------------------------------------
# IEEEtran, US Letter, two columns. A figure placed at \columnwidth must be
# BUILT at this width: scaling in \includegraphics rescales the text with the
# picture, so a figure is always exported at the width it will be placed at.
IEEE_COLUMN_W = 3.5       # inches, \columnwidth
IEEE_PAGE_W = 7.16        # inches, \textwidth -- figure* spanning both columns
IEEE_FONT_PT = 8

RCPARAMS = {
    "savefig.dpi": EXPORT_DPI,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.02,
    "figure.dpi": DISPLAY_DPI,
    # Type 42 embeds TrueType outlines instead of Type 3 bitmapped glyphs, so the
    # text in the PDF stays selectable, searchable and non-fuzzy. IEEE rejects
    # Type 3 outright.
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",
    "figure.constrained_layout.use": False,
}

# Same settings with the off-white studio ground replaced by white. The notebook
# palette sits on SURFACE = #fcfcfb, which prints as a faint grey rectangle on a
# white page; apply this variant when the figure goes into the article.
RCPARAMS_PAPER = dict(RCPARAMS, **{
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
})

# IEEEtran sets the body in Times at 10 pt; figure text is conventionally 8 pt.
# `serif` selects a real Times for the pdf so the figure text and the body text
# are the same typeface.
RCPARAMS_IEEE = dict(RCPARAMS, **{
    "font.family": "serif",
    "font.serif": ["Times New Roman", "STIX Two Text", "Nimbus Roman",
                   "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "font.size": IEEE_FONT_PT,
    "axes.titlesize": IEEE_FONT_PT,
    "axes.labelsize": IEEE_FONT_PT,
    "xtick.labelsize": IEEE_FONT_PT - 1,
    "ytick.labelsize": IEEE_FONT_PT - 1,
    "legend.fontsize": IEEE_FONT_PT - 1,
    "axes.linewidth": 0.6,
    "lines.linewidth": 1.2,
    "grid.linewidth": 0.5,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
})

# --- the one style ---------------------------------------------------------
# Nine notebooks carried a copy of this block. Where they disagreed the
# differences were drift rather than intent, so they are resolved here once:
# font.size 10 (was 9 in three notebooks), axes.titlesize 12 (was 11 and 10.5),
# titleweight semibold (was bold), and one grey for MUTED -- #8b8a84 against
# #898781 is a colour difference no reader can see, in a token that plays the
# identical role in both.
INK, INK_2, MUTED, SURFACE = "#0b0b0b", "#52514e", "#8b8a84", "#fcfcfb"
GRID, BASELINE = "#e6e5e1", "#c3c2b7"

# Four categorical slots, validated against each other for hue separation.
# The notebooks bind these to their own domains (TARIFF_COLOR, CONTRACT_COLOR,
# ...) -- that binding is the study's semantics and stays in the notebook.
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]

STYLE = {
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE,
    "axes.edgecolor": MUTED, "axes.labelcolor": INK_2,
    "axes.titlecolor": INK, "axes.titlesize": 12, "axes.titleweight": "semibold",
    "axes.titlelocation": "left", "axes.titlepad": 12,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "axes.axisbelow": True, "axes.spines.top": False, "axes.spines.right": False,
    "xtick.color": INK_2, "ytick.color": INK_2, "font.size": 10,
    "text.color": INK, "legend.frameon": False, "figure.dpi": DISPLAY_DPI,
}

# --- geometry --------------------------------------------------------------
# One width for every figure, so a page of them is a set rather than a pile.
# A figure asked for at another preset is shown AND saved at it -- `show()`
# resizes before it displays, so the preview is the picture that gets placed.
PRESETS = {
    "screen": IEEE_PAGE_W,   # the default: \textwidth, comfortable to read inline
    "page":   IEEE_PAGE_W,   # \textwidth + IEEE text, i.e. a figure*
    "column": IEEE_COLUMN_W,  # \columnwidth + IEEE text
}
IEEE_PRESETS = ("column", "page")
STANDARD_RATIO = 0.615       # 7.16 x 4.40 in

# --- module state ----------------------------------------------------------
# The knobs a notebook sets once, at the top, instead of per figure.
SAVE_PDF = True       # master switch: False while iterating, no other edits
PAPER_GROUND = True   # the SAVED copy gets a white ground; preview keeps SURFACE
PRESET = "screen"
LANG = "sl"
TITLES = True         # draw `finish`/`chart_frame` titles into the figure
SUBDIR = None         # per-notebook folder under Results/Figures

# Strings `translate_figure` had no glossary entry for, in first-seen order.
MISSING_TRANSLATIONS = {}


def use(*, paper=False, ieee=False, subdir=None, lang=None, preset=None,
        grid=True, titles=None):
    """Install the shared style. One line at the top of a notebook.

        import Plotting_Functions as pf
        pf.use(subdir="battery_sizing")
        from Plotting_Functions import INK, INK_2, MUTED, SURFACE, SERIES, EUR, finish

    The export keys are applied last, so they win over the style -- the order
    the notebook style cells this replaces already used.

    `grid=False` is for a notebook whose own helpers turn gridlines on per axis
    (`ax.grid(axis="y")`) and would otherwise get x gridlines it never had.

    `titles=False` drops the title out of every figure in the notebook. An IEEE
    figure carries no title of its own -- the caption below it, set in the
    article, is the title -- so a title baked into the image is a duplicate of
    the caption in a different typeface. The text is not lost: `finish` still
    records it, and it is written into the export's `source.json` and
    `SOURCE.md` as the caption to use.
    """
    global SUBDIR, LANG, PRESET, TITLES

    plt.rcParams.update(STYLE)
    if not grid:
        plt.rcParams["axes.grid"] = False
    apply(paper=paper, ieee=ieee)

    if preset is not None:
        PRESET = preset
    if subdir is not None:
        SUBDIR = subdir
    if lang is not None:
        LANG = lang
    if titles is not None:
        TITLES = titles
    # Any plt.subplots() without an explicit figsize is now already the right
    # size, so a migrated cell can simply drop its figsize literal.
    plt.rcParams["figure.figsize"] = figsize()
    return plt.rcParams


def apply(paper=False, ieee=False):
    """Push the export settings onto the live rcParams.

    `ieee=True` additionally switches the text to Times at IEEE_FONT_PT on a
    white ground. It changes the inline previews too, which is intended: the
    preview should then look like what the article will print.
    """
    plt.rcParams.update(RCPARAMS_IEEE if ieee else
                        RCPARAMS_PAPER if paper else RCPARAMS)
    return plt.rcParams


def ieee_style():
    """Context manager: build one figure IEEE-styled, leaving the notebook alone.

        with pf.ieee_style():
            fig, ax = plt.subplots(figsize=pf.ieee_figsize())
            ...
        pf.show(fig, "name", preset="column")

    Building inside this is exact; `preset="column"` on an already-drawn figure
    restyles it after the fact, which is close but not identical -- see
    `_ieee_restyle`.
    """
    return rc_context(RCPARAMS_IEEE)


def ieee_figsize(width="column", ratio=0.62):
    """Figure size in inches for an IEEE conference figure.

    `width`: "column" for a single column (\\columnwidth), "page" for a figure*
    spanning both (\\textwidth), or a number of inches.
    """
    if width == "column":
        w = IEEE_COLUMN_W
    elif width == "page":
        w = IEEE_PAGE_W
    else:
        w = float(width)
    return (w, w * ratio)


def figsize(ratio=STANDARD_RATIO, preset=None):
    """The standard figure size, or a taller/shorter one at the same width.

    `ratio` is height/width: pass a smaller number for a wide strip of panels,
    a larger one for a stack of rows.
    """
    return (PRESETS[preset or PRESET], PRESETS[preset or PRESET] * ratio)


# --- formatters ------------------------------------------------------------
# TICK LABELS CARRY NO UNIT. The unit belongs to the axis label, once, where a
# reader looks for it; repeating it on every tick prints it eight times and, on
# an axis already labelled "... [%]", says percent twice. So PCT no longer draws
# a "%" and PCT_SIGNED no longer draws a " %" -- the axis label does that, and
# every axis these two are used on carries [%] in its label.
#
# That leaves PCT rendering exactly like PLAIN, and it still keeps its own name:
# the name is what a cell says about its axis, and a percentage axis that stops
# being marked as one is how the unit goes missing again the next time somebody
# changes a formatter. PCT_SIGNED remains genuinely different -- it forces the
# sign, which is what a "change against the baseline" axis needs.
EUR = FuncFormatter(lambda v, _: f"{v:,.0f}")
PLAIN = FuncFormatter(lambda v, _: f"{v:,.0f}")
KW = FuncFormatter(lambda v, _: f"{v:,.1f}")
PCT = FuncFormatter(lambda v, _: f"{v:,.0f}")
PCT_SIGNED = FuncFormatter(lambda v, _: f"{v:+,.0f}")
YEARS = FuncFormatter(lambda v, _: f"{v:.0f}")


# --- colour ----------------------------------------------------------------

def mix(hex_a, hex_b, t):
    """Blend two hex colours, `t` of the way from a to b."""
    a = [int(hex_a[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(hex_b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#%02x%02x%02x" % tuple(round(x + (y - x) * t) for x, y in zip(a, b))


def ramp(hue, name="ramp", light=SURFACE):
    """A light-to-`hue` colormap for heatmaps, grounded on the studio surface."""
    from matplotlib.colors import LinearSegmentedColormap

    return LinearSegmentedColormap.from_list(
        name, [light, mix(light, hue, 0.45), hue])


# --- axes ------------------------------------------------------------------

def _axes_width_in(ax, fig_width_in=None):
    """How wide this axes is, in inches -- the room a left-aligned title has.

    A title at `axes.titlelocation: left` starts at the axes' left edge, not the
    figure's, so the y label and tick labels are NOT room it can use.

    After a layout pass the axes position is exact and is used. Before one --
    `finish` runs long before `show` lays the figure out -- the position is
    still the pre-layout default, so the share of the figure is taken from the
    subplot grid instead and trimmed for the axis furniture. That guess only has
    to be close: `show` re-wraps from the real geometry once the layout is done.
    """
    fig_width_in = fig_width_in or ax.figure.get_figwidth()
    if getattr(ax, "_pf_laid_out", False):
        return ax.get_position().width * fig_width_in
    try:
        ncols = ax.get_subplotspec().get_gridspec().ncols
    except AttributeError:
        ncols = 1
    return fig_width_in * 0.78 / max(1, ncols)


def _measure(artist, renderer, text):
    """Width of `text` in inches, as `artist` would actually draw it."""
    keep = artist.get_text()
    artist.set_text(text)
    try:
        return artist.get_window_extent(renderer).width / artist.figure.dpi
    finally:
        artist.set_text(keep)


def _wrap(artist, text, width_in):
    """Wrap one line of text to `width_in`, measuring rather than estimating.

    Left-aligned titles overflow to the RIGHT of the axes. Exported with
    `bbox_inches="tight"` that overflow is not clipped -- it silently widens the
    saved figure -- and exported at an exact IEEE width it is cut off mid-word.
    Either way the figure is wrong, so the wrap has to be right, and a character
    count is not: the same string is a third wider in bold Times at 9.6 pt than
    in the regular sans the estimate was calibrated on. The renderer knows, so
    it is asked; the estimate stays as the fallback for a canvas that cannot
    produce one.
    """
    try:
        renderer = artist.figure.canvas.get_renderer()
    except AttributeError:
        chars = max(24, int(width_in / (CHAR_IN * artist.get_fontsize() / FRAME_SUB_PT)))
        return "\n".join(textwrap.wrap(text, chars)) or text

    lines, line = [], ""
    for word in text.split():
        trial = f"{line} {word}".strip()
        if line and _measure(artist, renderer, trial) > width_in:
            lines.append(line)
            line = word
        else:
            line = trial
    if line:
        lines.append(line)
    return "\n".join(lines) or text


def _title_artist(ax):
    """The Text that `ax.set_title` will actually write to.

    It is only `ax.title` when the title is centred. This style sets
    `axes.titlelocation: left`, which routes set_title to a different artist --
    so measuring a wrap against `ax.title`, or restoring a font size onto it,
    quietly operates on an empty one while the visible title goes untouched.
    """
    loc = plt.rcParams["axes.titlelocation"].lower()
    return {"left": getattr(ax, "_left_title", ax.title),
            "right": getattr(ax, "_right_title", ax.title)}.get(loc, ax.title)


def _set_head(ax, title, subtitle, wrap, fig_width_in):
    """Draw an axes title (+ subtitle line), wrapped to the axes width.

    The size and family are passed back in because `ax.set_title` resets both
    from rcParams on every call -- and `show` calls this a second time, after
    the text has been scaled, to re-wrap against the laid-out axes. Without
    them that re-wrap silently undoes `_ieee_restyle` and `_scale_panel_text`
    for every title.
    """
    width_in = _axes_width_in(ax, fig_width_in)
    art = _title_artist(ax)
    head = _wrap(art, title, width_in) if wrap else title
    if subtitle is not None:
        head += "\n" + (_wrap(art, subtitle, width_in) if wrap else subtitle)
    ax.set_title(head, fontsize=art.get_fontsize(),
                 fontfamily=art.get_fontfamily())


def heads(fig):
    """The title, and subtitle, `finish` was given for each axes of a figure.

    Returned whether or not the titles are drawn, because when they are NOT
    this is where the caption text has gone -- `show` writes it into the
    export's provenance so the article has it to hand.
    """
    out = []
    for ax in fig.axes:
        head = getattr(ax, "_pf_head", None)
        if head is not None:
            out.append(" — ".join(p for p in head[:2] if p))
    return out


def _rewrap_heads(fig, titles=True):
    """Re-wrap every `finish`-set title from the laid-out geometry.

    `finish` wraps against a guess: it runs before `show` resizes the figure and
    before anything has laid the axes out. Here both are known -- so a title
    that was wrapped for a full-width figure gets re-wrapped for the
    \\columnwidth version of it, against the axes box it will really occupy.

    Returns whether any title changed, which is the caller's signal that the
    layout has to run once more: a title that gained a line needs the room.
    """
    width_in = fig.get_figwidth()
    changed = False
    for ax in fig.axes:
        head = getattr(ax, "_pf_head", None)
        if head is None:
            continue
        ax._pf_laid_out = True
        loc = plt.rcParams["axes.titlelocation"]
        before = ax.get_title(loc=loc)
        if titles:
            _set_head(ax, *head, width_in)
        else:
            art = _title_artist(ax)
            # Same reason as in `_set_head`: set_title re-reads rcParams, so the
            # scaled size has to be handed back even when the text is emptied.
            ax.set_title("", fontsize=art.get_fontsize(),
                         fontfamily=art.get_fontfamily())
        changed |= ax.get_title(loc=loc) != before
    return changed


def finish(ax, *, title=None, xlabel=None, ylabel=None, subtitle=None,
           yfmt=None, xfmt=None, wrap=True):
    """Title, labels and tick formats on one axes.

    Replaces five near-identical notebook helpers (`finish` in three notebooks
    with three different positional orders, `tidy`, `style_axes`). Everything
    after `ax` is keyword-only, so all three orders migrate by naming the
    arguments rather than by getting them in the right sequence.

    `subtitle` goes on a second title line, in the axes title pad. Both lines
    are wrapped to the axes width -- pass `wrap=False` for a figure that is
    exported `preset="as_built"`, where the final width is not the preset's.
    """
    if title is not None:
        ax._pf_head = (title, subtitle, wrap)     # re-wrapped by `show`
        _set_head(ax, title, subtitle, wrap,
                  PRESETS.get(PRESET, IEEE_PAGE_W))
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    if yfmt is not None:
        ax.yaxis.set_major_formatter(yfmt)
    if xfmt is not None:
        ax.xaxis.set_major_formatter(xfmt)
    return ax


def key_legend(ax, handles, where="below", ncol=4, **kw):
    """Place a legend built from explicit handles.

    The handles themselves stay in the notebook -- what a colour means is the
    study's semantics. This only decides where the keys go, which is the part
    that was written five times (`below_legend`, `tariff_legend`,
    `soc_mode_legend`, `family_legend`).

    `where="below"` puts the keys a fixed distance in INCHES under the axes,
    which is not what the anchor below says: -0.16 is an AXES fraction, so the
    gap it produces grows with the axes -- 0.56 in under a full-height chart and
    0.24 in under a short one. It is kept as the starting position, because the
    axes box is not laid out yet; `show` measures and corrects it.

    A caller that passes its own `bbox_to_anchor` has chosen the gap itself and
    is left alone.
    """
    managed = where == "below" and "bbox_to_anchor" not in kw
    if where == "below":
        kw.setdefault("bbox_to_anchor", (0.5, -0.16))
        kw.setdefault("loc", "upper center")
    else:
        kw.setdefault("loc", where if where != "inside" else "best")
    leg = ax.legend(handles=handles, ncol=ncol, **kw)
    if managed:
        leg._pf_key_gap = LEGEND_PAD_IN
    return leg


# --- figure-level frame ----------------------------------------------------
# Header and footer geometry in inches, not figure fractions, so one set of
# numbers works on a 3.4 in row and a 10 in grid alike.
PAD_TOP_IN, TITLE_IN, HEAD_GAP_IN = 0.10, 0.26, 0.08
SUB_LINE_IN, BODY_GAP_IN, LEFT_IN = 0.20, 0.26, 0.16
LEGEND_ROW_IN = 0.26          # one row of keys -- the FALLBACK, for when nothing
                              # can measure. A real 9.5 pt row is 0.19-0.25 in,
                              # and the surplus landed in the gap above it.
LEGEND_PAD_IN = 0.18          # gap between the axes and the first legend row
LEGEND_EDGE_IN = 0.06         # margin under the last row, to the canvas edge
LEGEND_KEY_EM = 4.8           # handle + text pad + column gap, in font-size units
LEGEND_MAX_COLS = 5           # past this the keys are narrower than their labels
CHAR_IN = 0.062               # mean glyph advance of DejaVu Sans at 9.5 pt
FRAME_TITLE_PT, FRAME_SUB_PT = 13, 9.5


def chart_frame(fig, title, subtitle="", handles=None, ncol=None):
    """Record the header and legend this figure wants. `show` lays them out.

    Call once, last, in place of suptitle + legend + tight_layout:

        pf.chart_frame(fig, "Title", "Subtitle", handles=keys)
        pf.show(fig, "name", layout="frame")

    NOTHING IS DRAWN HERE. The bands have to be measured at the width and the
    text size the figure is EXPORTED at, and when this is called neither is
    known: `show` resizes to the preset and restyles the text afterwards.
    Measuring here is what made `preset="column"` need a hand-tuned `ncol=` and
    a matching `figsize` to go with it -- three places to keep in step, every
    one of them compensating for a layout computed against the wrong canvas.

    `handles=None` draws no legend; pass a list of handles to get one. `ncol` is
    a MAXIMUM rather than an instruction -- see `_legend_shape`.
    """
    fig._pf_frame = {"title": title, "subtitle": subtitle,
                     "handles": handles, "ncol": ncol}
    fig._pf_frame_bands = None
    fig._pf_frame_head = " — ".join(p for p in (title, subtitle) if p)
    return fig


def _renderer(fig):
    """Something to measure with, or None on a canvas that cannot make one.

    Every measurement in this module is optional by construction: a headless or
    exotic backend falls back to an estimate rather than failing an export.
    """
    try:
        return fig.canvas.get_renderer()
    except AttributeError:
        return None


def _frame_pt(fig):
    """The frame's title and subtitle sizes, and the family, as it will be drawn.

    FRAME_TITLE_PT and FRAME_SUB_PT are quoted against STYLE's 10 pt body. When
    the body has moved -- an IEEE preset scales it to 8 pt in Times -- the frame
    has to move with it. It is drawn AFTER `_ieee_restyle`, which walks the text
    artists that exist at the time, so the frame is not among them and has to
    carry the typeface itself. Getting this wrong is not subtle: it sets the
    legend in the notebook's sans while the axis labels are in Times, at a size
    chosen for Times, so the keys come out looking a point or two too big.
    """
    scale = getattr(fig, "_pf_text_scale", None)
    if scale is None:
        scale = plt.rcParams["font.size"] / STYLE["font.size"]
    family = getattr(fig, "_pf_text_family", None) or plt.rcParams["font.family"]
    return FRAME_TITLE_PT * scale, FRAME_SUB_PT * scale, family


def _tight_pad_in():
    """The margin `tight_layout` keeps INSIDE whatever rect it is handed.

    It is not optional and it is not small -- 1.08 font-size units, 0.15 in at a
    10 pt body -- so a footer band that ignores it sits that much further from
    the axes than it asked to.
    """
    return 1.08 * plt.rcParams["font.size"] / 72.0


def _frame_sub_lines(fig, subtitle, width_in):
    """The subtitle, wrapped at the size it will actually be drawn."""
    _, sub_pt, family = _frame_pt(fig)
    probe = fig.text(0, 0, "", fontsize=sub_pt, color=INK_2, fontfamily=family)
    try:
        return _wrap(probe, subtitle, width_in).split("\n")
    finally:
        probe.remove()


def _widest_label_in(fig, handles, sub_pt, family, renderer):
    """Width of the longest legend label, in inches. The estimate, not the truth.

    Only used when there is no renderer; `_legend_shape` measures the assembled
    legend when there is one.
    """
    labels = [h.get_label() or "" for h in handles]
    if renderer is None:
        return max((len(s) for s in labels), default=0) * CHAR_IN
    probe = fig.text(0, 0, "", fontsize=sub_pt, fontfamily=family)
    try:
        return max((_measure(probe, renderer, s) for s in labels), default=0.0)
    finally:
        probe.remove()


def _legend_probe(fig, handles, ncol, sub_pt, family, renderer):
    """Build the legend at `ncol`, measure it in inches, take it away again.

    Returns (width, height), or None when it cannot be measured.
    """
    leg = fig.legend(handles=handles, loc="lower center", ncol=ncol,
                     prop=FontProperties(family=family, size=sub_pt))
    try:
        box = leg.get_window_extent(renderer)
        return box.width / fig.dpi, box.height / fig.dpi
    except Exception:
        return None
    finally:
        leg.remove()


def _legend_shape(fig, handles, requested=None):
    """How many columns the keys fit in at this width, and how tall that is.

    `requested` is a MAXIMUM, not an instruction. An `ncol=3` written for
    \textwidth stays 3 there and drops to whatever fits at \columnwidth, which
    is what lets one `preset=` retarget a figure with no other edit -- and is
    the difference between a legend that reads and the block that ate a third of
    the canvas when that same 3 was forced onto a 3.5 in figure.

    The widest arrangement that fits wins, found by building the legend and
    measuring it rather than by estimating a per-key allowance: an allowance has
    to guess the handle, the text pad and the column gap, and being one column
    gap out costs a whole extra ROW of height at \columnwidth.

    Both returns are measured: the height is what the keys really occupy, which
    the assumed 0.26 in a row over-stated by a third. The legend is anchored to
    the BOTTOM of the band it is given, so every inch reserved beyond what it
    occupies opened up as gap between the chart and its keys.
    """
    n = 0 if not handles else len(handles)
    if not n:
        return 1, 0.0
    renderer = _renderer(fig)
    _, sub_pt, family = _frame_pt(fig)
    avail = fig.get_figwidth() - 2 * LEFT_IN
    top = max(1, min(requested or LEGEND_MAX_COLS, LEGEND_MAX_COLS, n))

    if renderer is None:
        per_key = (_widest_label_in(fig, handles, sub_pt, family, None)
                   + LEGEND_KEY_EM * sub_pt / 72.0)
        fits = max(1, int(avail // per_key)) if per_key > 0 else n
        ncol = max(1, min(top, fits))
        return ncol, LEGEND_ROW_IN * math.ceil(n / ncol) * (sub_pt / FRAME_SUB_PT)

    last = None
    for ncol in range(top, 0, -1):
        size = _legend_probe(fig, handles, ncol, sub_pt, family, renderer)
        if size is None:
            break
        last = (ncol, size[1])
        if size[0] <= avail:
            return ncol, size[1]
    if last is not None:
        return last          # nothing fit, so `last` is the single-column result
    return 1, LEGEND_ROW_IN * n * (sub_pt / FRAME_SUB_PT)


def _frame_bands(fig):
    """Measure the header and legend bands, in inches. Returns (head, foot).

    Runs BEFORE the final resize, because the height depends on the bands and
    not the other way round: every term here comes from the figure's WIDTH and
    its font sizes, and none from its height. The result is cached on the figure
    so `_apply_frame` lays out against the same numbers the height was computed
    from -- re-measuring there would let the two drift by a rounding.
    """
    spec = getattr(fig, "_pf_frame", None)
    if not spec:
        return 0.0, 0.0
    w = fig.get_figwidth()
    title_pt, _, _ = _frame_pt(fig)
    show_titles = getattr(fig, "_pf_titles", TITLES)
    title = spec["title"] if show_titles else ""
    subtitle = spec["subtitle"] if show_titles else ""
    lines = (_frame_sub_lines(fig, subtitle, w - 2 * LEFT_IN)
             if subtitle else [""])
    head_scale = title_pt / FRAME_TITLE_PT
    head_in = (BODY_GAP_IN if not title else
               PAD_TOP_IN + TITLE_IN * head_scale + HEAD_GAP_IN
               + SUB_LINE_IN * head_scale * len(lines) + BODY_GAP_IN)

    ncol, legend_in = _legend_shape(fig, spec["handles"], spec["ncol"])
    # tight_layout adds its own pad inside the rect, so only the remainder has to
    # be reserved here; reserving the whole gap on top of it is how the space
    # under the axes grew to roughly twice what it was set to.
    gap_in = max(0.04, LEGEND_PAD_IN - _tight_pad_in())
    foot_in = 0.0 if not legend_in else LEGEND_EDGE_IN + legend_in + gap_in
    fig._pf_frame_bands = (head_in, foot_in, ncol, lines)
    return head_in, foot_in


def _apply_frame(fig):
    """Lay the axes out in what is left of the canvas, then fill the bands."""
    spec = getattr(fig, "_pf_frame", None)
    if not spec:
        return False
    if getattr(fig, "_pf_frame_bands", None) is None:
        _frame_bands(fig)
    head_in, foot_in, ncol, lines = fig._pf_frame_bands
    fig._pf_frame = fig._pf_frame_bands = None       # laid out once

    w, h = fig.get_figwidth(), fig.get_figheight()
    title_pt, sub_pt, family = _frame_pt(fig)
    show_titles = getattr(fig, "_pf_titles", TITLES)
    title = spec["title"] if show_titles else ""
    subtitle = spec["subtitle"] if show_titles else ""

    # Clamped for `as_built`, where the canvas was not grown to fit the bands and
    # a tall header could otherwise invert the rect.
    rect = (0.0, min(foot_in / h, 0.45), 1.0, 1.0 - min(head_in / h, 0.45))
    fig._pf_frame_rect = rect
    fig.tight_layout(rect=rect)
    if title:
        fig.text(LEFT_IN / w, 1.0 - PAD_TOP_IN / h, title,
                 ha="left", va="top", fontsize=title_pt, fontweight="bold",
                 color=INK, fontfamily=family)
    if subtitle:
        fig.text(LEFT_IN / w,
                 1.0 - (PAD_TOP_IN + TITLE_IN * (title_pt / FRAME_TITLE_PT)
                        + HEAD_GAP_IN) / h,
                 "\n".join(lines), ha="left", va="top", fontsize=sub_pt,
                 color=INK_2, linespacing=1.4, fontfamily=family)
    if foot_in > 0 and spec["handles"]:
        fig.legend(handles=spec["handles"], loc="lower center",
                   bbox_to_anchor=(0.5, LEGEND_EDGE_IN / h), ncol=ncol,
                   prop=FontProperties(family=family, size=sub_pt))
    return True


def _reanchor_key_legends(fig):
    """Put every `key_legend` a fixed number of INCHES below its axes.

    Returns whether anything moved, which is the caller's signal to lay out
    again: `tight_layout` sizes the axes around the legend, so a legend that
    moves changes the very box it was measured against. Two passes settle it.
    """
    renderer = _renderer(fig)
    if renderer is None:
        return False
    fig_h = fig.get_figheight()
    moved = False
    for ax in fig.axes:
        leg = ax.get_legend()
        gap = getattr(leg, "_pf_key_gap", None)
        if gap is None:
            continue
        box = ax.get_position()
        ax_h_in = box.height * fig_h
        if ax_h_in <= 0:
            continue
        try:
            xb = ax.xaxis.get_tightbbox(renderer)
        except Exception:
            xb = None
        # The tick labels and the x label hang below the axes box; the gap is
        # measured from the bottom of those, not from the box.
        drop_in = (0.0 if xb is None
                   else max(0.0, box.y0 * fig_h - xb.y0 / fig.dpi))
        y = -(drop_in + gap) / ax_h_in
        prev = getattr(leg, "_pf_key_y", None)
        leg._pf_key_y = y
        leg.set_bbox_to_anchor((0.5, y), transform=ax.transAxes)
        if prev is None or abs(prev - y) > 0.002:
            moved = True
    return moved



def edge_label(ax, y, text, side="right"):
    """One-line annotation pinned to an edge of the axes in AXES coordinates,
    on a surface-coloured pad so it never sits on a curve. Data coordinates are
    the wrong frame for these: the reference lines span the whole axis, and an
    x taken from the data can fall outside the view and be clipped away."""
    x, ha = (0.995, "right") if side == "right" else (0.005, "left")
    return ax.annotate(text, xy=(x, y), xycoords=("axes fraction", "data"),
                       xytext=(0, 4), textcoords="offset points", ha=ha,
                       va="bottom", color=INK_2, fontsize=8.5, zorder=5,
                       bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1.6))


PANEL_COLS = 4                # households per row; 16 households -> a 4 x 4 grid
PANEL_IN = (3.05, 2.5)        # one panel, at which the shared style is legible
PANEL_REF_IN = IEEE_PAGE_W / 2   # the widest a panel gets before it stops being
                                 # a small multiple; the text scales against it


def panel_grid(n, ncols=PANEL_COLS, panel=PANEL_IN, sharex=True, sharey=False,
               **kw):
    """A wrapped grid of `n` small panels, with the text scaled to the panel.

    Returns `(fig, axes)` with `axes` flat and the unused trailing slots already
    hidden -- `axes[:n]` are the live ones.

    The font scaling is why this exists rather than a second style preset. The
    shared style is set for a full-width chart; a 3 in panel in a 4 x 4 grid
    needs smaller text, and that is a property of drawing sixteen small panels,
    not of the notebook that happens to draw them. The scale is recorded on the
    figure and applied by `show()` as a single pass over the finished text, so
    it catches the titles and labels the caller adds after this returns -- an
    rc_context here would only have caught what was created inside it.
    """
    ncols = max(1, min(int(ncols), max(1, n)))
    nrows = math.ceil(n / ncols)
    fig, axes = plt.subplots(nrows, ncols, sharex=sharex, sharey=sharey,
                             figsize=(panel[0] * ncols, panel[1] * nrows),
                             squeeze=False, **kw)
    axes = axes.ravel()
    for ax in axes[n:]:
        ax.set_visible(False)     # empty slots when n is not a multiple of ncols
    fig._pf_panel_cols = ncols
    return fig, axes


def _scale_panel_text(fig):
    """Shrink the text of a `panel_grid` figure to suit one panel.

    Run after the figure has been resized to its preset, because that is what
    decides how wide a panel actually ends up: the same 4 x 4 grid is a 3 in
    panel at `as_built` and a 1.8 in panel at \textwidth, and the text that
    fits differs accordingly. Scaled against half the standard width, which is
    the widest a panel gets before it stops being a small multiple.

    The reference is a fixed physical width -- half of \\textwidth, 3.58 in --
    and not half of whatever preset is being exported to. Taking it from the
    target width cancels out (a panel is target/ncols wide, so the ratio is just
    2/ncols) and every preset would get identical text, which is the opposite of
    the point. Reading it from the module `PRESET` has the same flaw whenever a
    notebook sets that to "column".
    """
    ncols = getattr(fig, "_pf_panel_cols", None)
    if not ncols:
        return
    fig._pf_panel_cols = None                  # applied once, not once per call
    scale = min(1.0, (fig.get_figwidth() / ncols) / PANEL_REF_IN)
    if abs(scale - 1.0) < 1e-9:
        return
    for artist in fig.findobj(Text):
        artist.set_fontsize(artist.get_fontsize() * scale)



# --- language --------------------------------------------------------------
# The notebooks are written in Slovenian and the article is in English. Rather
# than rewrite every label at its call site, the finished figure is translated
# on the way out: `show()` walks the text artists and substitutes. It runs
# before the figure is displayed as well as before it is saved, so the preview
# and the PDF always say the same thing.
#
# Entries are exact label strings. Anything not covered falls through unchanged
# and is recorded in MISSING_TRANSLATIONS, so a gap is visible rather than a
# silently half-translated figure. Grow it per notebook as they migrate.
GLOSSARY = {
    # axes
    "Kapaciteta baterije [kWh]": "Battery capacity [kWh]",
    "Kapaciteta na gospodinjstvo [kWh]": "Capacity per household [kWh]",
    "Letni strošek [EUR/a]": "Annual cost [EUR/a]",
    "Mejna vrednost kapacitete [EUR/kWh/a]": "Marginal value of capacity [EUR/kWh/a]",
    "Neto korist [EUR/a]": "Net benefit [EUR/a]",
    "Energija [kWh/a]": "Energy [kWh/a]",
    "Konica odjema [kW]": "Peak import [kW]",
    "Sprememba konice odjema [%]": "Change in peak import [%]",
    "Ekvivalentni polni cikli [1/a]": "Equivalent full cycles [1/a]",
    "Življenjska doba [let]": "Service life [years]",
    # axes -- the bill
    "Letni račun [EUR/a]": "Annual bill [EUR/a]",
    "Povprečni letni račun [EUR/a]": "Mean annual bill [EUR/a]",
    "Letni račun skupnosti [EUR/a]": "Community annual bill [EUR/a]",
    "Letni račun gospodinjstva [EUR/a]": "Household annual bill [EUR/a]",
    "Neto letna korist skupnosti [EUR/a]": "Community net annual benefit [EUR/a]",
    "Sprememba letnega računa [EUR/a]": "Change in the annual bill [EUR/a]",
    "Učinek na letni račun [EUR/a]": "Effect on the annual bill [EUR/a]",
    "Energijski del letnega računa [EUR/a]": "Energy part of the annual bill [EUR/a]",
    "Prihranek [EUR/a]": "Saving [EUR/a]",
    "Dosegljivi prihranek [EUR/a]": "Achievable saving [EUR/a]",
    "Prihranek proti stanju brez delitve [EUR/a]": "Saving against no sharing [EUR/a]",
    "Delež bruto računa [%]": "Share of the gross bill [%]",
    "Razlika [EUR/a]": "Difference [EUR/a]",
    "Preplačilo [%]": "Overpayment [%]",
    "Diskontirani ROI [%]": "Discounted ROI [%]",
    # axes -- the horizon study
    "Vrzel [%]": "Gap [%]",
    "Povprečna vrzel [%]": "Mean gap [%]",
    "Vrzel skupine / povprečje algoritma [–]": "Group gap / algorithm mean [-]",
    "Čas reševalnika [s/(gospodinjstvo·leto)]": "Solver time [s/(household*year)]",
    # axes -- the community study
    "Trajanje [h/a]": "Duration [h/a]",
    "Odjem skupnosti [kW]": "Community import [kW]",
    "Neto moč skupnosti [kW]": "Community net power [kW]",
    "Cena SMP [EUR/MWh]": "Day-ahead price [EUR/MWh]",
    "Deljena energija [kWh]": "Shared energy [kWh]",
    "Pogodbeni delež deljene energije [%]": "Contracted share of shared energy [%]",
    "Značilni primer priključitve": "Connection case",
    "Ura dneva [h]": "Hour of the day [h]",
    "Mesec": "Month",
    "Cenik": "Price list",
    "Tip gospodinjstva": "Household type",
    "Število gospodinjstev": "Number of households",
    # axes -- the inverter sweep
    "Enkratni strošek razsmernika in montaže [EUR]":
        "One-off inverter and installation cost [EUR]",
    "Cena razsmernika [EUR/kW]": "Inverter price [EUR/kW]",
    "Mediana optimalne kapacitete [kWh]": "Median optimal capacity [kWh]",
    # titles
    "Letni strošek elektrike ob popolnem predvidevanju pada z velikostjo baterije":
        "Annual electricity cost under perfect foresight falls with battery size",
    "Kje se naslednja kWh hrambe ne izplača več":
        "Where the next kWh of storage stops paying for itself",
    "Neto letna korist = prihranek MILP − letni strošek baterije":
        "Net annual benefit = MILP saving − annualised battery cost",
    "Pretok energije skozi baterijo": "Energy through the battery",
    "Konica odjema iz omrežja": "Peak grid import",
    "Ekvivalentni polni cikli na leto": "Equivalent full cycles per year",
    "Kako velikost baterije premakne konec življenjske dobe":
        "How battery size moves the end of service life",
    # legend keys and annotations
    "Izpraznjeno iz baterije": "Discharged from battery",
    "Napolnjeno iz omrežja": "Charged from grid",
    "samo cikli (EFC limit)": "cycles only (EFC limit)",
    "samo starost (koledarsko)": "age only (calendar)",
    "dejanska življenjska doba (nižje od obeh)": "service life (lower of the two)",
}

# Fragments that recur inside generated strings ("brez baterije: 1.234 EUR/a"),
# where the number rules out an exact match. Applied longest-first, after the
# exact lookup fails.
GLOSSARY_PARTS = {
    "Gospodinjstvo": "Household",
    "brez baterije": "without battery",
    "poraba gospodinjstva": "household consumption",
    "dogovorjena obračunska moč": "agreed billing power",
    "EUR/kWh vgrajene kapacitete": "EUR/kWh installed capacity",
    "osenčeno območje = prihranek glede na različico brez baterije":
        "shaded area = saving against the no-battery case",
    "Modro = vrednost naslednje kWh kapacitete; dodajanje se izplača, dokler je "
    "krivulja nad črtkano črto stroška":
        "Blue = value of the next kWh of capacity; adding pays while the curve "
        "stays above the dashed cost line",
    "scenarij C": "scenario C",
    "let": "years",
}

_TRANSLATABLE = re.compile(r"[A-Za-zČčŠšŽž]{3}")


def t(sl, en=None):
    """Pick the string for the active language. For new code that has both."""
    return sl if (LANG == "sl" or en is None) else en


def translate_figure(fig, lang=None):
    """Rewrite every text artist in a finished figure into `lang`.

    In place and one-way: GLOSSARY maps Slovenian to English, so `lang="sl"`
    (the default) is a no-op and nothing has to be translated back.
    """
    lang = LANG if lang is None else lang
    if lang == "sl":
        return fig
    parts = sorted(GLOSSARY_PARTS.items(), key=lambda kv: -len(kv[0]))

    # The raw title `finish` stashed for re-wrapping is translated too, and
    # first: `show` re-wraps from it afterwards, which would otherwise put the
    # Slovenian original back over the translated artist.
    driven = set()          # title artists `show` will redraw from `_pf_head`
    for ax in fig.axes:
        head = getattr(ax, "_pf_head", None)
        if head is None:
            continue
        title, subtitle, wrap = head
        ax._pf_head = (_translate(title, parts),
                       None if subtitle is None else _translate(subtitle, parts),
                       wrap)
        driven.update(id(a) for a in (ax.title,
                                      getattr(ax, "_left_title", None),
                                      getattr(ax, "_right_title", None)) if a)

    for artist in fig.findobj(Text):
        text = artist.get_text()
        # A title driven by `_pf_head` is translated above, from the unwrapped
        # original. Looking its wrapped lines up again would only report the
        # fragments the line breaks cut in half as untranslated.
        if text and id(artist) not in driven:
            # A wrapped title is several lines; each is looked up on its own so
            # the line breaks do not hide it from an exact glossary entry.
            out = "\n".join(_translate(line, parts) for line in text.split("\n"))
            if out != text:
                artist.set_text(out)
    return fig


def _translate(text, parts):
    """One string into English: exact entry first, then known fragments."""
    if not text or not _TRANSLATABLE.search(text):
        return text
    if text in GLOSSARY:
        return GLOSSARY[text]
    out = text
    for sl, en in parts:
        out = out.replace(sl, en)
    if out == text:
        MISSING_TRANSLATIONS.setdefault(text, None)
    return out


# --- geometry normalisation ------------------------------------------------

def _as_figure(fig):
    """Accept a Figure, an Axes (pandas `.plot` only hands back one), or None."""
    if fig is None:
        return plt.gcf()
    return fig.get_figure() if hasattr(fig, "get_figure") else fig


INK_FLOOR_PT = 0.4        # thinner than this and a stroke drops out in print
MARKER_FLOOR_PT = 1.5     # smaller than this and a marker is a smudge


def _ieee_restyle(fig):
    """Put an already-drawn figure into the article's typeface and size.

    Building inside `ieee_style()` is exact; this is the retrofit for a figure
    whose notebook is expensive to re-run. Sizes are SCALED rather than set to
    IEEE_FONT_PT flat, so the hierarchy the figure was drawn with survives --
    a 12 pt title stays larger than a 10 pt label. What does not follow: offsets
    given in points (`textcoords="offset points"`) and bbox pads, which stay
    where they were placed.

    The scale is recorded on the figure so the frame text can follow it: the
    header and legend are drawn AFTER this runs, and quoting them at a fixed
    9.5 pt would leave a \columnwidth figure with a legend bigger than its own
    axis labels.
    """
    if abs(plt.rcParams["font.size"] - IEEE_FONT_PT) < 1e-9:
        return False              # the notebook is already in IEEE text
    scale = IEEE_FONT_PT / plt.rcParams["font.size"]
    fig._pf_text_scale = scale
    fig._pf_text_family = "serif"
    # "serif" rather than the concrete list: the list is resolved once from
    # rcParams when the figure draws, instead of being searched for -- and
    # warned about, per artist -- on every text object here.
    plt.rcParams["font.serif"] = RCPARAMS_IEEE["font.serif"]
    for artist in fig.findobj(Text):
        artist.set_fontsize(artist.get_fontsize() * scale)
        artist.set_fontfamily("serif")
    return True


def _scale_ink(fig, scale):
    """Scale every stroke in the figure by `scale`, with a floor.

    Stroke weight is given in points, so a resize leaves it alone -- and that is
    precisely the bug. Text is absolute because the reader's eye is; ink is a
    fraction of the picture and has to follow it. A 2 pt curve that reads
    cleanly across 7.16 in is double-weight on 3.5 in, which is what closed the
    dash patterns up into solid and lost the detail they encode.

    Scaled rather than set flat, so the weights a cell chose to tell an
    emphasised curve from a baseline rule survive the move. The floors are what
    keep a hairline from vanishing altogether at the bottom of the range.
    """
    if scale >= 1.0 - 1e-9 or getattr(fig, "_pf_ink_scaled", False):
        return False
    fig._pf_ink_scaled = True

    def down(value, floor=INK_FLOOR_PT):
        return max(floor, value * scale) if value else value

    for line in fig.findobj(Line2D):
        line.set_linewidth(down(line.get_linewidth()))
        if line.get_marker() not in (None, "None", "none", " ", ""):
            line.set_markersize(down(line.get_markersize(), MARKER_FLOOR_PT))
            line.set_markeredgewidth(down(line.get_markeredgewidth()))
    for patch in fig.findobj(Patch):     # Spine is a Patch, so this reaches them
        patch.set_linewidth(down(patch.get_linewidth()))
    for coll in fig.findobj(Collection):
        widths = coll.get_linewidth()
        try:
            coll.set_linewidth([down(float(v)) for v in widths])
        except TypeError:
            coll.set_linewidth(down(float(widths)))

    # Ticks and gridlines are rebuilt from these whenever a locator changes its
    # mind about how many to draw, which the layout pass is quite capable of
    # provoking -- so set them as well as scaling the ones already drawn. The
    # grid is only touched where it is already on: `axis.grid(**kw)` turns it ON
    # as a side effect, and two notebooks run with `pf.use(grid=False)`.
    for ax in fig.axes:
        for which in ("major", "minor"):
            ax.tick_params(which=which,
                           width=down(plt.rcParams["xtick.%s.width" % which]))
        for axis in (ax.xaxis, ax.yaxis):
            if any(gl.get_visible() for gl in axis.get_gridlines()):
                axis.grid(True, linewidth=down(plt.rcParams["grid.linewidth"]))
    return True



def _normalize(fig, preset, ratio=None):
    """Resize a figure to the active preset. Returns a provenance note or None.

    The width comes from the preset. `ratio` sizes the PLOT BOX, and
    `chart_frame`'s header and legend bands are measured and added around it --
    so the same `ratio` is the same picture shape whether the figure carries a
    one-row legend or a four-row one. It used to size the whole canvas, with the
    bands carved out of it, which made `ratio=0.61` mean a 3.9 in plot on one
    figure and 3.1 in on the next. A figure with no frame has no bands and is
    sized by `ratio` alone.

    The resize alone does nothing to the text, and does not need to: matplotlib
    font sizes are absolute points, so shrinking the canvas is exactly what
    building the same code at the smaller figsize would have produced. Two
    things do not survive that reasoning and are handled explicitly -- the
    typeface an IEEE preset wants (`_ieee_restyle`), and stroke weight, which is
    quoted in points but reads as a fraction of the canvas (`_scale_ink`).
    """
    w0, h0 = fig.get_size_inches()
    if preset == "as_built":
        _scale_panel_text(fig)
        _frame_bands(fig)      # measured anyway, so the legend gap is still right
        return None
    if preset not in PRESETS:
        raise ValueError(f"unknown preset {preset!r}; expected one of "
                         f"{', '.join(PRESETS)} or 'as_built'")
    w = PRESETS[preset]
    plot_h = w * (ratio if ratio is not None else h0 / w0)

    # The bands are measured at the final WIDTH and the final text, both of
    # which they depend on, and at a provisional height, which they do not.
    notes = []
    fig.set_size_inches(w, plot_h, forward=True)
    if preset in IEEE_PRESETS and _ieee_restyle(fig):
        notes.append("IEEE text applied to a figure drawn in the notebook style "
                     "(scaled, not rebuilt)")
    if _scale_ink(fig, w / w0):
        notes.append(f"stroke weights scaled {w / w0:.2f}x to the narrower canvas")
    _scale_panel_text(fig)
    head_in, foot_in = _frame_bands(fig)

    h = plot_h + head_in + foot_in
    if abs(w - w0) > 1e-3 or abs(h - h0) > 1e-3:
        notes.insert(0, f"resized from {w0:.2f}x{h0:.2f} to {w:.2f}x{h:.2f} in")
    fig.set_size_inches(w, h, forward=True)
    return "; ".join(notes) or None



class _white_ground:
    """Paint the figure white for the duration of a save, then put it back.

    `save_fig(facecolor=...)` only reaches the figure patch. The studio ground
    is also set on every axes, and an off-white axes rectangle on a white page
    is the faint grey box this exists to avoid.
    """

    def __init__(self, fig, enabled=True):
        self.fig, self.enabled, self.saved = fig, enabled, None

    def __enter__(self):
        if not self.enabled:
            return self.fig
        self.saved = (self.fig.get_facecolor(),
                      [(ax, ax.get_facecolor()) for ax in self.fig.axes])
        self.fig.set_facecolor("white")
        for ax in self.fig.axes:
            ax.set_facecolor("white")
        return self.fig

    def __exit__(self, *exc):
        if self.saved is None:
            return False
        fig_fc, axes_fc = self.saved
        self.fig.set_facecolor(fig_fc)
        for ax, fc in axes_fc:
            ax.set_facecolor(fc)
        return False


def _layout(fig, layout, rect):
    """Run the layout pass the figure asked for, if any."""
    if _apply_frame(fig):
        return          # chart_frame's bands are measured and the axes placed
    band_rect = getattr(fig, "_pf_frame_rect", None)
    if band_rect is not None:
        fig.tight_layout(rect=band_rect)   # lay out again, bands still reserved
        return
    if layout in (None, "frame"):
        return
    if layout == "auto" and fig.get_layout_engine() is not None:
        return          # built with constrained layout; tight_layout is ignored
    fig.tight_layout(**({"rect": rect} if rect else {}))



# --- the terminator --------------------------------------------------------

def show(fig=None, name=None, *, save_pdf=None, png=False,
         preset=None, ratio=None, layout="tight", rect=None, paper=None,
         subdir=None, lang=None, titles=None, note=None, close=False):
    """Translate, resize, lay out, export, then display one figure.

    This replaces the `plt.tight_layout(); plt.show()` that ended every figure
    cell:

        pf.show(fig, "cost_vs_capacity")

    `name` is what the article refers to the figure by, and it names the folder
    under `Results/Figures/` -- keep it stable, since the LaTeX side uses it.
    Called without a name nothing is written, so a cell can be converted before
    anyone has decided what the figure is called.

    `save_pdf=None` falls back to the module switch `pf.SAVE_PDF`: set that to
    False once and no figure in the session writes anything.

    `layout`: "tight" (the default, what the cells did), "frame" (none -- the
    figure went through `chart_frame`, which already measured its own bands),
    "auto" (skip when the figure was built with constrained layout), or None.

    `titles=False` (or `pf.use(titles=False)` for the whole notebook) leaves the
    title out of the image, the way an IEEE figure wants it -- the caption in
    the article is the title. The text is written into the export's provenance
    instead of being lost.

    The order below is load-bearing. The inline backend closes a figure when it
    is shown, so the save must happen BEFORE `plt.show()` -- saving afterwards
    silently writes a blank page.

    Returns nothing on purpose. A cell whose last statement is this call would
    display a returned Figure as a SECOND inline image, which is where the
    duplicate copies of the figures with no other output came from.
    """
    fig = _as_figure(fig)
    preset = PRESET if preset is None else preset
    save_pdf = SAVE_PDF if save_pdf is None else save_pdf
    # Read by `_frame_bands` and `_apply_frame`, which run below: the frame is
    # laid out here rather than in `chart_frame`, so a per-figure `titles=`
    # reaches it now instead of being decided by the module default.
    fig._pf_titles = TITLES if titles is None else titles

    translate_figure(fig, LANG if lang is None else lang)
    resize_note = _normalize(fig, preset, ratio)
    _layout(fig, layout, rect)
    # Titles are wrapped to the axes box, which only the layout pass above
    # decides -- so wrap against it, and lay out again if a title grew a line.
    caption = heads(fig) + [h for h in [getattr(fig, "_pf_frame_head", None)] if h]
    if _rewrap_heads(fig, TITLES if titles is None else titles):
        _layout(fig, layout, rect)
    # A `key_legend` is anchored in axes fractions before the axes box exists.
    # Now it does, so the gap can be set in inches -- and the layout re-run to
    # give the moved legend its room.
    if _reanchor_key_legends(fig):
        _layout(fig, layout, rect)
        _reanchor_key_legends(fig)

    if name and (save_pdf or png):
        notes = [n for n in (note, resize_note) if n]
        # A trimmed export is no longer the width it was built at, so LaTeX
        # rescales it -- and rescaling is what changes the text size. An IEEE
        # figure is therefore never trimmed; `chart_frame`'s reserved header and
        # legend bands are ink-free and would be trimmed away too.
        tight = preset not in IEEE_PRESETS and layout != "frame"
        with _white_ground(fig, PAPER_GROUND if paper is None else paper):
            save_fig(fig, name, SUBDIR if subdir is None else subdir,
                     png=png, tight=tight, caption=caption,
                     note="; ".join(notes) or None)

    plt.show()
    if close:
        plt.close(fig)


# --- provenance ------------------------------------------------------------

def _git(*args, cwd=None):
    """Run one git command, returning stripped stdout or None if it failed."""
    # encoding= rather than text=: text=True decodes with the LOCALE codec, and
    # on a Windows box that is the ANSI codepage (cp1250 here), which cannot
    # decode a diff carrying a U+2212 minus or any other non-Latin-2 character.
    # The decode then blows up inside subprocess's reader THREAD, which leaves
    # `out.stdout` as None on a returncode of 0 -- an AttributeError below
    # rather than a caught failure. git speaks UTF-8, so say so.
    try:
        out = subprocess.run(("git", "-C", str(cwd or REPO_ROOT)) + args,
                             capture_output=True, timeout=15,
                             encoding="utf-8", errors="replace")
    except (OSError, subprocess.SubprocessError):
        return None
    if out.returncode != 0 or out.stdout is None:
        return None
    return out.stdout.strip()


def git_trace():
    """The commit a figure was exported from, and whether that commit is enough.

    `dirty` is the field that matters: a figure exported from a modified tree is
    NOT reproducible from `commit` alone, which is why the diff is written next
    to it.
    """
    if _git("rev-parse", "--is-inside-work-tree") != "true":
        return {"available": False}

    status = _git("status", "--porcelain") or ""
    dirty_files = [ln[3:] for ln in status.splitlines() if ln.strip()]
    return {
        "available": True,
        "commit": _git("rev-parse", "HEAD"),
        "commit_short": _git("rev-parse", "--short", "HEAD"),
        "branch": _git("rev-parse", "--abbrev-ref", "HEAD"),
        "describe": _git("describe", "--always", "--dirty", "--tags"),
        "subject": _git("log", "-1", "--pretty=%s"),
        "committed_at": _git("log", "-1", "--pretty=%cI"),
        "remote": _git("config", "--get", "remote.origin.url"),
        "dirty": bool(dirty_files),
        "dirty_file_count": len(dirty_files),
        "dirty_files": dirty_files[:50],
        "dirty_stat": _git("diff", "--stat", "HEAD") if dirty_files else None,
    }


def _ipython():
    try:
        from IPython import get_ipython
    except ImportError:
        return None
    return get_ipython()


def _source_location():
    """Which notebook, and which cell in it, called `save_fig`.

    The notebook path is not something the kernel is reliably told, so each
    known way of learning it is tried in turn and whichever answered is
    recorded, rather than one guess being presented as fact.
    """
    import inspect

    loc = {"notebook": None, "notebook_detected_by": None,
           "cell_execution_count": None, "caller": None, "cwd": os.getcwd()}

    ip = _ipython()
    if ip is not None:
        # VS Code sets this in the user namespace; JupyterLab >= 3.6 exports the
        # session name to the environment.
        vsc = ip.user_ns.get("__vsc_ipynb_file__")
        jpy = os.environ.get("JPY_SESSION_NAME")
        if vsc:
            loc["notebook"], loc["notebook_detected_by"] = str(vsc), "__vsc_ipynb_file__"
        elif jpy:
            loc["notebook"], loc["notebook_detected_by"] = str(jpy), "JPY_SESSION_NAME"
        loc["cell_execution_count"] = ip.execution_count

    # Outermost non-library frame, which is the cell body under IPython and the
    # script otherwise. Gives a real file:line whenever the call is not in a cell.
    try:
        outer = inspect.stack()[-1]
        loc["caller"] = f"{outer.filename}:{outer.lineno}"
    except Exception:
        pass

    if loc["notebook"]:
        try:
            loc["notebook"] = str(Path(loc["notebook"]).resolve())
        except OSError:
            pass
    return loc


def _current_cell_source():
    """Source of the cell that is executing, for `cell.py`.

    `In[-1]` is the cell currently running, which is the one that drew the
    figure -- the single most direct answer to "where did this picture come
    from", and independent of whether the notebook path was detectable.
    """
    ip = _ipython()
    if ip is None:
        return None
    history = ip.user_ns.get("In")
    if not history or len(history) < 2:
        return None
    return history[-1]


def _write_provenance(out_dir, name, fig, written, formats, dpi, note,
                      tight=True, caption=()):
    import matplotlib

    git = git_trace()
    loc = _source_location()

    record = {
        "figure": name,
        "created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "files": [p.name for p in written],
        "export": {
            "formats": list(formats),
            "dpi": dpi,
            "bbox": "tight" if tight else "exact figure size",
            "figsize_in": [round(v, 4) for v in fig.get_size_inches()],
            "matplotlib": matplotlib.__version__,
            "python": sys.version.split()[0],
        },
        "source": loc,
        "git": git,
    }
    if caption:
        record["caption"] = list(caption)
    if note:
        record["note"] = note

    # The diff is what makes a dirty-tree export recoverable; without it the
    # commit id points at code that is not what ran.
    if git.get("dirty"):
        diff = _git("diff", "HEAD", "--", ".", *DIFF_EXCLUDE) or ""
        truncated = len(diff.encode()) > MAX_DIFF_BYTES
        if truncated:
            diff = diff.encode()[:MAX_DIFF_BYTES].decode(errors="ignore")
            diff += "\n\n... TRUNCATED: diff exceeded MAX_DIFF_BYTES ...\n"
        (out_dir / "uncommitted.diff").write_text(diff, encoding="utf-8")
        record["git"]["diff_file"] = "uncommitted.diff"
        record["git"]["diff_truncated"] = truncated
        record["git"]["diff_excludes"] = list(DIFF_EXCLUDE)

    cell = _current_cell_source()
    if cell:
        (out_dir / "cell.py").write_text(cell, encoding="utf-8")
        record["source"]["cell_file"] = "cell.py"

    (out_dir / "source.json").write_text(
        json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out_dir / "SOURCE.md").write_text(_readable(record), encoding="utf-8")
    return record


def _readable(record):
    """The same record as a few lines someone can read in the folder."""
    git, src = record["git"], record["source"]
    lines = [f"# {record['figure']}", "",
             f"Exported {record['created_utc']}",
             f"Files: {', '.join(record['files'])}",
             f"Size: {record['export']['figsize_in'][0]} x "
             f"{record['export']['figsize_in'][1]} in "
             f"@ {record['export']['dpi']} dpi ({record['export']['bbox']})", ""]
    if record.get("note"):
        lines += [f"> {record['note']}", ""]
    if record.get("caption"):
        lines += ["## Caption", "",
                  "The title text for this figure, for the article's "
                  "`\\caption{...}`:", ""]
        lines += [f"- {c}" for c in record["caption"]] + [""]
    lines += ["## Source", "",
              f"- notebook: {src.get('notebook') or 'not detected'}"
              + (f" (via {src['notebook_detected_by']})" if src.get("notebook_detected_by") else ""),
              f"- cell execution count: {src.get('cell_execution_count')}",
              f"- caller: {src.get('caller')}",
              f"- cell source: {src.get('cell_file', 'not captured')}", ""]
    lines += ["## Git", ""]
    if not git.get("available"):
        lines += ["- not a git working tree", ""]
    else:
        lines += [f"- commit: {git['commit']} ({git['branch']})",
                  f"- subject: {git['subject']}",
                  f"- describe: {git['describe']}"]
        if git["dirty"]:
            lines += ["",
                      f"**Working tree was DIRTY ({git['dirty_file_count']} files) — the commit "
                      f"above does NOT reproduce this figure on its own.**",
                      f"See `{git.get('diff_file')}`"
                      + (" (truncated)" if git.get("diff_truncated") else "")
                      + f", which excludes {', '.join(DIFF_EXCLUDE)} — the notebook "
                      "side is in `cell.py`.", "",
                      "```", git.get("dirty_stat") or "", "```"]
        else:
            lines += ["- clean tree: this commit reproduces the figure"]
    return "\n".join(lines) + "\n"


# --- the export ------------------------------------------------------------

def _overflow_in(fig, tol=0.02):
    """Inches by which the drawn content runs outside the figure canvas.

    Only meaningful for an untrimmed export. `bbox_inches="tight"` grows the
    saved page around anything that overflows, which is why the trimmed path
    never needed this; an IEEE preset writes the canvas at its declared width,
    so whatever falls outside is cut off silently. Returns None when nothing
    overflows by more than `tol`, which absorbs the sub-point rounding every
    text bbox carries.
    """
    try:
        fig.canvas.draw()
        bb = fig.get_tightbbox(fig.canvas.get_renderer())
    except Exception:
        return None          # never let a diagnostic stop an export
    w, h = fig.get_size_inches()
    over = max(-bb.x0, -bb.y0, bb.x1 - w, bb.y1 - h)
    return float(over) if over > tol else None


def save_fig(fig, name, subdir=None, *, png=False, extra_formats=(),
             dpi=EXPORT_DPI, tight=True, transparent=False, facecolor=None,
             caption=(), note=None):
    """Write one figure, plus its provenance, into its own folder.

        Results/Figures/[subdir/]<name>/
            <name>.pdf          always
            <name>.png          when png=True
            source.json         machine-readable provenance
            SOURCE.md           the same, readable
            cell.py             the notebook cell that drew it
            uncommitted.diff    only when the tree was dirty

    `name` is what the article refers to the figure by -- keep it stable, since
    the LaTeX side names the folder and the file.

    `tight` trims the export to its ink. Convenient, but it means the file is no
    longer the width the figure was built at, so LaTeX rescales it -- and
    rescaling is what changes the text size. Pass `tight=False` when the pdf is
    built at an IEEE width and placed at natural size; `show()` derives this
    from the preset so it never has to be typed.

    With `tight=False` nothing trims overflowing labels, so call
    `fig.tight_layout()` (or build with constrained layout) before saving.

    `caption` is the title text the figure would have carried. With
    `pf.use(titles=False)` it is not drawn into the image, so it is recorded
    here instead: it is what the article's `\\caption{...}` should say.

    This is the only function that writes into `Results/Figures` -- every
    resolution, format and provenance decision is made here, once.
    """
    base = FIGURE_DIR if subdir is None else FIGURE_DIR / subdir
    out_dir = base / name
    out_dir.mkdir(parents=True, exist_ok=True)

    formats = ["pdf"]
    if png:
        formats.append("png")
    formats += [f for f in extra_formats if f not in formats]

    # Turning trimming OFF cannot be done with a kwarg: savefig resolves
    # `bbox_inches=None` through `_val_or_rc` back to `savefig.bbox`, which
    # RCPARAMS sets to "tight". Only the rcParam itself switches it off.
    kwargs = {"dpi": dpi, "transparent": transparent, "pad_inches": 0.02}
    if facecolor is not None:
        kwargs["facecolor"] = facecolor
        kwargs["edgecolor"] = facecolor
    exact_bbox = {"savefig.bbox": None}

    overflow = None if tight else _overflow_in(fig)
    if overflow:
        # With the trim off, nothing grows the canvas around a label that runs
        # past it -- it is simply cut at the edge, and a PDF gives no sign. The
        # figure is still written, because a clipped figure the author can see
        # is more useful than no figure and a traceback.
        warnings.warn(
            f"{name}: content extends {overflow:.2f} in beyond the "
            f"{fig.get_size_inches()[0]:.2f} x {fig.get_size_inches()[1]:.2f} in "
            f"canvas and will be CLIPPED. Shorten the label, or give show() a "
            f"taller ratio=.", stacklevel=2)

    written = []
    for fmt in formats:
        path = out_dir / f"{name}.{fmt}"
        with rc_context({} if tight else exact_bbox):
            fig.savefig(path, format=fmt, **kwargs)
        written.append(path)

    _write_provenance(out_dir, name, fig, written, formats, dpi, note, tight,
                      caption)
    return written


def latex_figure(name, caption, label=None, subdir=None, span=False,
                 placement="!t"):
    """The LaTeX block for a figure `save_fig` just wrote.

    `span=True` uses `figure*`, the IEEEtran float that spans both columns.
    """
    stem = f"{name}/{name}" if subdir is None else f"{subdir}/{name}/{name}"
    label = label or f"fig:{name.replace('_', '-')}"
    env = "figure*" if span else "figure"
    width = "textwidth" if span else "columnwidth"
    return (f"\\begin{{{env}}}[{placement}]\n"
            "  \\centering\n"
            f"  \\includegraphics[width=\\{width}]{{{stem}}}\n"
            f"  \\caption{{{caption}}}\n"
            f"  \\label{{{label}}}\n"
            f"\\end{{{env}}}")


# --- legacy ----------------------------------------------------------------

def slug(text, fallback="figure"):
    """A filesystem- and LaTeX-safe folder name from a figure title."""
    out = re.sub(r"[^\w\-]+", "_", str(text).strip(), flags=re.UNICODE).strip("_")
    return out.lower() or fallback


def plotMultiY(X, Y=None, X_label="X_os", Y_Label=None,
               legend=None, title="title",
               save=False, grid=True, save_pdf=False, show_title=False):
    """Plot several Y series against a shared X axis, padding mismatched lengths.

    The signature is unchanged, so the seven call sites in `Household_local
    model.ipynb` keep working without an edit -- which matters because that
    notebook's state is a trained DQN that only exists after a long run. What
    changed is underneath: it builds its own figure instead of drawing into
    whatever `plt.gca()` happened to be, `save_pdf=True` now writes into
    `Results/Figures/` with provenance instead of dropping a PDF named after the
    title into the working directory, and it returns `(fig, ax)`.
    """
    if Y is None:
        Y = []
    if Y_Label is None:
        Y_Label = ["" for _ in range(max(1, len(Y)))]
    if legend is None:
        legend = ["" for _ in range(max(1, len(Y)))]

    X = list(X)
    Y = [list(series) for series in Y]
    Y_Label = list(Y_Label)
    legend = list(legend)

    colors = ["C0", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"]
    line_type = ["-", "--", ":", "-."]

    fig, ax = plt.subplots()
    if show_title:
        ax.set_title(title)

    if len(Y_Label) < len(Y):
        for _ in range(len(Y) - len(Y_Label)):
            Y_Label.append(Y_Label[0])

    if len(legend) < len(Y):
        for _ in range(len(Y) - len(legend)):
            legend.append(legend[0])

    if len(Y) > 0:
        if len(X) < len(Y[0]):
            X += [X[-1]] * (len(Y[0]) - len(X))
        elif len(X) > len(Y[0]):
            X = X[:len(Y[0])]

    for i in range(len(Y) - 1):
        if len(Y[i + 1]) < len(Y[i]):
            Y[i + 1] += [Y[i + 1][-1]] * (len(Y[i]) - len(Y[i + 1]))
        elif len(Y[i + 1]) > len(Y[i]):
            Y[i + 1] = Y[i + 1][:len(Y[i])]

    if grid:
        ax.grid(color="Black", linestyle="--", linewidth=0.5)
    else:
        ax.grid(False)

    for i in range(len(Y)):
        ax.plot(X, Y[i], color=colors[i], label=legend[i],
                linestyle=line_type[i % len(line_type)])
        ax.legend()
        if i > 0:
            if Y_Label[i] != Y_Label[i - 1]:
                ax.set_ylabel(Y_Label[i], color=colors[i])
                ax.tick_params(axis="y", colors=colors[i])
        else:
            ax.set_xlabel(X_label)
            ax.set_ylabel(Y_Label[i] if len(Y_Label) > 0 else "")

    # Date axis gets month ticks; otherwise ~10 evenly spaced labels.
    if all(isinstance(x, (date, datetime)) for x in X):
        ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    else:
        if len(X) > 10:
            step = max(1, len(X) // 10)
            ax.set_xticks(X[::step])
            ax.tick_params(axis="x", labelrotation=45)

    show(fig, slug(title) if (save or save_pdf) else None,
         save_pdf=bool(save_pdf), png=bool(save))
    return fig, ax
