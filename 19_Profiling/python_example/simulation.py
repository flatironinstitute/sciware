import numpy as np
import os
import sys

n_steps = 100000
n_write = 100
n_particles = 1000
n_dim = 3
coords = np.random.uniform(size=(n_particles, n_dim))

traj_file = "traj.dat"


def write_handle(f, pos):
    f.write(pos)


def write_append(pos, index=None):
    f = open(traj_file, 'ab')
    f.write(pos)


def write_single(pos, index):
    f = open(traj_file + "." + str(index), 'wb')
    f.write(pos)


def timestep(pos):
    pos = np.random.uniform(size=pos.shape)


def simulate(pos, write_fun):
    for i_step in range(n_steps):
        timestep(pos)
        if i_step % n_write == 0:
            write_fun(pos, i_step // n_write)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Supply writer as argument: handle, append, single")

    if os.path.isfile(traj_file):
        os.remove(traj_file)

    writer = sys.argv[1]
    if writer == "handle":
        f = open(traj_file, 'wb')
        write_fun = lambda pos, index: write_handle(f, pos)
    elif writer == "append":
        write_fun = write_append
    elif writer == "single":
        write_fun = write_single
    else:
        print(
            "Invalid writer supplied. Valid options are: handle, append, single"
        )

    simulate(coords, write_fun)
