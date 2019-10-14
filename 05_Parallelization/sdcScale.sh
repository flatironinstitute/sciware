
for n in 1 2 4 8
do
    t0=$(date +%s)
    for x in $(seq 0 $(( n - 1 )) )
    do
	RANK=$x RANKS=$n python3 subdivideCheckPar.py &
    done
    wait
    echo $n $(( $(date +%s) - t0 ))
done
