# Sciware

https://sciware.flatironinstitute.org/32_IntroToHPC

https://github.com/flatironinstitute/sciware/tree/main/32_IntroToHPC



## Rules of Engagement

### Goal:

Activities where participants all actively work to foster an environment which encourages participation across experience levels, coding language fluency, *technology choices*\*, and scientific disciplines.

<small>\*though sometimes we try to expand your options</small>


## Rules of Engagement

- Avoid discussions between a few people on a narrow topic
- Provide time for people who haven't spoken to speak/ask questions
- Provide time for experts to share wisdom and discuss
- Work together to make discussions accessible to novices

<small>
(These will always be a work in progress and will be updated, clarified, or expanded as needed.)
</small>



## Center-hosted Sciware

- Sciware will rotate between centers each month
   - focus on topics of interest to centers
   - include voices from all centers
   - each center will host twice a year
   - open to all
- Suggest topics or contribute to content in #sciware Slack
- We are recording. Link will be posted to [https://sciware.flatironinstitute.org/](https://sciware.flatironinstitute.org/)



## Today's Agenda
- Flatiron resources overview
- Environment management [interactive]
- Running your jobs [interactive]



## Flatiron resources overview


### Two clusters: 'Rusty' and 'Popeye'

- Rusty on east coast, Popeye on west coast
- Completely distinct
  - Independent storage
  - Independent job management
- Both heterogenous -- multiple node types
- Details at https://wiki.flatironinstitute.org/SCC/Overview


### TODO Cluster components and lingo
- File systems
- Networks
- Nodes vs CPUs vs cores


### Rusty -- compute power

- FI's "primary" cluster
- \~100k CPU cores (\~1200 nodes)
- _Almost_ every node connected by high performance infiniband fabric
  - Dedicated (only for job traffic)
  - fiber-optic
  - Node types on different infiniband networks!
- 240 H100, 288 A100 and 98 V100 GPUs


### Popeye -- compute power

- \~41k dedicated CPU cores (\~800 nodes)
- Generally more available, but data separate from rusty
- Everything on infiniband fabric
- 128 V100 GPUs


### Rusty/popeye storage -- home

- Put your source code and software installs here!
- High performance GPFS filesystem (mounted NFS on workstations)
- Mind your quota! You can get locked out of the cluster!
  - \~1 million files
  - \~1 TiB limit
- `module load fi-utils && fi-quota`


### Rusty/popeye storage -- ceph

- rusty: located at `/mnt/ceph/$USER` or via symlink at `~/ceph`
- popeye: located at `/mnt/sdceph/$USER` or via symlink at `~/ceph`
- Always put your data/large files here!
- \~45 PiB (rusty) and \~15 PiB (popeye)
- High bandwidth, high latency (\~1.5GiB/s parallel reads)
- Highly redundant, but not backed up



## Environment management


## What you'll need

- Remote access to the cluster via terminal
  - on 'FI' wifi network: `ssh username@rusty`
  - or... `ssh -p 61022 username@gateway.flatironinstitute.org`, `ssh rusty`
  - or... `https://jupyter.flatironinstitute.org`
- Way to edit files on cluster
  - terminal `emacs/vi/nano/ed`
  - or... remote edit via `vscode/emacs/vi/sshfs`
  - or... `https://jupyter.flatironinstitute.org`


## Navigating/building/running software

- decide language (to discuss compilers and play with modules)
- intro to modules (modules as a 'tree', `module avail`)
- If possible, how to compile software in addition to python [high priority]
- failure state if say, can't find necessary stuff (compiling with system compiler, or running without gcc loaded)
- icx + gcc necessary
- move this down to later


## Let's make a python project

- create new project directory
- `ml python ; python -m venv venv --system-site-packages ; source venv/bin/activate`
- create `setup_env` script that loads clean environment


## Please never do this

- Calculate π by throwing darts "_Monte Carlo Sampling_"
- π ≅ 4 N<sub>in</sub> / N<sub>tot</sub>
- https://github.com/flatironinstitute/tree/main/32_IntroToHPC/mc_pi
<center>
    <img src="./assets/dartboard.png" style="border:0;box-shadow:none" height="350px">
</center>


## Running it on the cluster
- Demonstrate how to sbatch script with single
- just me, not other people (1 node, gen, partition, etc)


## Scaling up
- We could make our code more efficient...
- But let's throw some power at it


## MPI with slurm
- This is not recommended with embarrassingly parallel problems (like this one)
- We're going to do it anyway...


## disBatch
- Create list of tasks, pass to disBatch
- `module load disBatch`
- sbatch <sbatch options> disBatch task_file



## SciWare Survey [TODO]
<!-- <center> -->
<!-- <img width="50%" src="./qr.png"> -->
<!-- </center> -->
