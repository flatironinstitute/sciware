#!/bin/sh -e
[[ $# -gt 0 ]] || set -- .00000015 100

# Sequential run.
echo ------------------- Sequential ------------------
time (
  python3 subdivideCheck.py "$@"
)
echo End sequential

# Parallel runs with various ranks.
for n in 1 2 4 8 16
do
  echo -------------------- Ranks $n --------------------
  time (
    for x in $(seq 0 $(( n - 1 )) )
    do
      RANK=$x RANKS=$n python3 subdivideCheckPar.py "$@" &
    done
    wait
  )
done

# Parallel runs with various pool sizes.
for n in 1 2 4 8 16
do
  echo ------------------ Pool size $n ------------------
  time (
    RANKS=$n python3 subdivideCheckDist.py "$@"
  )
done
