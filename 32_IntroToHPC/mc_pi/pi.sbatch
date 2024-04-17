#!/bin/bash -e
#SBATCH -o pi.log
#SBATCH -e pi.err
#SBATCH -p genx
#SBATCH -t 1:00

source load_env.sh
python pi.py 100000 0
