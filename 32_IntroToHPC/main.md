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


### Rusty -- compute power

- ~100k dedicated CPU cores 
- two 3-6TB 'bigmem' machines
- Almost everything on high bandwidth fabric (omnipath *or* infiniband)
- GPUs
  - 144 H100 (18 x 8)
  - 288 A100 (72 x 8)
  - 8 V100 (22 x 4 + 5 x 2)


### Popeye -- compute power

- Appx. 41k dedicated CPU cores
- 1 3TB 'bigmem' machine
- Everything (but bigmem) on infiniband
- 128 V100 (32 x 4) GPUs


### Rusty/popeye storage -- home

- Put your source code and software installs here!
- High performance GPFS filesystem (mounted NFS on workstations)
- Mind your quota! You can get locked out of the cluster!
  - ~1 million files
  - ~1 TiB limit
- `module load fi-utils && fi-quota`


### Rusty/popeye storage -- ceph

- rusty: located at `/mnt/ceph/$USER` or via symlink at `~/ceph`
- popeye: located at `/mnt/sdceph/$USER` or via symlink at `~/ceph`
- Always put your data/large files here!
- ~45 PiB (rusty) and ~15 PiB (popeye)
- High bandwidth, high latency (~1.5GiB/s parallel reads)
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


##



## SciWare Survey [TODO]
<!-- <center> -->
<!-- <img width="50%" src="./qr.png"> -->
<!-- </center> -->
