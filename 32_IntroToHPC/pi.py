import numpy as np
import sys

N = int(float(sys.argv[1]))
nums = np.random.uniform(low=-1, high=1.0, size=(N, 2))
pi = 4 * np.mean(np.linalg.norm(nums, axis=1) <= 1.0)
print(pi)

hits = 0
for i in range(N):
    hits += int(np.linalg.norm(np.random.uniform(low=-1, high=1.0, size=2)) <= 1.0)

pi = 4 * hits / N
print(pi)
