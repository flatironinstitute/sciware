#include <math.h>
#include <stddef.h>
#include <stdint.h>

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
