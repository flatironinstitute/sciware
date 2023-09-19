#!/bin/bash
#SBATCH --nodes=2                     # number of nodes
#SBATCH --ntasks-per-node=8           # number of tasks per node
#SBATCH --cpus-per-task=16            # number of cpus(threads) per task
#SBATCH --constraint=rome,ib          # computers to use at FI
#SBATCH --partition=ccb               # center allocation
#SBATCH --time=00:10:00               # maximum time for job
#SBATCH --job-name=mpi_omp_example1   # job name
#SBATCH --output=mpi_omp_example1.log # slurm output file

# Set up our environment for this SLURM submission
module -q purge                       # purge current modules
module -q load openmpi                # Load openmpi
module list                           # What modules are loaded?

# Helper functions to see what kind of system we are running on, if we have GPUs that are accessible, and other information
lscpu                                 # What cpus do we have?
nvidia-smi                            # Is there gpu information?
numactl -H                            # What is the NUMA layout

# Print some helpful information
echo "Slurm nodes:              ${SLURM_NNODES}"
echo "Slurm ntasks:             ${SLURM_NTASKS}"
echo "Slurm ntasks-per-node:    ${SLURM_NTASKS_PER_NODE}"
echo "Slurm cpus-per-task:      ${SLURM_CPUS_PER_TASK}"

# Run the program
OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK} mpirun mpi_omp_mockup
