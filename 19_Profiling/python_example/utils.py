import numba
import numpy as np


@numba.njit()
def fill_row_ind_numba(row_ind, offset, nrows, ncols):
    for i in range(nrows):
        for j in range(ncols):
            row_ind[i * ncols + j] = offset + i


@numba.njit
def fill_col_ind_numba(col_ind, offset, nrows, ncols):
    for i in range(nrows):
        for j in range(ncols):
            col_ind[i * ncols + j] = offset + j


@numba.njit
def fill_indices_and_indptr_numba(indices, indptr, nrows_arr, ncols_arr):
    iptr = 1
    offset_c = 0
    for imat in range(nrows_arr.shape[0]):
        nrows = nrows_arr[imat]
        ncols = ncols_arr[imat]

        for irow in range(nrows):
            for icol in range(ncols):
                indices[indptr[iptr - 1] + icol] = offset_c + icol

            indptr[iptr] = indptr[iptr - 1] + ncols
            iptr += 1

        offset_c += ncols


def concatenate_list(mats, order='C'):
    return np.concatenate([mat.ravel(order=order) for mat in mats])
