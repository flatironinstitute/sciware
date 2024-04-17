#!/bin/bash 
#SBATCH -o mpi_pi.log # stdout logfile
#SBATCH -e mpi_pi.err # stderr logfile
#SBATCH -N 2          # 2 nodes, one task per core
#SBATCH -p scc        # change this to your center partition
#SBATCH -C ib-rome    # rome, using 'infiniband' constraint
#SBATCH -t 10:00      # 10 min max runtime

source load_env.sh
mpirun python mpi_pi.py 1000000
