# Sciware

https://sciware.flatironinstitute.org/29_CCA

https://github.com/flatironinstitute/sciware/tree/main/29_CCA


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

- Binder
- Usage estimates
- JAX



# Binder

### Shy Genel

[slides](https://docs.google.com/presentation/d/1XD2M2kY2MMW08AvuZlr9Q3FY9PBkBAnkGES98BY4ukU/edit)

### Dylan Simon (SCC)


## Flatiron-hosted BinderHub

- Based on same software as mybinder.org
- Supports hosting environments and data on FI clusters (rather than github)
- Anyone with a google account can log in, can restrict access by email address
- Servers for [rusty](binder.flatironinstitute.org) and [popeye](sdsc-binder.flatironinstitute.org)


## Resource usage

- Default limits: 2 cores, 10G memory
   - Guaranteed resources vs. shared limits
   - Can increase limits, but this reduces number of possible binder users
- Popeye has a lot of available resources, rusty busier
   - Testing access to GPUs on rusty (`gpu: true`)
- Monitor usage on [grafana.flatironinstitute.org](https://grafana.flatironinstitute.org/d/KqB4-8OZk/binder) from FI network


## Getting started

- [Wiki documentation](https://wiki.flatironinstitute.org/SCC/BinderHub)
- Create a directory under `~/public_binder`, e.g., `MyProjectEnv`
- Create YAML configuration file `.public_binder`


## Configuration

Empty `~/public_binder/MyProjectEnv/.public_binder` fine for defaults

```yaml
mounts: # from symlinks if not specified
  symlinkname: symlinktarget
  mydata: '/mnt/ceph/users/you/yourdata'
users: # all users by default
  - user1@gmail.com
cpu_guarantee: 1 # dedicated exclusively to each user
cpu_limit: 2 # peak usage limit (shared)
mem_guarantee: '10G'
mem_limit: '20G'
```


## Software environment

- Does not use cluster software
- Conda packages in `environment.yml`

      dependencies:
      - scipy
      - h5py=3.9.0
      - python=3.10
      - pip:
        - git+https://github.com/user/package --flags
- Pip packages in `requirements.txt` (python version in `runtime.txt`)
- Additional commands to run in `postBuild`
- Many other options, including custom `Dockerfile` providing jupyter-compatible server


## Data sharing considerations

- To share a data directory, it must be:
   - World-readable (`chmod o+rX`)
   - Owned by you, or in the same group as directory `~/public_binder/MyProjectEnv`
   - Avoid putting large data in `public_binder` directly (will be copied)
   - Symlinks only work in top-level directory
- No write access to shared data from binder


## User data storage

- Each user has their own `~/home` directory (`/home/jovyan/home`)
   - 1TB storage limit
   - Deleted after a few weeks of inactivity


## Sharing environments

- Give users your username and directory (environment) name
- Or link directly to `binder.flatironinstitute.org/~YOURUSER/MyProjectEnv`



# Usage estimates

### Yan-Fei Jiang

[slides](https://www.dropbox.com/sh/hrw4ulndqfa0iff/AADy7WZA1UHtAyAXK9EfvKVua?dl=0)



# JAX

### Kaze Wong

[slides](https://kazewong.github.io/MyUnhingedPresnetations/reveal/SciwareJax2023/top.html)
