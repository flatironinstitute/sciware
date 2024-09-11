[[ ! -z $CONDA_DEFAULT_ENV ]] && conda deactivate

module -q reset
module load openmpi python python-mpi
source myenv/bin/activate
