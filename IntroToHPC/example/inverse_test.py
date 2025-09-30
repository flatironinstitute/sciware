import numpy as np
from scipy.linalg import lu
import os
import time

dt = -time.time()
N = 5000
alpha = 0.1
seed = os.getpid()

gen = np.random.MT19937
rng = np.random.Generator(gen(seed=seed))

print(f"Generating and decomposing a {N}x{N} matrix with alpha={alpha} and seed={seed}.")

# Generate a random n x n matrix
gen_time = -time.time()
A = rng.random((N, N)) + alpha * np.eye(N)
gen_time += time.time()
print(f"Matrix generation took {gen_time:.2f} seconds.")

lu_time = -time.time()
P, L, U = lu(A)
lu_time += time.time()
print(f"LU decomposition took {lu_time:.2f} seconds.")

check_time = -time.time()
success = np.allclose(A, P @ L @ U)
check_time += time.time()
print(f"LU decomposition validation took: {check_time:.2f} seconds and reported success = {success}.")

inv_time = -time.time()
A_inv = np.linalg.inv(A)
inv_time += time.time()
print(f"Matrix inversion took {lu_time:.2f} seconds.")

check_time = -time.time()
success = np.allclose(np.eye(N), A_inv @ A)
check_time += time.time()
print(f"Inversion validation took: {check_time:.2f} seconds and reported success = {success}.")

dt += time.time()
print(f"Total time: {dt:.2f} seconds.")
