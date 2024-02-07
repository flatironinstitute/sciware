import ctypes
from timeit import default_timer

import click
import numpy as np

SO_FILE = './example.so'

@click.command()
@click.option('--n', default=10_000, help='Number of particles')
@click.option('--nbin', default=30, help='Number of bins')
@click.option('--seed', default=123, help='Random seed')
def main(n, nbin, seed):
    rng = np.random.default_rng(seed)
    pos2d = rng.random((n, 2))
    dist = np.zeros(nbin, dtype=np.uint64)
    
    lib = ctypes.CDLL(SO_FILE)
    compute_pair_dist = lib.compute_pair_dist
    # void compute_pair_dist(
    #     const size_t nbin,
    #     size_t *dist,
    #     const size_t npart,
    #     const double *pos2d
    # )
    compute_pair_dist.argtypes = [ctypes.c_size_t,
                                  ctypes.POINTER(ctypes.c_size_t),
                                  ctypes.c_size_t,
                                  ctypes.POINTER(ctypes.c_double),
                                  ]
    compute_pair_dist.restype = None
    
    t_ctypes = -default_timer()
    compute_pair_dist(nbin,
                      dist.ctypes.data_as(ctypes.POINTER(ctypes.c_size_t)),
                      n,
                      pos2d.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
                      )
    t_ctypes += default_timer()
    print(dist)
    print(f'\tctypes: {t_ctypes:.4g} sec')

    # solve with numpy
    t_numpy = -default_timer()
    all_dists = np.linalg.norm(pos2d[:, None] - pos2d, axis=-1)
    hist, _ = np.histogram(all_dists, bins=nbin, range=(0, 1))
    hist[0] -= n
    hist //= 2
    t_numpy += default_timer()
    print(hist)
    print(f'\tnumpy: {t_numpy:.4g} sec')

if __name__ == '__main__':
    main()
