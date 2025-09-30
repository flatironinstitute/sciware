#!/bin/bash

#SBATCH -C genoa
#SBATCH -t 5:00
#SBATCH -J inverse_test
#SBATCH -p gen

# you usually want to run on your center partition (ccm, cca, ccb, ccn, ccq). I'm using gen
# here because SCC has different default behavior than other center partitions

module -q reset
module -q load python
python inverse_test.py
