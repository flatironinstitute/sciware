#!/bin/sh -e
[[ $# -gt 0 ]] || set -- .00000015 100

# Sequential run.
time (
  python3 subdivideCheck.py "$@"
  echo Sequential
)

# Parallel runs with various ranks.
for n in 1 2 4 8
do
  time (
    for x in $(seq 0 $(( n - 1 )) )
    do
	RANK=$x RANKS=$n python3 subdivideCheckPar.py "$@" &
    done
    wait
    echo Ranks $n
  )
done
