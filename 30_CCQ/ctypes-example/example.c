#include <math.h>
#include <stddef.h>
#include <stdint.h>

void double_arr(size_t n, double *outarr, double const *inarr) {
    for (size_t i = 0; i < n; i++) {
        outarr[i] = 2 * inarr[i];
    }
}
