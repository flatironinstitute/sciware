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



# SSHFS and FUSE
- SSH FileSystem (SSHFS): SSHFS lets you remotely mount filesystems over ssh. It's a convenient way to access files on the cluster as if they're on your local machine. (Think Dropbox but for files stored on cluster instead of the cloud.)

- Filesystem in USErspace (FUSE): "a software interface for Unix and Unix-like computer operating systems that lets non-privileged users create their own file systems without editing kernel code." -Wikipedia. Needed by SSHFS to create the mount point in the cluster directory.

https://docs.simonsfoundation.org/index.php/Public:Playbooks/SSHFS


## Demo of what SSHFS can do


## Things to know 
- It is very sensitive to latency, so depending on your connection, may sometimes be a bit slow.


## Setting up FUSE for cluster
- Install fuse and sshfs (may already be installed on linux, or should be in your package manager; on OSX download them [here](https://osxfuse.github.io/)).
- Make sure you can `ssh flatiron` (from inside the FI network) or `ssh gateway` (from outside), following the [RemoteConnect](https://docs.simonsfoundation.org/index.php/RemoteConnect) instructions if necessary.
- Choose which directory you want to mount, such as /mnt/home/USERNAME or /mnt/ceph/users/USERNAME and create directories on your local computers to mount in. 


It often makes things more convenient to use paths matching the cluster. If you wish to do this, then type the following commands
```bash
sudo mkdir -p /mnt/home/<USERNAME /mnt/ceph/users/USERNAME
sudo chown $USER /mnt/home/USERNAME /mnt/ceph/users/USERNAME

```


- Mount the directory you want from the server you can connect to, e.g.:

```bash
sshfs flatiron:/mnt/home/USERNAME /mnt/home/USERNAME
```