all: run_array run_map

map_ARGS=-DUSE_UNORDERED_MAP=1

run_%: main.cc
	g++ $($*_ARGS) -g -pg -Wall -o $@ $<

gmon_%: run_%
	GMON_OUT_PREFIX=gmon ./$< & \
	pid=$$! ; \
	wait && mv gmon.$$pid $@

gprof_%: gmon_%
	gprof run_$* $< > $@

.SECONDARY:
