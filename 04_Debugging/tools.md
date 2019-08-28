# Debugging

### Language-agnostic ways to figure out what your code is doing



# System tools

Let's analyze some running [processes](examples)


## dstat (or vmstat)

`dstat -nvl 5`


## ps

`ps fuxS`


## top and htop

`htop -u $USER`


## lsof (or proc)

`lsof -p PID`

`/proc/PID/fdinfo`


## strace


## watch



## Print statements

- Be careful of buffering
- Make sure to flush! (`fflush(stdout)`, `print(..., flush=True)`)
- `python -u` (`PYTHONUNBUFFERED=1`)



## Core dumps

`ulimit -c unlimited`

`/tmp/core.*`

