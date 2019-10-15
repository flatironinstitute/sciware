
# Sequential run.
t0=$(date +%s)
python3 subdivideCheck.py .00000015 100
echo Sequential $(( $(date +%s) - t0 ))

# Parallel runs with various ranks.
for n in 1 2 4 8
do
    t0=$(date +%s)
    for x in $(seq 0 $(( n - 1 )) )
    do
	RANK=$x RANKS=$n python3 subdivideCheckPar.py .00000015 100 &
    done
    wait
    echo Ranks $n $(( $(date +%s) - t0 ))
done
