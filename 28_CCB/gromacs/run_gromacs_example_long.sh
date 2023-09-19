#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=120
#SBATCH --cpus-per-task=1
#SBATCH --constraint=rome,ib
#SBATCH --partition=ccb
#SBATCH --time=01:00:00
#SBATCH --job-name=slurm_gromacs_examplerun_long
#SBATCH --output=slurm_gromacs_examplerun_long.log

# Set up our environment for this SLURM submission
module -q purge
module -q load modules/2.2-20230808
module -q load openmpi/cuda-4.0.7
module -q load gromacs/mpi-2023.1
module list

# Explicitly set the number of openmp tasks per mpi process
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Helper functions to see what kind of system we are running on, if we have GPUs that are accessible, and other information
lscpu
nvidia-smi
numactl -H

# If you want to compile the TPR file yourself, uncomment this command
# mpirun -np 1 gmx_mpi grompp -f gromacs_examplerun_long.mdp -o gromacs_examplerun_long.tpr -c step6.6_equilibration.gro -p topol.top -n index.ndx

# Run the TPR file for gromacs
mpirun --map-by socket:pe=$OMP_NUM_THREADS gmx_mpi mdrun -v -deffnm gromacs_examplerun_long
