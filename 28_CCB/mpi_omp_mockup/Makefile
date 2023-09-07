# This is a standard makefile
CXX=mpicxx
CXXFLAGS=-O2 -fopenmp

# Target
TARGET=mpi_omp_mockup

all: $(TARGET)

$(TARGET): $(TARGET).cpp
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	rm -f $(TARGET)
