
if [[ ! -z $VIRTUAL_ENV ]]; then
    deactivate
fi

if [[ ! -z $CONDA_DEFAULT_ENV ]]; then
    conda deactivate
fi

module -q reset
module load openmpi python python-mpi
source venv/bin/activate
