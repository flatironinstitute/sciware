# nanobind-example

Creates Python bindings for a C++ module using [nanobind](https://github.com/wjakob/nanobind)

## Build and install (basic)
```console
$ pip install .
```

## Build and install (editable)
```console
$ pip install scikit-build-core nanobind ninja
$ pip install -e . --no-build-isolation
```

## Test
```
$ python -m example_pkg.compute
```
