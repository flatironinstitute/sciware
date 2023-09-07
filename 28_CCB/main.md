# Sciware

## The many faces of parallelism
### Running parallel codes on the cluster

https://sciware.flatironinstitute.org/28_CCB

https://github.com/flatironinstitute/sciware/tree/main/28_CCB


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


## Zoom Specific

- Dedicated Zoom moderator to field questions.
- Please stay muted if not speaking. (Host may mute you.)
- We are recording. Link will be posted to [https://sciware.flatironinstitute.org/](https://sciware.flatironinstitute.org/)


## Future Sessions

- Suggest topics or contribute to content in #sciware Slack


## Today's Agenda



# Measuring performance on HPC clusters
- We want our code to be as performant as possible!
- Need to define
  - "Time"
  - "Performant"
  - <h4 style="color:rgb(255,0,0)">"Efficiency"</h4>
- How do we do this in an HPC/cluster environment?
- "Premature optimization is the root of all evil" -- Donald Knuth


## Problem statement
We have highly parallelized code \<foo\> and want to get the "best" performance out of it that we can.


## A brief introduction to cluster computing (at FI)
<small>
(Although much of this information will work at other clusters)
</small>

- How do you share a set of computational resources among cycle-hungry scientists?
  - With a job scheduler! Also known as a queue system.
- Flatiron uses [Slurm](https://slurm.schedmd.com) to schedule jobs


## A standard SLURM script
```bash
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=16
#SBATCH --constraint=rome,ib
#SBATCH --partition=ccb
#SBATCH --time=00:10:00
#SBATCH --job-name=mpi_omp_example4
#SBATCH --output=mpi_omp_example4.log

# Set up our environment for this SLURM submission
module -q purge
module -q load openmpi
module list

# Helper functions to see what kind of system we are running on, if we have GPUs that are accessible, and other information
lscpu
nvidia-smi
numactl -H

# Print some helpful information
echo "Slurm nodes:              ${SLURM_NNODES}"
echo "Slurm ntasks:             ${SLURM_NTASKS}"
echo "Slurm ntasks-per-node:    ${SLURM_NTASKS_PER_NODE}"
echo "Slurm cpus-per-task:      ${SLURM_CPUS_PER_TASK}"

# Run the program
OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK} mpirun -np ${SLURM_NTASKS} --report-bindings mpi_omp_mockup
```


## Running a simple MPI/OpenMP executable on the cluster
<foo> = mpi\_omp\_mockup

```bash
cd mpi_omp_mockup/
sbatch run_slurm_example1.sh
```

What do you see for the output of the log file?

<small>
If you want to compile mpi\_omp\_mockup.cpp, feel free to do so with MPI and OpenMP
</small>


## Understanding performance metrics

### Time exists so everything doesn't happen all at once!

- "Wall time" = time
- "CPU time" = cpu cores * time
  - Multiple threads
  - 1 core for 1 second + 8 cores for 5 seconds + 1 core for 2 seconds = 43 cpu seconds, 8 wall seconds
- Need to figure out what we just ran...


## Getting performance results through **seff**

Getting previous job information from the cluster (need JobID)
```bash
> sacct
JobID           JobName  Partition    Account  AllocCPUS      State ExitCode 
------------ ---------- ---------- ---------- ---------- ---------- -------- 
2640715      mpi_omp_e+        ccb        ccb        256  COMPLETED      0:0 
2640715.bat+      batch                   ccb        128  COMPLETED      0:0 
2640715.ext+     extern                   ccb        256  COMPLETED      0:0 
2640715.0         orted                   ccb        128  COMPLETED      0:0
```


# Ways to access and transfer data
- Globus
- Globus public download portal
- SSHFS
- JupyterHub
- [Other options on wiki...](https://wiki.flatironinstitute.org/SCC/DataSharing)


# Globus


# SSHFS and FUSE
- SSH FileSystem (SSHFS): Is a convenient way to access files on the cluster as if they're on your local machine. 

- Filesystem in USErspace (FUSE): Needed by SSHFS to 'mount' a filesystem. 

https://wiki.flatironinstitute.org/SCC.Playbooks/SshFsMount


## What can SSHFS do?

- Access files on the cluster as if they're on your local machine
- Transfer files between your local machine and the cluster


## Things to know 
- It is very sensitive to latency, so depending on your connection, may sometimes be slow.
- Folders mounted on the cluster, e.g, a zip archive mounted using `fusermount`, may not show up in directory.
- Used primarly to interact with files using GUI and visual tools.


## Setting up FUSE for cluster
- Install FUSE and SSHFS (may already be installed on linux, or should be in your package manager; on OSX download them [here](https://www.fuse-t.org)).
- Make sure you can `ssh rusty` (from inside the FI network) or `ssh gateway` (from outside), following the [RemoteConnect](https://wiki.flatironinstitute.org/SCC/RemoteConnect) instructions if necessary.
- Choose which cluster directory you want to mount, such as `/mnt/home/USERNAME` or `/mnt/ceph/users/USERNAME`, and create directories on your local computers to mount to. 


It often makes things more convenient to use paths matching the cluster. If you wish to do this, then type the following command
```bash
mkdir -p ~/mnt/home/USERNAME ~/mnt/ceph/users/USERNAME
```


- Mount directory you want from the server, e.g.:
```bash
sshfs rusty:/mnt/home/USERNAME ~/mnt/home/USERNAME 
```

## Example
```bash
> cd ~/mnt/home/alamson/
> ls
> sshfs rusty:/mnt/home/alamson/ ~/mnt/home/alamson/
> ls
10-powerline-symbols.conf ceph                      requirements.txt
Chi                       intel                     test_local
Desktop                   libyaml-cpp.a             test_projects
Downloads                 local                     
bash_profile              projects
bashrc                    public_www
```

## Tips and Tricks
- Create aliases for common mount points in your `.bashrc` or `.bash_profile` files, e.g.:
```bash
alias mount_home='sshfs flatiron:/mnt/home/USERNAME /mnt/home/USERNAME'
```
