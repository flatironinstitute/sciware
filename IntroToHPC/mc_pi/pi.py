import numpy as np
import sys

N = int(float(sys.argv[1]))
seed = int(sys.argv[2])
rng = np.random.default_rng(seed=seed)

hits = 0
for i in range(N):
    xy = rng.uniform(low=-1.0, high=1.0, size=2)
    if np.linalg.norm(xy) <= 1.0:
        hits += 1

pi = 4 * hits / N
print(f'{pi:.16f}')
