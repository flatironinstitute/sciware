// Mockup of simple MPI and OpenMP hybrid stuff with race condition

#include <chrono>
#include <iostream>
#include <thread>

#include <mpi.h>
#include <omp.h>

int main(int argc, char *argv[]) {

    // Initialize MPI
    MPI_Init(&argc, &argv);
    auto mpicomm = MPI_COMM_WORLD;

    // Get MPI information
    int mpisize;
    int mpirank;
    MPI_Comm_size(mpicomm, &mpisize);
    MPI_Comm_rank(mpicomm, &mpirank);

    // Get OpenMP information
#pragma omp parallel
    {
        int ompsize = omp_get_num_threads();
        int omprank = omp_get_thread_num();

        // Print out the information
#pragma omp critial
        {
            std::cout << "Hello from thread " << omprank << " out of " << ompsize << " from process " << mpirank << " out of " << mpisize <<std::endl;
        }
    }

    // Clean up
    MPI_Barrier(mpicomm);
    MPI_Finalize();
    return 0;
}
