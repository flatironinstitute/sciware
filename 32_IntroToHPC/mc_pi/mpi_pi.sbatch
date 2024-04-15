#!/bin/bash 
#SBATCH -o mpi_pi.log
#SBATCH -e mpi_pi.err
#SBATCH -N 2
#SBATCH -c 1
#SBATCH -n 256
#SBATCH -p scc
#SBATCH -C ib-rome
#SBATCH -t 1:00

source load_env.sh
mpirun python mpi_pi.py 100000
