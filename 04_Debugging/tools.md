# Debugging: System Tools

### Language-agnostic ways to figure out what your code is doing



# Print statements

- Be careful of buffering
- Make sure to flush! (`fflush(stdout)`, `print(..., flush=True)`)
- `python -u` (`PYTHONUNBUFFERED=1`)



# Core dumps

`ulimit -c unlimited`

`/tmp/core.*`



# System tools


# dstat (or vmstat)

`dstat -nvl 5`


# ps

`ps fuxS`


# top and htop


# lsof (or proc)

`lsof -p PID`

`/proc/PID/fdinfo`


# strace
