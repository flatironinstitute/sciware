#!/bin/bash 
#SBATCH -o mpi_pi.log        # stdout logfile
#SBATCH -e mpi_pi.err        # stderr logfile
#SBATCH -N 1                 # 1 nodes
#SBATCH --ntasks-per-node 64 # 64 cores on icelake node
#SBATCH -p scc               # change this to your center partition
#SBATCH -C ib-icelake        # rome, using 'infiniband' constraint
#SBATCH -t 10:00             # 10 min max runtime

echo $SLURM_JOBID

source load_env.sh
srun python mpi_pi.py 1000000
