#!/bin/sh -e
run() {
	echo "$@"
	"$@"
}

CXX=g++
CXXFLAGS="-g -pg -Wall -std=c++20 -fopenmp"
run $CXX $CXXFLAGS                       -o run_array main.cc
run $CXX $CXXFLAGS -DUSE_UNORDERED_MAP=1 -o run_map   main.cc

echo

GMON_OUT_PREFIX=gmon_array run \time ./run_array
mv gmon_array.* gmon_array
echo
GMON_OUT_PREFIX=gmon_map   run \time ./run_map
mv gmon_map.*   gmon_map

gprof run_array gmon_array > gprof_array.txt
gprof run_map   gmon_map   > gprof_map.txt
