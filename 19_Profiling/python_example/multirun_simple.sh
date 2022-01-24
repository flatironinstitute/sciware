#!/bin/bash

DIR=$(dirname "${BASH_SOURCE[0]}")
DIR=$(realpath "${DIR}")

python "$DIR/simulation.py" &
python "$DIR/simulation.py" &
python "$DIR/simulation.py" &
echo "Run complete"
