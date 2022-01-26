import numpy as np
import os
import glob
import tempfile

working_dir = "/mnt/ceph/users/rblackwell" # Path for our simulation data
n_steps = 10000                            # number of timesteps
n_write = 10                               # how many timesteps between each flush to file
n_particles = 1000                         # number of particles in our chain
n_dim = 3                                  # number of dimensions or chain lives in
D = 1.0                                    # diffusion coefficient
dt = 0.01                                  # timestep
kT = 1.0                                   # energy
gamma = kT / D                             # drag
k_spring = 0.1                             # spring constant between points on our chain


def write_handle(pos, traj_file, index=None):
    """Write each simulation frame by appending to file, maintaining an open file handle"""
    # Note: Using static variables like this is not good practice in most cases, but suits for
    # simplicity in this example to maintain the same function signature. Better practice is to
    # just pass a file handle in.
    if not hasattr(write_handle, 'f'):
        write_handle.f = open(traj_file, 'wb')
    write_handle.f.write(pos)


def write_append(pos, traj_file, index=None):
    """Write each simulation frame by appending to file, reopening each write"""
    with open(traj_file, 'ab') as f:
        f.write(pos)


def write_single(pos, traj_file, index):
    """Write each simulation frame as a separate file"""
    with open(traj_file + "." + str(index), 'wb') as f:
        f.write(pos)


def timestep(pos):
    """Steps a chain via a Brownian walk"""
    dx_diffusion = np.random.normal(loc=0.0,
                                    scale=np.sqrt(2 * dt * D),
                                    size=pos.shape)
    dx_spring = k_spring * (pos[:, 1:-1] - pos[:, 0:-2]) * dt / gamma
    pos[:, 0:-2] += dx_spring
    pos[:, 1:-1] -= dx_spring
    pos += dx_diffusion


def finalize():
    """Closes any open file handles"""
    if hasattr(write_handle, 'f'):
        write_handle.f.close()


def simulate(pos, traj_file, write_fun):
    """Simulates a chain, writing to file every n_write timesteps"""
    for i_step in range(n_steps):
        timestep(pos)
        if i_step % n_write == 0:
            write_fun(pos, traj_file, i_step // n_write)


if __name__ == '__main__':
    coords = np.zeros(shape=(n_dim, n_particles))
    with tempfile.TemporaryDirectory(dir=working_dir) as tmpdir:
        traj_file = os.path.join(tmpdir, 'traj.dat')
        simulate(coords, traj_file, write_single)
        finalize()
