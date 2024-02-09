#include <iostream>
#include <sstream>

#include <nanobind/nanobind.h>
#include <nanobind/ndarray.h>
#include <nanobind/stl/string.h>

namespace nb = nanobind;

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
