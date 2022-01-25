import numpy as np
import os
import glob

n_steps = 10000
n_write = 10
n_particles = 1000
n_dim = 3
traj_file = "traj.dat"
D = 1.0
dt = 0.01
kT = 1.0
gamma = kT / D
k_spring = 0.1


def write_handle(pos, traj_file, index=None):
    # Note: Using static variables like this is not good practice in most cases, but suits for
    # simplicity in this example to maintain the same function signature. Better practice is to
    # just pass a file handle in.
    if not hasattr(write_handle, 'f'):
        write_handle.f = open(traj_file, 'wb')
    write_handle.f.write(pos)


def write_append(pos, traj_file, index=None):
    f = open(traj_file, 'ab')
    f.write(pos)


def write_single(pos, traj_file, index):
    f = open(traj_file + "." + str(index), 'wb')
    f.write(pos)


def timestep(pos):
    dx_diffusion = np.random.normal(loc=0.0,
                                    scale=np.sqrt(2 * dt * D),
                                    size=pos.shape)
    dx_spring = k_spring * (pos[:, 1:-1] - pos[:, 0:-2]) * dt / gamma
    pos[:, 0:-2] += dx_spring
    pos[:, 1:-1] -= dx_spring
    pos += dx_diffusion


def cleanup(traj_file):
    for filepath in glob.glob(traj_file + "*"):
        try:
            os.remove(filepath)
        except (FileNotFoundError):
            # Trying to remove the 'traj.dat' file but it's already been removed.
            # This can happen sometimes due to a race condition if multiple instances
            # of the script are running. In production code, we would avoid this
            # by using formal temp files/directories, but for this example we don't
            # care as long as the file's gone, so just ignore the error.
            pass


def simulate(pos, traj_file, write_fun):
    for i_step in range(n_steps):
        timestep(pos)
        if i_step % n_write == 0:
            write_fun(pos, traj_file, i_step // n_write)


if __name__ == '__main__':
    coords = np.zeros(shape=(n_dim, n_particles))
    cleanup(traj_file)
    simulate(coords, traj_file, write_append)
