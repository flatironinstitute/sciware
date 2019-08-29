# Debugging

### Language-agnostic ways to figure out what your code is doing



# System tools

Let's analyze some running [processes](examples)


## Overall system

- `dstat -nvl 5`
   - `vmstat 5`
   - `iostat 5`
- `nproc`
- `lscpu`


## Individual processes

- `ps fuxS`
- `htop -u $USER`
   - `top -u $USER`


## Open files per process

- `lsof -p $PID`
   - `ls -l /proc/$PID/fd`
- `cat /proc/$PID/fdinfo/$FD`


## Process activity

- `strace -p $PID`


## Other useful tools

- `watch`



## Print statements

- Be careful of buffering
- Make sure to flush! (`fflush(stdout)`, `print(..., flush=True)`)
- `python -u` (`PYTHONUNBUFFERED=1`)


## Core dumps

- `ulimit -c unlimited`
- `ls /tmp/core.*`

