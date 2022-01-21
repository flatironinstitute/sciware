#!/bin/bash

PIDS=()
python ./simulation.py &
PIDS[0]=$!
#echo "${PIDS[0]}"
python ./simulation.py &
PIDS[1]=$!
#echo "${PIDS[1]}"
python ./simulation.py &
PIDS[2]=$!
#echo "${PIDS[2]}"
echo "All pids: ${PIDS[@]}"
while [ ${#PIDS[@]} -ne 0 ]; do
  for IDX in ${!PIDS[@]}; do
    PID=${PIDS[$IDX]}
    if [ ! -d "/proc/$PID" ]; then
      wait $PID
      echo "$PID terminated with code $?"
      unset PIDS[$IDX]
    fi
  done
  sleep 2
done

echo "Run complete"
