import numpy as np
from mpi4py import MPI
import sys

N = int(float(sys.argv[1]))
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
np.random.seed(rank)

hits = 0
for i in range(N):
    hits += int(np.linalg.norm(np.random.uniform(low=-1.0, high=1.0, size=2)) <= 1.0)

hits_arr = comm.gather(hits, root=0)
if rank == 0:
    pi = 4 * np.array(hits_arr).mean() / N
    print(f'{pi:.16f}', np.abs(100 * (1 - pi/np.pi)))
