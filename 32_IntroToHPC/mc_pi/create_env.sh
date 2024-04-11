#!/bin/bash

module -q reset
module load python
if [[ ! -d "venv" ]]; then
    python -m venv venv --system-site-packages
fi
mkdir -p logs
