"""Publication-quality figure export shared by every notebook.

One module decides the export resolution, the file formats and the provenance
record, so a figure that ends up in the article is written the same way whichever
notebook produced it -- the same reason the solver gap lives in
`Horizon_Comparison` rather than being retyped per study.

Two resolutions, because they are two different questions:

  DISPLAY_DPI   what the inline PNG in the .ipynb is rendered at. IPython passes
                `fig.dpi` to `print_figure`, so this is the knob for the picture
                you see in the notebook -- and for what a right-click "save
                image as" gives you. Raising it to 600 would multiply every
                stored output in these already 1-4 MB notebooks by ~30x.
  EXPORT_DPI    what `savefig` writes. This is the article's resolution, and it
                is independent of the inline preview.

Three formats, because they are three different jobs:

  pdf   always written. Self-contained vector art with the fonts embedded as
        TrueType outlines (`pdf.fonttype: 42`, never Type 3, which IEEE rejects).
        Needs no TeX installation, so this is the one that always works.
  pgf   opt-in (`pgf=True`). LaTeX source, not an image: the text is typeset by
        the article itself, so it inherits IEEEtran's Times at exactly the size
        the surrounding body text uses. This is what makes figure text match
        automatically. Requires a TeX installation -- see `pgf_available()`.
  png   opt-in (`png=True`). 600 dpi raster, for anywhere that cannot take
        vector art.

Every export gets its own folder holding the image files plus the provenance
needed to find the code that drew it again: `source.json`, the producing
notebook cell as `cell.py`, and the git commit -- with the uncommitted diff
alongside it when the tree was dirty, because a commit id alone does not
reproduce a figure exported from a modified working tree.
"""
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

EXPORT_DPI = 600          # raster resolution for the article
DISPLAY_DPI = 110         # inline preview in the notebook, unchanged

REPO_ROOT = Path(__file__).resolve().parent

# Where exports land. Kept beside the CSV results rather than in the notebook's
# working directory, so a re-run overwrites the article's figures in place.
FIGURE_DIR = REPO_ROOT / "Results" / "Figures"

# A dirty-tree diff is written into the figure folder so the exact source can be
# recovered later, but a diff that touches an .ipynb runs to megabytes of stored
# output. Past this it is truncated and `source.json` says so.
MAX_DIFF_BYTES = 1_000_000

# --- IEEE conference geometry ---------------------------------------------
# IEEEtran, US Letter, two columns. A figure placed at \columnwidth must be
# BUILT at this width: scaling in \includegraphics rescales the text with the
# picture, which is exactly what the pgf route exists to avoid.
IEEE_COLUMN_W = 3.5       # inches, \columnwidth
IEEE_PAGE_W = 7.16        # inches, \textwidth -- figure* spanning both columns

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

# Preamble LaTeX runs when it measures the text for a .pgf export. It should
# match the article's own preamble: the measurement decides where matplotlib
# places every label, so a mismatch here shows up as spacing that is slightly
# off once the figure is \input into the document.
#
# `newtxtext,newtxmath` are IEEEtran's Times metrics -- add them here once the
# article's preamble loads them, otherwise measurement happens in Computer
# Modern and the labels sit fractionally wide.
PGF_PREAMBLE = "\n".join([
    r"\usepackage[T1]{fontenc}",      # Slovenian č/š/ž in labels
    r"\usepackage[utf8]{inputenc}",
])

# Applied only while a .pgf is being written, via rc_context, so the notebook's
# inline preview never depends on a TeX installation being present.
#
# What a .pgf does and does not take from the document, checked against
# backend_pgf rather than assumed:
#
#   TYPEFACE  inherited. matplotlib emits `\rmfamily` or `\sffamily` per text
#             node -- a *relative* command -- so `font.family: "serif"` resolves
#             to whatever roman font the article loads, i.e. IEEEtran's Times.
#             This is the real benefit of the pgf route.
#   SIZE      NOT inherited. `_font_properties_str` always appends an absolute
#             `\fontsize{<font.size>}{1.2*<font.size>}`, so the pt size is fixed
#             here, in matplotlib, and no `\footnotesize` around the `\input`
#             can override it. Set `font.size` to the size you want in print.
#
# `pgf.rcfonts` only gates a fontspec block in the measuring preamble, and that
# block is inside `\ifdefined\pdftexversion\else` -- so under pdflatex it is a
# no-op. It is set False for the xelatex/lualatex case.
PGF_RCPARAMS = {
    "pgf.texsystem": "pdflatex",
    "pgf.rcfonts": False,
    "pgf.preamble": PGF_PREAMBLE,
    "text.usetex": True,
}

# --- IEEE text ------------------------------------------------------------
# IEEEtran sets the body in Times at 10pt; figure text is conventionally 8pt.
# `serif` is the load-bearing entry: it becomes `\rmfamily` in a .pgf and picks
# up the article's Times, and it selects a real Times for the self-contained pdf
# so the two routes look the same.
IEEE_FONT_PT = 8
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


def apply(paper=False, ieee=False):
    """Push the export settings onto the live rcParams.

    Call this AFTER a notebook's own `plt.rcParams.update({...})` style block, so
    the export keys win over anything the style set.

    `ieee=True` additionally switches the text to Times at IEEE_FONT_PT on a
    white ground. It changes the inline previews too, which is intended: the
    preview should then look like what the article will print.
    """
    from matplotlib import pyplot as plt

    plt.rcParams.update(RCPARAMS_IEEE if ieee else
                        RCPARAMS_PAPER if paper else RCPARAMS)
    return plt.rcParams


def ieee_style():
    """Context manager: build one figure IEEE-styled, leaving the notebook alone.

        with fx.ieee_style():
            fig, ax = plt.subplots(figsize=fx.ieee_figsize())
            ...
        fx.save_fig(fig, "name", pgf=True, tight=False)

    Preferred over `apply(ieee=True)` when only some figures go in the paper --
    the study's own styling stays in place for everything else.
    """
    from matplotlib import rc_context

    return rc_context(RCPARAMS_IEEE)


def ieee_figsize(width="column", ratio=0.62):
    """Figure size in inches for an IEEE conference figure.

    `width`: "column" for a single column (\\columnwidth), "page" for a figure*
    spanning both (\\textwidth), or a number of inches.

    Build the figure at this size and place it UNSCALED. The default ratio is
    near 1/phi, which is a reasonable single-plot proportion; pass a taller one
    for stacked panels.
    """
    if width == "column":
        w = IEEE_COLUMN_W
    elif width == "page":
        w = IEEE_PAGE_W
    else:
        w = float(width)
    return (w, w * ratio)


# macOS puts MacTeX here and adds it to the PATH through /etc/paths.d/TeX, which
# only login shells run. A Jupyter kernel started by an editor often does not
# inherit that, so TeX is installed and still invisible to the kernel.
TEX_FALLBACK_DIRS = ("/Library/TeX/texbin", "/usr/local/texlive/bin",
                     "/opt/homebrew/bin")


def _ensure_tex_on_path(texsystem):
    """Find the TeX binary, adding the known install dirs to PATH if needed."""
    from shutil import which

    if which(texsystem):
        return True
    for d in TEX_FALLBACK_DIRS:
        if which(texsystem, path=d):
            os.environ["PATH"] = d + os.pathsep + os.environ.get("PATH", "")
            return True
    return False


def pgf_available(texsystem=None):
    """Whether a .pgf export can be written: can the TeX binary be found?

    The pgf backend shells out to LaTeX to measure text at save time, so this is
    required even though the output is source rather than an image. Has the side
    effect of putting TeX on PATH for this process when it is installed but not
    visible -- see TEX_FALLBACK_DIRS.
    """
    return _ensure_tex_on_path(texsystem or PGF_RCPARAMS["pgf.texsystem"])


# --- provenance ------------------------------------------------------------

def _git(*args, cwd=None):
    """Run one git command, returning stripped stdout or None if it failed."""
    try:
        out = subprocess.run(("git", "-C", str(cwd or REPO_ROOT)) + args,
                             capture_output=True, text=True, timeout=15)
    except (OSError, subprocess.SubprocessError):
        return None
    return out.stdout.strip() if out.returncode == 0 else None


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


def _write_provenance(out_dir, name, fig, written, formats, dpi, note, tight=True):
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
            "pgf_bbox": "exact figure size",
            "figsize_in": [round(v, 4) for v in fig.get_size_inches()],
            "matplotlib": matplotlib.__version__,
            "python": sys.version.split()[0],
        },
        "source": loc,
        "git": git,
    }
    if note:
        record["note"] = note

    # The diff is what makes a dirty-tree export recoverable; without it the
    # commit id points at code that is not what ran.
    if git.get("dirty"):
        diff = _git("diff", "HEAD") or ""
        truncated = len(diff.encode()) > MAX_DIFF_BYTES
        if truncated:
            diff = diff.encode()[:MAX_DIFF_BYTES].decode(errors="ignore")
            diff += "\n\n... TRUNCATED: diff exceeded MAX_DIFF_BYTES ...\n"
        (out_dir / "uncommitted.diff").write_text(diff, encoding="utf-8")
        record["git"]["diff_file"] = "uncommitted.diff"
        record["git"]["diff_truncated"] = truncated

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
                      + (" (truncated)" if git.get("diff_truncated") else "") + ".", "",
                      "```", git.get("dirty_stat") or "", "```"]
        else:
            lines += ["- clean tree: this commit reproduces the figure"]
    return "\n".join(lines) + "\n"


# --- the export ------------------------------------------------------------

def save_fig(fig, name, subdir=None, *, pgf=False, png=False, extra_formats=(),
             dpi=EXPORT_DPI, tight=True, transparent=False, facecolor=None,
             note=None):
    """Write one figure, plus its provenance, into its own folder.

        Results/Figures/[subdir/]<name>/
            <name>.pdf          always
            <name>.pgf          when pgf=True
            <name>.png          when png=True
            source.json         machine-readable provenance
            SOURCE.md           the same, readable
            cell.py             the notebook cell that drew it
            uncommitted.diff    only when the tree was dirty

    `name` is what the article refers to the figure by -- keep it stable, since
    the LaTeX side names the folder and the file.

    `facecolor="white"` or `transparent=True` drops the off-white notebook ground
    for a figure going onto a white page.

    `tight` trims the export to its ink. Convenient, but it means the file is no
    longer the width the figure was built at, so LaTeX rescales it -- and
    rescaling is what changes the text size. **A .pgf is always written at the
    exact figure size regardless of `tight`**: it is \\input unscaled, so its
    width has to be the width it claims. For the same reason, pass `tight=False`
    when the pdf is built at `ieee_figsize()` and placed at natural size.

    With `tight=False` nothing trims overflowing labels, so call
    `fig.tight_layout()` (or build with constrained layout) before saving.
    """
    base = FIGURE_DIR if subdir is None else FIGURE_DIR / subdir
    out_dir = base / name
    out_dir.mkdir(parents=True, exist_ok=True)

    formats = ["pdf"]
    if pgf:
        formats.append("pgf")
    if png:
        formats.append("png")
    formats += [f for f in extra_formats if f not in formats]

    if "pgf" in formats and not pgf_available():
        raise RuntimeError(
            f"pgf export needs {PGF_RCPARAMS['pgf.texsystem']!r} on PATH -- the backend "
            "runs LaTeX to measure the text. Install TeX (e.g. `brew install --cask "
            "basictex`, then `sudo tlmgr install type1cm cm-super underscore`), or set "
            "Figure_Export.PGF_RCPARAMS['pgf.texsystem'] to one you have. "
            "The pdf export needs no TeX and is unaffected.")

    # Turning trimming OFF cannot be done with a kwarg: savefig resolves
    # `bbox_inches=None` through `_val_or_rc` back to `savefig.bbox`, which
    # RCPARAMS sets to "tight". Only the rcParam itself switches it off.
    kwargs = {"dpi": dpi, "transparent": transparent, "pad_inches": 0.02}
    if facecolor is not None:
        kwargs["facecolor"] = facecolor
        kwargs["edgecolor"] = facecolor
    exact_bbox = {"savefig.bbox": None}

    from matplotlib import rc_context

    written = []
    for fmt in formats:
        path = out_dir / f"{name}.{fmt}"
        if fmt == "pgf":
            # Never trimmed: a .pgf is \input at its own size, so the file has
            # to be exactly the width the figure was built at. Trimming it would
            # leave the article scaling the figure to fit the column, which
            # rescales the text -- the one thing the pgf route exists to prevent.
            #
            # The pgf rcParams are scoped so text.usetex never leaks into the
            # inline preview, which would make every later draw in the session
            # depend on a TeX installation.
            with rc_context({**PGF_RCPARAMS, **exact_bbox}):
                fig.savefig(path, format="pgf", **kwargs)
        else:
            with rc_context({} if tight else exact_bbox):
                fig.savefig(path, format=fmt, **kwargs)
        written.append(path)

    _write_provenance(out_dir, name, fig, written, formats, dpi, note, tight)
    return written


def latex_figure(name, caption, label=None, subdir=None, fmt="pdf",
                 span=False, placement="!t"):
    """The LaTeX block for a figure `save_fig` just wrote.

    `fmt="pgf"` emits `\\input`, which is how a pgf figure is included -- it is
    LaTeX source, so it is never \\includegraphics'd and never scaled: it was
    built at the right width so its text matches the body text.

    No `\\footnotesize` wrapper: a .pgf carries an absolute `\\fontsize` on every
    text node, so a size command around the `\\input` does nothing. Set the size
    in matplotlib instead -- `ieee_style()` or `RCPARAMS_IEEE["font.size"]`.

    `span=True` uses `figure*`, the IEEEtran float that spans both columns.
    """
    stem = f"{name}/{name}" if subdir is None else f"{subdir}/{name}/{name}"
    label = label or f"fig:{name.replace('_', '-')}"
    env = "figure*" if span else "figure"
    body = (f"  \\input{{{stem}.pgf}}" if fmt == "pgf"
            else f"  \\includegraphics[width=\\{'textwidth' if span else 'columnwidth'}]{{{stem}}}")
    return (f"\\begin{{{env}}}[{placement}]\n"
            "  \\centering\n"
            f"{body}\n"
            f"  \\caption{{{caption}}}\n"
            f"  \\label{{{label}}}\n"
            f"\\end{{{env}}}")
