all: run_array run_map
gprof: gprof_array gprof_map

map_ARGS=-DUSE_UNORDERED_MAP=1

run_%: main.cc
	g++ $($*_ARGS) -g -pg -Wall -o $@ $<

gmon_%: run_%
	GMON_OUT_PREFIX=$@ time ./$<
	mv $@.* $@

gprof_%: gmon_%
	gprof run_$* $< > $@

clean:
	rm -f run_* gmon_* gprof_* gmon.out

.SECONDARY:
