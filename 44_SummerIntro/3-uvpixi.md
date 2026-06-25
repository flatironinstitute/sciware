# Making Your Software Project "Just Work"
## Project environments and lockfiles with uv and Pixi

https://sciware.flatironinstitute.org/44_SummerIntro/day3.html

<style>
.reveal ul, .reveal ol { display: block; }.reveal pre.term { background:#1e1e1e; color:#d4d4d4; width:fit-content; max-width:94%; margin:14px auto; padding:12px 16px; text-align:left; font-size:0.58em; line-height:1.5; border-radius:8px; }
.reveal pre.term .pa { color:#3fc7e0; }
.reveal pre.term .dl { color:#808080; }
.reveal pre.term .nm { color:#ffffff; font-weight:bold; }
.reveal pre.term .pr { color:#6a9955; }
</style>


## We start with a couple of Python scripts

- A small analysis, split across two files. No `pyproject.toml`, no environment — yet.

```text
uv-demo/
├── analyze.py        # the script we run
└── measurements.py   # helper functions it imports
```

```python
# analyze.py
from measurements import summarize

values = [12.3, 11.8, -999.0, 12.1, 12.5, -999.0, 11.9]
mean, std = summarize(values)
print(f"mean = {mean:.3f}, std = {std:.3f}")
```

- **Goal:** run this on a machine that doesn't have its dependencies yet


## Python projects have dependencies

- `analyze.py` → `measurements.py` → `import numpy`
- Today we *declare* dependencies in a `pyproject.toml`
  - older methods: `setup.py`, `setup.cfg`, `requirements.txt`
- To run the project, Python has to *find* those dependencies at import time
- Where does it look? In a **virtual environment** ("venv")
  - in gory detail: a list of directories on `sys.path`


## How do packages get into the venv?

- You put them there with a **frontend**: `pip`, `conda`, `uv`, or `pixi`
- The frontend resolves the dependency graph and installs packages into the venv
- `conda` / `pixi` can install more than *Python* packages — we'll come back to that


## A "traditional" way: one central venv + pip

```bash
python3.12 -m venv ~/venvs/research    # create a venv — Python 3.12 (why: next slides)
source ~/venvs/research/bin/activate   # activate it
pip install numpy                      # install into it
python analyze.py                      # run
```

- Or the `conda` equivalent: `conda create -n research`, `conda activate research`, `conda install numpy`. Still centralized.
- We `pip install numpy` → we get the *latest* NumPy (2.x). Then:

```text
  File "measurements.py", line 11, in clean
    arr = np.asarray(values, dtype=np.float_)
AttributeError: `np.float_` was removed in the NumPy 2.0 release. Use `np.float64` instead.
```

#note: Demo live: create the venv, activate, `pip install numpy`, run, and let it crash — the traceback is the hook for the next slide. Use **Python 3.12**: it's the last version with NumPy 1 wheels, so when we pin `numpy < 2` in a moment, the install stays fast (from a wheel). On 3.13+, pip finds no wheel and compiles NumPy from source — minutes of dead air in front of the room. Make sure `python3.12` is on your PATH first (e.g. `uv python install 3.12`, pyenv, or a module).


## What can go wrong?

1. **Hidden dependencies** — nothing announced that this project needs NumPy; you have to read *every* file (the `import numpy` is down in `measurements.py`, not `analyze.py`)
2. **No version constraints** — `pip install numpy` grabbed NumPy 2, but the code needs NumPy 1. Nothing recorded that requirement.
3. **One env, many projects** — reuse `~/venvs/research` for project B, upgrade a package, and you can silently break project A


## Fix (1) & (2): a `pyproject.toml`

```toml
[project]
name = "research"
version = "0.1"
dependencies = ["numpy < 2"]
```

- Dependencies now live *with the code* — discoverable, and with a version constraint
- Install the project itself in **editable mode**; pip reads `pyproject.toml`:

```bash
pip install -e .
```

- ⚠️ An old dependency can constrain your *Python*: NumPy 1's last wheels are for **Python 3.12** — use 3.12 or earlier, or pip compiles NumPy from source on 3.13+ (`uv` automates this for us later)
- ✅ (1) deps discoverable &nbsp; ✅ (2) version pinned &nbsp; ❌ (3) still one shared env


## A 4th pitfall: the "wrong-environment" problem

```bash
# yesterday — set up and ran project A
cd ~/projA
source .venv/bin/activate     # activate A's environment
python train.py               # ✓ runs with A's packages

# today — same terminal still open; switch to project B
cd ~/projB
python analyze.py             # ✗ still in A's venv!
#   ModuleNotFoundError: No module named 'pandas'
#   ...or worse: it runs, but with the wrong versions → subtly wrong results
```

- Manual activation is a step you can always forget
- Pitfalls (3) & (4) share one root cause: **shared, manually-managed environments**



# Project-centric environments
## A conceptual framework for projects that "just work"


## A venv per project

<style>
.pce { display:flex; gap:56px; justify-content:center; align-items:flex-start; margin:6px 0 4px; }
.pce-col { flex:0 1 430px; }
.pce-col h3 { text-align:center; margin:0 0 14px; font-size:0.9em; }
.pce-chips { display:flex; gap:10px; justify-content:center; }
.pce-chip { border:2px solid #537eba; border-radius:8px; padding:6px 10px; font-weight:bold; font-size:0.72em; }
.pce-stack { display:flex; flex-direction:column; align-items:center; gap:5px; }
.pce-down { color:#537eba; font-size:1.2em; line-height:1; }
.pce-shared { border:2px dashed #537eba; border-radius:8px; padding:12px; text-align:center; font-weight:bold; font-size:0.74em; margin-top:6px; }
.pce-card { border:2px solid #537eba; border-radius:8px; padding:8px; text-align:center; }
.pce-card .lbl { font-weight:bold; font-size:0.72em; margin-bottom:6px; }
.pce-venv { border:2px dashed #537eba; border-radius:6px; padding:5px; font-size:0.66em; font-family:monospace; }
.pce-note { text-align:center; margin-top:12px; font-size:0.72em; }
.pce-bad { color:#c0392b; }
.pce-good { color:#2e7d32; }
</style>

<div class="pce">
  <div class="pce-col">
    <h3>Traditional: one central venv</h3>
    <div class="pce-chips">
      <div class="pce-stack"><span class="pce-chip">Project A</span><span class="pce-down">↓</span></div>
      <div class="pce-stack"><span class="pce-chip">Project B</span><span class="pce-down">↓</span></div>
      <div class="pce-stack"><span class="pce-chip">Project C</span><span class="pce-down">↓</span></div>
    </div>
    <div class="pce-shared">one shared venv<br>~/venvs/research</div>
    <p class="pce-note pce-bad">⚠ upgrade a package for B → silently break A</p>
  </div>
  <div class="pce-col">
    <h3>Project-centric: a venv per project</h3>
    <div class="pce-chips">
      <div class="pce-card"><div class="lbl">Project A</div><div class="pce-venv">.venv</div></div>
      <div class="pce-card"><div class="lbl">Project B</div><div class="pce-venv">.venv</div></div>
      <div class="pce-card"><div class="lbl">Project C</div><div class="pce-venv">.venv</div></div>
    </div>
    <p class="pce-note pce-good">✓ the venv is a property of the project</p>
  </div>
</div>

- The venv lives *beside* the code (a `.venv/` in the project), so projects can't interfere → fixes **(3)** and **(4)**
- Reproducible & **disposable**: delete `.venv`, recreate it from scratch anytime
- (*) Need a consistent env across several projects? → **workspaces** (later)


## The ecosystem of Python package managers

<style>
.eco { display:grid; grid-template-columns:auto 1fr 1fr; gap:10px; max-width:740px; margin:18px auto 0; }
.eco > div { padding:14px; border-radius:8px; text-align:center; }
.eco .hd { font-weight:bold; background:#eef2f8; color:#2c3e50; }
.eco .hd span { font-weight:normal; font-size:0.78em; }
.eco .rh { font-weight:bold; background:#eef2f8; color:#2c3e50; display:flex; flex-direction:column; align-items:center; justify-content:center; }
.eco .rh .sub { font-weight:normal; font-size:0.78em; }
.eco .cell { border:2px solid #537eba; font-family:monospace; font-size:1.05em; display:flex; align-items:center; justify-content:center; }
.eco .focus { background:#537eba; color:#fff; }
.eco .corner { background:transparent; }
.eco-note { text-align:center; font-size:0.78em; margin-top:16px; }
</style>

<div class="eco">
  <div class="corner"></div>
  <div class="hd">PyPI<br><span>(pip wheels / sdists)</span></div>
  <div class="hd">conda-forge<br><span>(conda packages)</span></div>

  <div class="rh"><span>Traditional</span><span class="sub">central envs</span></div>
  <div class="cell">pip + venv</div>
  <div class="cell">conda</div>

  <div class="rh"><span>Project-centric</span><span class="sub">lockfiles</span></div>
  <div class="cell focus">uv</div>
  <div class="cell">pixi</div>
</div>

<p class="eco-note"><b>uv</b> is to <b>pip</b> what <b>pixi</b> is to <b>conda</b>: a fast, modern, project-centric frontend.<br>Today: mostly <b>uv</b>, with a look at <b>pixi</b> at the end.</p>


# uv: a project-centric package manager


## Introducing uv

- `uv run script.py`: one command that
  - creates a venv (`uv venv`),
  - solves the dependency graph (`uv lock`)
  - ensures the dependencies are present (`uv sync`), and
  - runs your code in the venv
- No manual activation → no chance to use the wrong env
- Automatically installs the local package in editable mode


## Installing uv

- Follow the official docs at <https://docs.astral.sh/uv/>:

<pre style="width:fit-content;margin:20px auto;"><code class="language-bash">curl -LsSf https://astral.sh/uv/install.sh | sh</code></pre>

- **Minimally invasive:** a single self-contained binary
  - no admin rights, doesn't touch your system Python
  - no `conda`-style activation block in your `.bashrc` — only a `PATH` entry
  - on the FI clusters, there's also a module: `module load uv` (more later)
- Want to follow along today? Install it now.


## Other uv selling points

- Lightning-fast dependency resolution and installation
  - (see [Charlie Marsh's talk](https://www.youtube.com/watch?v=gSKTfG1GXYQ) for more)
- Great error messages and docs (`uv run --help`, `uv help run`)
- Developed openly, permissive licensing (dual MIT / Apache-2)
- Wide adoption (see next slide)


## Adoption

<img src="assets/star-history-2026625.png" alt="GitHub star history: uv climbing near-vertically since 2024, alongside poetry, jax, pytorch, pixi, and conda" style="height:540px; border:none; box-shadow:none;">

<p style="font-size:0.7em; color:#888; margin-top:0.2em;">Stars ≈ developer mindshare, not usage, but still one of the steepest star trajectories ever on GitHub.</p>


## Tour of uv: two interfaces

uv gives you two ways to work — pick one per project:

<style>
.iface { display:flex; gap:40px; justify-content:center; margin-top:16px; }
.iface-col { flex:0 1 410px; border:2px solid #537eba; border-radius:10px; padding:14px 20px; }
.iface-col.focus { background:#eef4fb; box-shadow:0 0 0 3px #537eba inset; }
.iface-col h3 { margin:0 0 2px; font-size:0.95em; }
.iface-col .badge { font-size:0.58em; background:#537eba; color:#fff; border-radius:4px; padding:2px 7px; vertical-align:middle; margin-left:8px; }
.iface-tag { font-size:0.72em; color:#777; margin:0 0 10px; line-height:1.9; }
.iface-tag code { padding:1px 5px; }
.iface-cmds { font-family:monospace; font-size:0.72em; line-height:1.9; }
.iface-cmds code { background:#f3f3f3; border-radius:4px; padding:1px 6px; white-space:nowrap; display:inline-block; }
.iface-use { font-size:0.72em; margin-top:10px; }
</style>

<div class="iface">
  <div class="iface-col focus">
    <h3>Project interface<span class="badge">default</span></h3>
    <p class="iface-tag">uv manages your <code>pyproject.toml</code>, <code>uv.lock</code> &amp; <code>.venv</code></p>
    <div class="iface-cmds"><code>uv init</code> <code>uv add</code> <code>uv lock</code> <code>uv sync</code> <code>uv run</code></div>
    <p class="iface-use"><b>Use for:</b> almost everything</p>
  </div>
  <div class="iface-col">
    <h3>pip interface</h3>
    <p class="iface-tag">you manage the venv yourself (familiar <code>pip</code> muscle memory)</p>
    <div class="iface-cmds"><code>uv venv</code> &nbsp; <code>uv pip install</code></div>
    <p class="iface-use"><b>Use for:</b> fine control, temporary edits to venv</p>
  </div>
</div>


## Project interface

Our project already has a `pyproject.toml`. The whole venv dance becomes:

```bash
uv add "numpy<2"      # record the dep → updates pyproject.toml + uv.lock
uv run analyze.py     # build the env to match, then run — no activation
```

```text
Creating virtual environment at: .venv
 + numpy==1.26.4
mean = 12.120, std = 0.256
```

<style>
.life { display:flex; align-items:center; justify-content:center; flex-wrap:wrap; gap:7px; margin:8px 0 2px; font-family:monospace; font-size:0.72em; }
.life .pill { border:2px solid #537eba; border-radius:7px; padding:5px 9px; }
.life .pill.focus { background:#537eba; color:#fff; }
.life .arr { color:#537eba; }
.life .grp { display:inline-flex; align-items:center; gap:7px; border:2px dashed #537eba; border-radius:9px; padding:6px 8px; background:#eef4fb; }
.life-cap { text-align:center; font-size:0.72em; color:#537eba; margin-top:6px; }
</style>

<div class="life">
  <span class="pill">uv init</span><span class="arr">→</span>
  <span class="pill">uv add</span><span class="arr">→</span>
  <span class="grp"><span class="pill">uv lock</span><span class="arr">→</span><span class="pill">uv sync</span></span>
  <span class="arr">→</span>
  <span class="pill focus">uv run</span>
</div>
<p class="life-cap"><code>uv run</code> does the boxed steps for you — so the env always matches the lockfile</p>

- No manual venv, no activation → the wrong-env pitfall is gone, and the env can't drift


## Dependency groups & extras

The same `uv add` commands write to different tables in `pyproject.toml`:

```toml
[project]
dependencies = ["numpy"]          # uv add numpy

[dependency-groups]               # dev-side — not shipped to users
dev  = ["pytest"]                 # uv add --dev pytest
docs = ["sphinx"]                 # uv add --group docs sphinx

[project.optional-dependencies]   # extras — users opt in
plot = ["matplotlib"]             # uv add --optional plot matplotlib
```

- **Groups** = *developer*-side (tests, docs); never published with your package
- **Extras** = optional features your *users* choose: `pip install research[plot]`


## Lockfiles

- Pins every package's exact version + hash → a **reproducible**, **disposable** env (delete `.venv`, `uv sync` rebuilds it)
  - skips the **"should I add an upper bound?"** debate: prefer **lower bounds only** (`numpy>=1.26`) + the lockfile of known-good versions — speculative caps like `numpy<2` propagate downstream and cause conflicts
  - imperfect for **libraries**, which usually don't ship a lockfile
- Technically human-readable TOML — but generated & maintained by **tooling** (`uv lock`, `uv sync`); you rarely read or edit it yourself

```toml
# uv.lock — generated; read & written by tooling, not by hand
version = 1
requires-python = ">=3.12"
[[package]]
name = "numpy"
version = "1.26.4"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "…/numpy-1.26.4-cp312-…x86_64.whl", hash = "sha256:675d61ff…" },
    # … one pinned wheel per OS / arch / Python …
]
```


## uv pip interface

```bash
uv venv                       # create a .venv (no project files needed)
uv pip install numpy          # install into it, pip-style
uv run --no-sync analyze.py   # run without re-syncing from the lockfile
```

- More control, but more chances to slip up — doesn't use the lockfile
- No need to activate to install; you *do* to run `python` directly (or just use `uv run --no-sync`)
- Can be useful for projects that mix Python with compiled code (easy way to force rebuild)
- uv venvs are ordinary, PEP-standardized venvs: pip-compatible, project-interface-compatible, auto git-ignored
  - Contrast with conda/Pixi, which lock you into specific (albeit open source) tooling


## Python versions

- uv will download Python for you, or use a local version
  - plays nice with cluster modules
- Pin a version per-project in a `.python-version` file (`uv python pin 3.12`) — a lockfile for your Python
- `requires-python` in `pyproject.toml` declares the *range* your code supports — not an exact pin (don't upper-bound it!)
- **Back to our demo:** `numpy < 2` needed Python ≤ 3.12 — pin `3.12` and uv fetches it for you. No manual `python3.12`, no surprise source build.

<pre class="term"><span class="pr">❯</span> uv python list
cpython-3.14.3-linux-x86_64-gnu     <span class="dl">&lt;download available&gt;</span>
cpython-3.13.12-linux-x86_64-gnu    <span class="pa">~/.local/share/uv/python/…/python3.13</span>
cpython-3.12.13-linux-x86_64-gnu    <span class="pa">~/.local/share/uv/python/…/python3.12</span>
cpython-3.11.13-linux-x86_64-gnu    <span class="pa">/usr/bin/python3.11</span>
cpython-3.10.20-linux-x86_64-gnu    <span class="dl">&lt;download available&gt;</span></pre>


## Running tools, not just projects

- A "tool" is a Python project with an executable module (e.g. `python -m ruff`)
- uv has first-class support for tools (`uv tool`, `uvx`)
- `uvx ruff check` — run a tool in a throwaway env (like `pipx run`)
  - Exactly equivalent to `uv tool run`
- `uv tool install ruff` — install a CLI globally, isolated from your projects
  - handy for `ruff`, `pre-commit`, `py-spy`, `meson`, even `disbatch`

<pre class="term"><span class="pr">❯</span> uv tool list
<span class="nm">ruff v0.15.12</span>
- ruff
<span class="nm">py-spy v0.4.1</span>
- py-spy
<span class="nm">disbatch v3.1.dev39</span>
- disBatch
- disbatch</pre>


## Ephemeral envs → "scrolls"

Need a package for a *single* run? Make a throwaway env with `--with`:

```bash
uv run --with matplotlib plot.py   # temporary env, just this once
```

Run it often? **Bake the deps into the script** — a "scroll" (PEP 723):

```python
# /// script
# requires-python = ">=3.11"
# dependencies = ["matplotlib", "numpy"]
# ///
import matplotlib.pyplot as plt
```

- `uv run plot.py` reads the embedded metadata, builds the env, and runs — no `--with`, no `pyproject.toml`
- The `# /// script` block is **PEP 723** — a Python standard, not uv-specific (pipx and hatch read it too)
- Perfect for emailing/Slacking/gisting a one-file tool; add deps with `uv add --script plot.py numpy`

<!-- niche/advanced — kept for reference, not shown
## Ecosystem & build backend

- **Ecosystem**: official GitHub Action, distroless Docker images
- **`uv_build`**: fast, minimal build backend for pure-Python packages
-->


## uv with notebooks

- Run Jupyter from your project's environment:

```bash
uv add --dev ipykernel              # makes the project env available as a kernel
uv run --with jupyter jupyter lab   # launch Jupyter (nice on a laptop)
```

- In VS Code, just select `.venv` as the kernel — it'll offer to install `ipykernel` for you


## uv workspace (advanced)

- One repo, several packages → **shared resolution and a single `.venv`**
- List members in `[tool.uv.workspace]` in the top-level `pyproject.toml`
- Can replace the idea of a **"base" environment**:
  - if you reflexively activate a conda env in your `.bashrc`, a workspace is often the better fit
- Members resolve together → no version skew between your own projects


## uv on the FI clusters

- `module load python uv` — module Python + uv's cache on your GPFS home (doesn't shadow your own uv)
- Fast installs **hard-link** from the cache → cache and `.venv` must share a filesystem. Seeing this?

```text
warning: Failed to hardlink files; falling back to full copy.
         …cache and target directories are on different filesystems…
```

- **Fix:** `module load uv` (puts the cache beside your venvs) — or silence with `UV_LINK_MODE=copy` (copies are slower)
- The cache is **many small files** → run `uv cache prune` occasionally to stay under your GPFS **inode quota**
- uv ignores `--system-site-packages` during resolution · see the cluster wiki for setup


## Future of uv

- Among the fastest-growing dev tools by GitHub stars
- Astral was acquired by OpenAI; development seems to be carrying on as normal — but the future of AI companies is impossible to predict (uv is permissively licensed and could be forked)
- **Centralized venvs** (venv-in-cache) are landing — a big win for cluster users
- The uv team plays a **leading role** in the next generation of wheels:
  - **WheelNext** — first-class **compiled / non-Python dependencies** in wheels (conda's old advantage)
  - **Wheel Variants** (PEPs 817 & 825) — auto-pick the **optimal build for your machine**, e.g. the right GPU/CUDA wheel (think PyTorch)
- uv + wheels growing more conda-like: build, package & distribute compiled deps (e.g. CUDA)
- First-class **source installs** — an edge over conda for HPC / complex builds (still a footgun; Pixi is moving toward first-class source installs too)



# Pixi: project-centric environments for the conda world


## Introducing Pixi

- Same idea as uv — per-project env, lockfile, `pixi run` — but it pulls from **conda channels** (conda-forge), not PyPI
- Reach for it when your dependencies aren't just Python packages:
  - compilers, MPI, CUDA toolkit, R, system libraries — things pip/uv generally can't install


## Quick tour

```bash
pixi init research
pixi add numpy "scipy>=1.13"  # conda-forge deps → pixi.toml + pixi.lock
pixi add --pypi <pkg>         # mix in a PyPI-only package
pixi run python analyze.py    # run in the project env — no activation
```

- Config in `pixi.toml`, or `[tool.pixi]` in `pyproject.toml`; lockfile is `pixi.lock` (multi-platform)
- Several named environments per project — e.g. `default`, `gpu`, `test`
- `pixi shell` activates an env interactively, like `conda activate` but per-project


## Pixi vs. conda

- A fast, modern frontend to the **same conda-forge ecosystem** — Pixi is to conda what uv is to PyPI
- Fixes conda's *workflow* pain:
  - project-centric + lockfile, instead of central named envs you manually activate
  - no `conda init` block bloating your `.bashrc` — it just adds `pixi` to your `PATH`
- `pixi global` installs user-wide tools — cf. conda's base env or `uv tool`
- Inherits conda's *ecosystem* caveat: conda-forge binaries aren't ABI-compatible with the cluster **modules** — don't mix the two


## uv or Pixi?

- Pure-Python / PyPI stack → **uv**
- Need non-Python deps from conda-forge (compilers, CUDA, R, …) → **Pixi**
- Same project-centric mental model either way, so switching is cheap
