#!/bin/bash

module -q reset
module load python
if [[ ! -d "myenv" ]]; then
    python -m venv myenv --system-site-packages
fi
mkdir -p logs
