#include <nanobind/nanobind.h>
#include <nanobind/ndarray.h>

namespace nb = nanobind;

template <typename Scalar>
void compute_pair_dist(nb::ndarray<uint64_t, nb::shape<nb::any>, nb::c_contig, nb::device::cpu> dist,
                       nb::ndarray<const Scalar, nb::shape<nb::any, 2>, nb::c_contig, nb::device::cpu> pos2d) {
    /* Compute all pair-wise distances between the points in `pos2d`
     * and store the histogram of distances in `dist`.
     */

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


NB_MODULE(examplemod, m) {
    m.def("compute_pair_dist", &compute_pair_dist<float>);
    m.def("compute_pair_dist", &compute_pair_dist<double>);
}
