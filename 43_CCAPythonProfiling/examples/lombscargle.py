import numpy as np

from astropy.timeseries import (
    LombScargle,
)

rng = np.random.default_rng(
    seed=123
)
N = 10**6
t = rng.uniform(
    0, 100, size=N
)
y = rng.poisson(
    np.sin(50 * t) + 2, size=N
)

frequency, power = (
    LombScargle(
        t, y
    ).autopower()
)
