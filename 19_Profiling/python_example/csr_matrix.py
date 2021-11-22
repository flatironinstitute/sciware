import numpy as np
from scipy.sparse import csr_matrix, block_diag
from utils import *


def block_diag_csr_matrix_rowcol_numba(mats):
    # linear array of non-zero output matrix elements
    data = concatenate_list(mats)
    # row/col indices (see scipy.sparse.csr_matrix documentation)
    row_ind = np.empty_like(data, dtype='int64')
    col_ind = np.empty_like(data, dtype='int64')

    # row/column index of upper left of current submatrix
    offset_r, offset_c = 0, 0

    # current position of the data 'pointer'
    offset = 0
    for mat in mats:
        nrows, ncols = mat.shape
        chunk_size = nrows * ncols

        fill_row_ind_numba(row_ind[offset:offset + chunk_size], offset_r,
                           nrows, ncols)
        fill_col_ind_numba(col_ind[offset:offset + chunk_size], offset_c,
                           nrows, ncols)

        offset_r += nrows
        offset_c += ncols
        offset += chunk_size

    return csr_matrix((data, (row_ind, col_ind)))


def block_diag_csr_matrix_index_ptrs_numba(mats):
    nrows_arr = np.empty(len(mats), dtype='int64')
    ncols_arr = np.empty(len(mats), dtype='int64')
    for i, mat in enumerate(mats):
        nrows_arr[i] = mat.shape[0]
        ncols_arr[i] = mat.shape[1]

    nrows_tot = nrows_arr.sum()
    ncols_tot = ncols_arr.sum()

    # linear array of non-zero output matrix elements
    data = concatenate_list(mats)
    indices = np.empty_like(data, dtype='int64')
    indptr = np.zeros(1 + nrows_tot, dtype='int64')

    fill_indices_and_indptr_numba(indices, indptr, nrows_arr, ncols_arr)

    return csr_matrix((data, indices, indptr), shape=(nrows_tot, ncols_tot))


def block_diag_csr_matrix_scipy(mats):
    block_diag_mat = block_diag(mats)
    return csr_matrix(block_diag_mat)


if __name__ == "__main__":
    nmats = 10000
    mats = []
    nrows_arr = np.zeros(nmats, dtype='int64')
    ncols_arr = np.zeros(nmats, dtype='int64')
    for i in range(nmats):
        mats.append(
            np.random.uniform(size=(np.random.randint(32, 64),
                                    np.random.randint(32, 64))))
        nrows_arr[i] = mats[-1].shape[0]
        ncols_arr[i] = mats[-1].shape[1]

    # precompile numba functions
    block_diag_csr_matrix_rowcol_numba(mats[0:2])
    block_diag_csr_matrix_index_ptrs_numba(mats[0:2])

    # make it take some time for cProfile
    for i in range(10):
        compressed_scipy = block_diag_csr_matrix_scipy(mats)
        compressed_rowcol = block_diag_csr_matrix_rowcol_numba(mats)
        compressed_index_ptrs = block_diag_csr_matrix_index_ptrs_numba(mats)
