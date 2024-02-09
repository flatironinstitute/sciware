#include <nanobind/nanobind.h>
#include <nanobind/ndarray.h>

namespace nb = nanobind;

template <typename Scalar>
void double_arr(nb::ndarray<Scalar, nb::ndim<1>, nb::device::cpu> outarr,
            nb::ndarray<const Scalar, nb::ndim<1>, nb::device::cpu> inarr) {

    auto out_view = outarr.view();
    auto in_view = inarr.view();

    for (size_t i = 0; i < in_view.shape(0); i++) {
        out_view(i) = 2 * in_view(i);
    }
}

NB_MODULE(array_example_module, m) {
    m.def("double_arr", &double_arr<float>);
    m.def("double_arr", &double_arr<double>);
    m.def("double_arr", &double_arr<int64_t>);
}
