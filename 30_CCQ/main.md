# Sciware

https://sciware.flatironinstitute.org/30_CCA

https://github.com/flatironinstitute/sciware/tree/main/30_CCA

---

## Rules of Engagement

### Goal:

Activities where participants all actively work to foster an environment which encourages participation across experience levels, coding language fluency, *technology choices*\*, and scientific disciplines.

<small>\*though sometimes we try to expand your options</small>

---

## Rules of Engagement

- Avoid discussions between a few people on a narrow topic
- Provide time for people who haven't spoken to speak/ask questions
- Provide time for experts to share wisdom and discuss
- Work together to make discussions accessible to novices

<small>
(These will always be a work in progress and will be updated, clarified, or expanded as needed.)
</small>

---

## Center-hosted Sciware

- Sciware will rotate between centers each month
   - focus on topics of interest to centers
   - include voices from all centers
   - each center will host twice a year
   - open to all
- Suggest topics or contribute to content in #sciware Slack
- We are recording. Link will be posted to [https://sciware.flatironinstitute.org/](https://sciware.flatironinstitute.org/)

---

## Today's Agenda

- Intro to inter-language operability
- Julia <-> Python, Julia <-> C
- Python <-> C/C++

---

# Python ctypes

Calling C from Python
https://docs.python.org/3/library/ctypes.html

---

## Python ctypes
- [ctypes](https://docs.python.org/3/library/ctypes.html) is part of the Python standard library
- Lets you load a shared object, call functions, access variables, etc.
- Responsibility falls on the user to compile the shared object and call the functions with the correct signature
- *Very* easy to get this wrong and cause the Python interpreter to crash!

---

## Python ctypes
```c
void compute_pair_dist(const size_t nbin, uint64_t *dist, const size_t npart, const double *pos2d) {
    /* Compute all pair-wise distances between the points in `pos2d`
     * and store the histogram of distances in `dist`.
     */

    for (size_t i = 0; i < npart; i++) {
        for (size_t j = i + 1; j < npart; j++) {
            double dx = pos2d[i * 2] - pos2d[j * 2];
            double dy = pos2d[i * 2 + 1] - pos2d[j * 2 + 1];
            double r = sqrt(dx * dx + dy * dy);
            size_t k = (size_t) (r * nbin);
            if (k < nbin) {
                dist[k]++;
            }
        }
    }
}
```

---

## Python ctypes
1. Compile the C code into a shared object (user is responsible for this, perhaps using a Makefile or CMake):

```console
gcc -fPIC -c -o example.o example.c
gcc -fPIC -shared -o example.so example.o
```

2. Load the shared object in Python using ctypes:

```python
import ctypes
lib = ctypes.CDLL('./example.so')
```

---

## Python ctypes
3. Set up the arguments and the return types:

```python
compute_pair_dist = lib.compute_pair_dist
# void compute_pair_dist(const size_t nbin, size_t *dist, const size_t npart, const double *pos2d)
compute_pair_dist.argtypes = [ctypes.c_size_t,
                              ctypes.POINTER(ctypes.c_size_t),
                              ctypes.c_size_t,
                              ctypes.POINTER(ctypes.c_double),
                              ]
compute_pair_dist.restype = None
```

---

## Python ctypes

4. Call the function (finally!):
```python
compute_pair_dist(nbin,
                  dist.ctypes.data_as(ctypes.POINTER(ctypes.c_size_t)),
                  n,
                  pos2d.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                  )
```

---

## Python ctypes

### Live demo

---

## Python ctypes
- By default, Python knows nothing about the arguments and return types of our functions, or how to compile code into a load-able library
- Verbose and fragile—relies on the user to keep Python definitions in sync with C function signatures
- Portable path resolution to the built library can be challenging
- Limited support for languages beyond C
- Often hidden assumptions about contiguity of arrays
- These are some of the problems that more sophisticated libraries, like pybind11 and clair, solve
- On the other hand, ctypes is built-in to the Python standard library
- Universal, in the sense that it only deals with the platform's C ABI

---

# nanobind

Calling C++ from Python
https://github.com/wjakob/nanobind

---

## nanobind
- Library to create Python bindings to C++ code (and vice versa)
- Successor to pybind11: near-identical syntax (same creator) but produces more efficient code
- Works with C++17 and newer (can use pybind11 for C++11)
- Seamless integration with modern Python build backends
- NumPy-aware

---

## nanobind `examplemod.cpp`
```c++
template <typename Scalar>
void compute_pair_dist(nb::ndarray<uint64_t, nb::shape<nb::any>, nb::c_contig, nb::device::cpu> dist,
                       nb::ndarray<const Scalar, nb::shape<nb::any, 2>, nb::c_contig, nb::device::cpu> pos2d) {

    auto dist_view = dist.view();
    auto pos2d_view = pos2d.view();

    for (size_t i = 0; i < pos2d_view.shape(0); i++) {
        for (size_t j = i + 1; j < pos2d_view.shape(0); j++) {
            Scalar dx = pos2d_view(i, 0) - pos2d_view(j, 0);
            Scalar dy = pos2d_view(i, 1) - pos2d_view(j, 1);
            Scalar r = sqrt(dx * dx + dy * dy);
            size_t k = (size_t) (r * dist_view.shape(0));
            if (k < dist_view.shape(0)) {
                dist_view(k)++;
            }
        }
    }
}
```

---

## nanobind `CMakeLists.txt`
```cmake
cmake_minimum_required(VERSION 3.15...3.27)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

find_package(Python 3.8 COMPONENTS Interpreter Development.Module REQUIRED)
find_package(nanobind CONFIG REQUIRED)

nanobind_add_module(examplemod src/examplepkg/examplemod.cpp)

install(TARGETS examplemod LIBRARY DESTINATION examplepkg)
```

---

## nanobind `pyproject.toml`
```toml
[build-system]
requires = ["scikit-build-core >= 0.5", "nanobind"]
build-backend = "scikit_build_core.build"

[project]
name = "examplepkg"
version = "0.0.1"
requires-python = ">=3.8"

[tool.scikit-build]
minimum-version = "0.5"
build-dir = "build/{wheel_tag}"
editable.rebuild = true
```

---

## nanobind build & install
- Build and install:
```console
$ pip install .
```

- With automatic rebuilds:
```console
$ pip install scikit-build-core nanobind ninja
$ pip install -e . --no-build-isolation
```

---

## nanobind python
```python
from . import examplemod
examplemod.compute_pair_dist(dist, pos2d)
```

- Easy! nanobind will check that the array types have the expected shape, dtype, strides, etc.

---

## nanobind

### Live demo

---

## nanobind summary
- nanobind makes it easy to define robust bindings between C++ and Python
- Flexible and powerful, but verbose (terse on the Python side, however)
- Native NumPy-awareness makes it a good option for array processing
- Combined with scikit-build-core, is a very powerful way to distribute compiled components in a Python package
- We've only scratched the surface; can deal with custom C++ types, GPU arrays, ownership/lifetime management, etc.
