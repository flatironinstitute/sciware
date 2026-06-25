# uv demo: starting point

A tiny two-file "project" used as the live-demo starting point for the
uv/Pixi session. It deliberately has **no** `pyproject.toml` and **no**
environment — the presenter builds those up during the talk.

- `analyze.py` — the script you run. Note it imports `summarize` from
  `measurements`; the `import numpy` is hidden one level down in
  `measurements.py` (motivates pitfall #1: "you have to read every file to
  find the dependencies").
- `measurements.py` — uses `np.float_` and `np.NaN`, both **removed in
  NumPy 2.0**. So the script *runs on NumPy 1.x* but *crashes on NumPy 2.x*
  (motivates pitfall #2: nothing records that you need `numpy < 2`).

## What the presenter sees

```bash
# works on NumPy 1.x
$ python analyze.py
mean = 12.120, std = 0.256

# crashes on NumPy 2.x
$ python analyze.py
...
AttributeError: `np.float_` was removed in the NumPy 2.0 release. Use `np.float64` instead.
```

You can reproduce both quickly with uv. Use **Python 3.12** — it's the last
version with NumPy 1 wheels, so `numpy<2` installs from a prebuilt wheel
instead of triggering a slow source build (the trap to avoid in a live demo):

```bash
uv run --no-project --python 3.12 --with "numpy<2"  python analyze.py   # works
uv run --no-project --python 3.12 --with "numpy>=2" python analyze.py   # crashes
```

> On Python 3.13+, `pip install "numpy<2"` finds no wheel and compiles NumPy
> from source — minutes of waiting. So the live demo's venv must be 3.12.
