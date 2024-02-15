# Sciware

https://sciware.flatironinstitute.org/30_CCQ

https://github.com/flatironinstitute/sciware/tree/main/30_CCQ
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
## nanobind project layout
A simple nanobind project has the following files:
```
nanobind-example/
├── CMakeLists.txt
├── pyproject.toml
└── src
    └── example_pkg
        ├── compute.py
        ├── array_example_module.cpp
        └── __init__.py
```
---
## nanobind `array_example_module.cpp`
```c++
template <typename Scalar>
void double_arr(
    nb::ndarray<Scalar, nb::ndim<1>, nb::device::cpu> outarr,
    nb::ndarray<const Scalar, nb::ndim<1>, nb::device::cpu> inarr) {

    auto out_view = outarr.view();
    auto in_view = inarr.view();

    for (size_t i = 0; i < in_view.shape(0); i++) {
        out_view(i) = in_view(i) * 2;
    }
}

NB_MODULE(array_example_module, m) {
    m.def("double_arr", &double_arr<float>);
    m.def("double_arr", &double_arr<double>);
}
```
---
## nanobind `compute.py`
```python
from . import array_example_module

inarr = np.arange(20)
outarr = np.empty_like(inarr)

array_example_module.double_arr(outarr, inarr)
```

- Easy! nanobind will check that the array types have the expected shape, dtype, strides, etc.
- A more sophisticated example would have nanobind returning a NumPy array
- Now we'll look at how `array_example_module.cpp` gets built
---
## nanobind `CMakeLists.txt`
```cmake
cmake_minimum_required(VERSION 3.15...3.27)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

find_package(Python 3.8 COMPONENTS Interpreter Development.Module REQUIRED)
find_package(nanobind CONFIG REQUIRED)

nanobind_add_module(array_example_module src/example_pkg/array_example_module.cpp)

install(TARGETS array_example_module LIBRARY DESTINATION example_pkg)
```
---
## nanobind `pyproject.toml`
```toml
[build-system]
requires = ["scikit-build-core >= 0.5", "nanobind"]
build-backend = "scikit_build_core.build"

[project]
name = "example_pkg"
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
- That's it! scikit-build-core, nanobind, cmake, and ninja will all be downloaded and installed automatically as needed
- With automatic rebuilds:
```console
$ pip install scikit-build-core nanobind ninja
$ pip install -e . --no-build-isolation
```
- Automatic rebuilds: C++ code is recompiled *at import time* (see demo)
---
## nanobind

### Live demo
*including automatic rebuilds*
---
## nanobind struct
- Can get complicated and verbose with custom types
<div class="two-column">
    <div class="grid-item">

```c++
struct S {
  int i;
  S(int i):i{i}{}
  int m() const { return i+2;}
};

// A function using S
int f(S const & s){ return s.i;}

// make S printable in C++
std::ostream & operator<<(std::ostream &out, S const & s) {
     return out << "S struct with i=" << s.i << '\n';
}
```

    </div>
    <div class="grid-item">

```c++
NB_MODULE(struct_example_module, m) {
    nb::class_<S>(m, "S")
        .def_rw("i", &S::i)
        .def(nb::init<int>())
        .def("m", &S::m)
        .def("__repr__", [](const S& s) {
          std::stringstream stream;
          stream << s;
          return stream.str();
        });
    m.def("f", &f);
}
```

    </div>
</div>
---
## nanobind summary
- nanobind makes it easy to define robust bindings between C++ and Python
- Flexible and powerful, but verbose (terse on the Python side, however)
- Native NumPy-awareness makes it a good option for array processing
- Combined with scikit-build-core, is a very powerful way to distribute compiled components in a Python package
- We've only scratched the surface; can deal with custom C++ types, GPU arrays, ownership/lifetime management, etc.
---
# Python ctypes

Calling C from Python
[https://docs.python.org/3/library/ctypes.html](https://docs.python.org/3/library/ctypes.html)
---
## Python ctypes
- [ctypes](https://docs.python.org/3/library/ctypes.html) is part of the Python standard library
- Lets you load a shared object, call functions, access variables, etc.
- Responsibility falls on the user to compile the shared object and call the functions with the correct signature
- *Very* easy to get this wrong and cause the Python interpreter to crash!
---
## Python ctypes
- ctypes doesn't help you compile your code into a shared library, but assume we've figured that out (maybe with setuptools, a Makefile, or CMake)
- Load the a shared object in Python using ctypes:

```python
import ctypes
lib = ctypes.CDLL('./example.so')
# void double_arr(size_t n, double *outarr, double const * inarr)
lib.double_arr.argtypes = [ctypes.c_size_t,
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double),
                          ]
lib.double_arr.restype = None
```
---
## Python ctypes
- Call the function (finally!):
```python
lib.double_arr(len(inarr),
            outarr.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            inarr.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            )
```
---
## Python ctypes
- What happens if we swap the order of the C arguments but forget to update our Python?
```c
void double_arr(size_t n, double *outarr, double const *inarr)  // old
void double_arr(double *outarr, double const *inarr, size_t n)  // new
```

```console
$ python script.py
Segmentation fault (core dumped)
```
---
## Python ctypes
- Verbose and fragile—relies on the user to keep Python definitions in sync with C function signatures
- The tooling for compiling shared objects for ctypes is older and less portable
- On the other hand, ctypes is built-in to the Python standard library
- Universal, in the sense that it only deals with the platform's C ABI
- Usually better to use C++ and nanobind for scientific computing
---
## SciWare Survey

<center>
<img width="50%" src="./qr.png">
</center>
