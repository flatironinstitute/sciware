from timeit import default_timer

import click
import numpy as np

from . import examplemod

@click.command()
@click.option('--n', default=10_000, help='Number of particles')
@click.option('--nbin', default=30, help='Number of bins')
@click.option('--seed', default=123, help='Random seed')
def main(n, nbin, seed):
    rng = np.random.default_rng(seed)
    pos2d = rng.random((n, 2))
    dist = np.zeros(nbin, dtype=np.uint64)
    
    t_nanobind = -default_timer()
    examplemod.compute_pair_dist(dist, pos2d)
    t_nanobind += default_timer()
    print(dist)
    print(f'\tnanobind: {t_nanobind:.4g} sec')

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
