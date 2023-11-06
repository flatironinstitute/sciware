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


## Zoom Specific

- Dedicated Zoom moderator to field questions.
- Please stay muted if not speaking. (Host may mute you.)
- We are recording. Link will be posted to [https://sciware.flatironinstitute.org/](https://sciware.flatironinstitute.org/)


## Future Sessions

- Suggest topics or contribute to content in #sciware Slack


## Today's Agenda

- JAX
- Usage estimates
- Binder



# Binder


## Flatiron-hosted BinderHub

- Based on same software as mybinder.org
- Supports hosting environments and data on FI clusters (rather than github)
- Anyone with a google account can log in, can restrict access by email address
- Servers for [rusty](binder.flatironinstitute.org) and [popeye](sdsc-binder.flatironinstitute.org)


## Getting started

- [Wiki documentation](https://wiki.flatironinstitute.org/SCC/BinderHub)
- Create a directory under `~/public_binder`, e.g., `MyProjectEnv`
- Specify software environment (does not use cluster software)
   - Add pip packages to `requirements.txt` *or* conda packages to `environment.yml` (or other options)
- Create YAML configuration file `~/pubilc_binder/MyProjectEnv/.public_binder`
   - Specify users with access, directories to share, resource limits


## Data storage considerations

- To share a data directory, it must be:
   - World-readable
   - Owned by you, or in the same group as the `~/public_binder/MyProjectEnv`
   - Either list "mounts" in `.public_binder` *or* create symlinks
- No write access to shared data from binder
- Each user has their own `~/home` directory
   - 1TB storage limit
   - Deleted after a few weeks of inactivity


## Specifying environments

- Conda provides the most flexible environment, but can be tricky to setup
   - Add conda (not pip) packages to `environment.yml`
- You can also write custom script for additional installation, or a full `Dockerfile`
- Can host any jupyter-compatible server
- Give users your username and directory (environment) name
   - Or link directly to `binder.flatironinstitute.org/~YOURUSER/MyProjectEnv`


## Resource usage

- Default limits: 2 cores, 10G memory
- Can increase limits, but this reduces number of binder users
- Popeye has a lot of available resources, rusty more limited
   - Looking to expand rusty, possibly add GPUs
- Monitor usage on [grafana](https://grafana.flatironinstitute.org/d/KqB4-8OZk/binder) from FI network
