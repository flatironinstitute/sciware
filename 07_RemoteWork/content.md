# Sciware

## Working Remotely

https://github.com/flatironinstitute/learn-sciware-dev/tree/master/07_RemoteWork


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

- If comfortable, please keep video on so we can all see each other's faces.
- Ok to break in for quick, clarifying questions.
- Use Raise Hand feature for new topics or for more in-depth questions.
- Please stay muted if not speaking. (Host may mute you.)


## Feedback

- Future sessions planned:
   - Intro to Julia
   - Optimizing Python Numeric Computing Performance 
   - Intro to GitHub (with Software Carpentry)
- Suggest topics and vote on options in #sciware Slack



## Today's Agenda

- Zoom Lessons
- Remote Access Overview
- Remote Display (XQuartz, X11, VNC)
- Persistent Development Environments
- Discussion, Open Share



## SSH

* OpenSSH has a number of useful features that can be configured (per-host) in `~/.ssh/config`
* These apply to the *client* side only: the place you run "ssh"
* The file is divided into `Host` sections, matching the "host" on the command line against each section

```
# settings only for "ssh myhost"
Host myhost
Hostname server.to.connect.edu
Port 22

# settings for one domain
Host *.flatironinstitute.org
User myuser

Host *
# defaults for all hosts
```


### Keypairs

* Keypairs let you authenticate to some hosts
* Generate a new private/public key pair

        ssh-keygen -t ed25519 -f ~/.ssh/id_mykey

* You should set a new passphrase unless your local machine is secure (e.g., encrypted disk, or at least more secure than the server, e.g., github)
* The private key (`id_mykey`) is your "password"
* The public key (`id_mykey.pub`) can be put on servers to accept the private key


* Use it in *client* config

        IdentityFile ~/.ssh/id_mykey
        KbdInteractiveAuthentication no

* Add it to *server* `~/.ssh/authorized_keys` (list of keys, one per line)

        ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIP6+dWRKWnpvs+JQcA1I6RW2Lq11Q/CWu87I3SZXYsYw

* Or use `ssh-copy-id -i ~/.ssh/id_mykey host`
* You can also set additional options/restrictions per key

        from="my.client.com" environment="TERM=screen" command="..." ssh-ed25519 ...


### ControlMaster

Another way to avoid authentication when reconnecting is to re-use a single connection

```
Host myhost
ControlMaster auto

Host *
ControlPath ~/.ssh/.%r@%h:%p
```

Now if you run `ssh myhost` in two different windows, the second will re-use the first connection without authentication


### Compression

If you're on a *slow* connection, compression may help

```
Compression yes
```

### Keep alive

If your router (or, horrors, ISP) drops idle connections, enable keep-alives

```
ServerAliveInterval 60
```


### Specific port forwards

Forward specific services (https, vnc, ssh)

```
LocalForward 127.0.0.1:23443 jupyter:443
LocalForward 127.0.0.1:43059 x2go01:5902
LocalForward 127.0.0.1:51022 myhost:22
```

I often use this for chaining ssh

```
Host gateway
Hostname gateway.flatironinstitute.org
LocalForward 127.0.0.1:51022 myhost:22

Host myhost
Hostname 127.0.0.1
Port 51022
```

Newer ssh provides another way

```
Host myhost
ProxyJump gateway
```


### Dynamic port forwarding (SOCKS)

```
DynamicForward 21099
```

Now configure your browser to use a SOCKS5 proxy at `127.0.0.1:21099` (or use something like `runsocks`)

### Forward only

* Sometimes you want to connect only to setup forwards, and don't need a shell

        ExitOnForwardFailure yes

        ssh -Nf host


### Advanced forwarding

```
RemoteForward 127.0.0.1:remotetarget 127.0.0.1:localsrc
GatewayPorts yes
```

### X11 forwarding

```
ForwardX11 yes
ForwardX11Trusted yes
```

* Many application need trusted (same as `-Y`) but beware of security implications (e.g., keylogging)
* Without trusted, there is a timeout (default 20 min), after which X11 will stop working.  Disable with

        ForwardX11Timeout 0



## Workstations

* If you have a linux workstation, and forget its name, just use `username.lin` (.flatironinstitute.org)


## VPN

* If you have a *Foundation-owned* Mac laptop, it should have the FI VPN pre-configured (if not, contact IT)
* VPN is not available on Linux laptops or self-managed machines
