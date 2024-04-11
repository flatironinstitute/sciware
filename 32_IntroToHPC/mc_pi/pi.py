import numpy as np
import sys

N = int(float(sys.argv[1]))
seed = int(sys.argv[2])
np.random.seed(seed)

hits = 0
for i in range(N):
    hits += int(np.linalg.norm(np.random.uniform(low=-1, high=1.0, size=2)) <= 1.0)

pi = 4 * hits / N
print(f'{pi:.16f}')
