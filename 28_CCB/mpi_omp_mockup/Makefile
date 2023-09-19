# This is a standard makefile
CXX=mpicxx
CXXFLAGS=-O2 -fopenmp

all: mpi_omp_mockup mpi_omp_mockup_race

mpi_omp_mockup: mpi_omp_mockup.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

mpi_omp_mockup_race: mpi_omp_mockup_race.cpp
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	rm -f mpi_omp_mockup mpi_omp_mockup_race
