# Making Your Software Project "Just Work"
## Project-centric environments and lockfiles with uv and Pixi


## Python projects have dependencies

- E.g. NumPy
- Today, we write those dependencies in a `pyproject.toml` file
  - (older methods include `setup.py`, `setup.cfg`, and `requirements.txt`)
- When you run your project, Python needs to be able to find those dependencies
- Where does it look? The virtual environment / venv (or `sys.path` in detail)


## How do we get packages into the venv?

- A frontend like pip, conda, uv, or pixi
- (Conda/Pixi can install more than just Python packages — we'll come back to that)


## Let's set up an environment the "traditional" way

- Start with some Python scripts importing NumPy
- No `pyproject.toml` or anything


## Traditional: central venv + pip install

- Create a venv: `python -m venv ~/venvs/research`
- Activate: `source ~/venvs/research/bin/activate`
- Install a package: `pip install numpy`
- Or similarly with conda:
  - `conda create -n myenv`, `conda activate myenv`, `conda install numpy`


## What can go wrong?

1. You have to inspect your scripts to figure out their dependencies
2. What if your script only works with NumPy 1? Can't tell from the imports
3. Reusing this environment for project B might break project A


## Solve (1) & (2) with a `pyproject.toml`

- Add `numpy < 2` to the deps
- Install the project in editable mode: reads `pyproject.toml`
- ...but we haven't solved (3)


## A 4th pitfall: the "wrong environment" problem

- Working on project A, activate A's venv
- Switch to project B in the same terminal, forget to activate B's venv → error!


## The fix: "project-centric environments"

- Solves (3) & (4)
- The venv is a property of the project
- Projects don't share venvs(*)
- (*) We'll see "workspaces" for consistent, multi-project envs though



# uv: a project-centric package manager


## Introducing uv

- `uv run script.py`: one command that
  - creates a venv,
  - ensures the dependencies are present, and
  - runs your code in the venv
- No manual activation → no chance to use the wrong env
- Automatically installs the local package in editable mode


## Other uv selling points

- Lightning-fast dependency resolution and installation
  - (see Charlie Marsh's talk for more)
- Single binary install (or two, if you count uvx)
- Great error messages and docs (`uv run --help`, `uv help run`)
- Developed openly, permissive licensing


## Tour of uv: two interfaces

- "Project interface" and "pip interface"


## Project interface

- `uv init`, `uv add`, `uv sync`, `uv run`
- `uv add` works with local packages (or use workspaces)
- Dev-only dependencies: `uv add --dev`
- ...and the generalization: groups (`uv add --group tests`)


## Lockfiles

- Make environments reproducible (and disposable!)
- Solve the problem of "NumPy 3 broke my code"
- When to commit lockfiles? Application = yes, library = no.


## pip interface

- `uv venv`, `uv pip install`
- More control, but more chance to make mistakes
- Don't need to activate the venv to install — do need to to run
- Can be a good option for projects that mix Python & compiled code
- uv venvs are fully pip-compatible and automatically git-ignored


## Python versions

- uv will download Python for you, or use a local version
  - (plays nice with modules)
- Manage with `uv python`, `.python-version`


## More uv bells and whistles

- `uvx`: run a package in an ephemeral, isolated environment
- `uv tool`: install global commands from packages
  - (disbatch, meson, pre-commit, py-spy, ruff)
- Manually create ephemeral envs: `uv run --with numpy,matplotlib`
- "Scrolls": standalone scripts with embedded deps (`uv add --script`)
  - Great for email, Slack, or gists
- Broad ecosystem support: dedicated GH Action, Docker distroless
- `uv_build` build backend, good for Python-only projects


## uv with notebooks

- Just need `ipykernel`
  - (can add to dev deps, or VS Code will install it)


## uv workspace

- A collection of packages with shared dependency resolution and a single venv
- Can replace the concept of a "base" environment
  - e.g. if you activate a conda env in your `.bashrc`, consider a workspace instead


## uv on the cluster

- `module load python uv`: tells uv to use the modules Python and put its cache in GPFS home
  - (doesn't mask the user's uv executable)
- Fast cached installs use hard links → cache and venv must be on the same filesystem
- uv ignores `--system-site-packages` in dependency resolution


## Future of uv

- One of the fastest-growing packages by GH stars
- Astral bought by OpenAI; plans for uv unclear. Still, uv could be forked.
- Still waiting on features like venv-in-cache (centralized venvs) for cluster users
- Team is active in next-gen Python packaging (WheelNext, PEP 817, 825)
- Leading wheel variant support (generalized platform tags), complex installs like PyTorch
- uv + pip + wheels growing more conda-like (build/package/distribute compiled deps, e.g. CUDA)
- First-class source installs are a clear advantage over conda for HPC / complex builds
  - Can still be a footgun



<!-- AI generated Pixi outline -->
# Pixi: project-centric environments for the conda world


## Introducing Pixi

- Same philosophy as uv (per-project env, lockfile, `pixi run`)
  - but pulls from conda channels (conda-forge) instead of PyPI
- Why you'd reach for it: dependencies that aren't just Python packages
  - Compilers, MPI, CUDA toolkit, R, system libraries
  - things conda packages and pip/uv generally don't


## Quick tour

- `pixi init`, `pixi add numpy`, `pixi run python script.py`
- Config lives in `pyproject.toml` or `pixi.toml`; lockfile is `pixi.lock`
- Can mix conda and PyPI deps in one project (`pixi add --pypi <pkg>`)
- Multiple named environments per project (e.g. `default`, `gpu`, `test`)


## Pixi vs. conda

- A modern, fast frontend to the same conda ecosystem
  - (like uv is to PyPI)
- Project-centric and lockfile-based, instead of central named envs you activate
- `pixi global` for user-wide tools (cf. conda base / `uv tool`)


## uv or Pixi?

- Pure-Python / PyPI stack → uv
- Need non-Python deps from conda-forge → Pixi
- Same mental model either way, so the switch is cheap
