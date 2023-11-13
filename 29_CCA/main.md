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

- Binder
- Usage estimates
- JAX



# Binder


## Flatiron-hosted BinderHub

- Based on same software as mybinder.org
- Supports hosting environments and data on FI clusters (rather than github)
- Anyone with a google account can log in, can restrict access by email address
- Servers for [rusty](binder.flatironinstitute.org) and [popeye](sdsc-binder.flatironinstitute.org)


## Resource usage

- Default limits: 2 cores, 10G memory
   - Guaranteed resources vs. shared limits
   - Can increase limits, but this reduces number of possible binder users
- Popeye has a lot of available resources, rusty more limited
   - Testing access to GPUs on rusty (`gpu: true`)
- Monitor usage on [grafana.flatironinstitute.org](https://grafana.flatironinstitute.org/d/KqB4-8OZk/binder) from FI network


## Getting started

- [Wiki documentation](https://wiki.flatironinstitute.org/SCC/BinderHub)
- Create a directory under `~/public_binder`, e.g., `MyProjectEnv`
- Specify software environment (does not use cluster software)
   - conda packages in `environment.yml` (recommended)
   - pip packages in `requirements.txt`
   - many other options, including a custom `Dockerfile` providing jupyter-compatible server
- Create YAML configuration file `.public_binder`


## Configuration

Empty `~/public_binder/MyProjectEnv/.public_binder` works for defaults

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


## Data sharing considerations

- To share a data directory, it must be:
   - World-readable (`chmod o+rX`)
   - Owned by you, or in the same group as the `~/public_binder/MyProjectEnv`
   - Don't put data in `public_binder` directly (will be copied)
- No write access to shared data from binder


## User data storage

- Each user has their own `~/home` directory (`/home/jovyan/home`)
   - 1TB storage limit
   - Deleted after a few weeks of inactivity


## Sharing environments

- Give users your username and directory (environment) name
- Or link directly to `binder.flatironinstitute.org/~YOURUSER/MyProjectEnv`
