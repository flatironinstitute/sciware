#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --cpus-per-task=1
#SBATCH --constraint=rome,ib
#SBATCH --partition=ccb
#SBATCH --time=01:00:00
#SBATCH --job-name=slurm_dedalus_examplerun1
#SBATCH --output=slurm_dedalus_examplerun1.log

# Set up our environment for this SLURM submission
module -q purge
module -q load modules/2.2-20230808
module -q load gcc/11
module -q load openmpi/4.0.7
module -q load python/3.10.10
module -q load fftw/mpi-3.3.10
module -q load dedalus/3.2302-dev-py3.10.10
module list

# Explicitly set the number of openmp tasks per mpi process
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Helper functions to see what kind of system we are running on, if we have GPUs that are accessible, and other information
lscpu
nvidia-smi
numactl -H

# Run dedalus on the python file
mpirun --map-by socket:pe=$OMP_NUM_THREADS -np $SLURM_NTASKS_PER_NODE --report-bindings python3 dedalus_examplefiber.py
