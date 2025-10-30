# Common libraries that we will need
using Revise;
using Plots;
using LaTeXStrings;
using LinearAlgebra;
using StaticArrays;
using Random;
using Chairmarks;
Random.seed!(1234);

# How many threads are we using?
Threads.nthreads()

# This will become very important later!
BLAS.set_num_threads(1)

# We will be creating a matrix of data...
Nbins = 8
Nreplicates = 3
# Actual data
Adata = rand(0:1, Nreplicates, Nbins)

################################
# Serial
################################
# Loop over each replicate and over each row in the replicate (but order may matter...)
function MatrixSum_Serial_Slow(A::AbstractMatrix{T}) where T
    B = zeros(Int, 1, size(A, 2));
    for irow in axes(A, 1) # row
        for jcolumn in axes(A, 2) # column
            # Result just has a single "row"
            B[jcolumn] += A[irow, jcolumn];
        end
    end
    return B;
end
# "Correct" column-ordered loop
function MatrixSum_Serial_Fast(A::AbstractMatrix{T}) where T
    B = zeros(Int, 1, size(A, 2));
    for jcolumn in axes(A, 2) # column
        for irow in axes(A, 1) # row
            # Result just has a single "row"
            B[jcolumn] += A[irow, jcolumn];
        end
    end
    return B;
end

# How does the serial portion perform?
MatrixSum_Serial_Slow(Adata)
@b MatrixSum_Serial_Slow($Adata)

# Do this on a larger matrix
Nbins = 20_000;
Nreplicates = 20_000;
Adata = rand(0:1, Nreplicates, Nbins);
# Row-ordered loop
@b MatrixSum_Serial_Slow($Adata)
# Compare to the column-ordered loop
@b MatrixSum_Serial_Fast($Adata)

################################
# Parallel -- Threads
################################
using Base.Threads
# We will now use threads to split up our work, and always build the array when we need it
# to return (this applies to a specific section in a few moments)

# This has what is called a 'race condition' and will fail to give the correct result
function MatrixSum_ParallelRace_Slow(A::AbstractMatrix{T}) where T
    B = zeros(Int, 1, size(A, 2));
    Threads.@threads for irow in axes(A, 1) # row
        for jcolumn in axes(A, 2) # column
            ### This is the problem line for the race condition...
            B[jcolumn] += A[irow, jcolumn];
            ### due to multiple threads reading from and writing to the same location in memory!
        end
    end
    return B;
end
# Do this a couple of times and we can see that we come up with different answers
MatrixSum_ParallelRace_Slow(Adata)
MatrixSum_ParallelRace_Slow(Adata)
MatrixSum_ParallelRace_Slow(Adata)

# We can actually fix this trivially by swapping the order of row/column for the loop
function MatrixSum_Parallel_Fast(A::AbstractMatrix{T}) where T
    B = zeros(Int, 1, size(A, 2));
    Threads.@threads for jcolumn in axes(A, 2) # column
        for irow in axes(A, 1) # row
            ### The operation now stays inside of the same 'j'
            B[jcolumn] += A[irow, jcolumn];
        end
    end
    return B;
end
MatrixSum_Parallel_Fast(Adata)

# Let's compare our parallel and serial versions
@b MatrixSum_Serial_Fast($Adata)
@b MatrixSum_Parallel_Fast($Adata)
# This is sometimes called 'data partitioning' or 'domain decomposition', you don't need synchronization of any kind

################################
# Parallel -- Threads with synchronization
################################
# Instead of the previous example where we knew the bin index for sorting, what if we had N particles that we were
# sorting into the different bins, and had no idea of the bin index, but had to determine it?
Nparticles = 40_000_000;
Xmax = Float64(1000);
Nbins = 100;

Xpart = Float64.(rand(1:Xmax, Nparticles));

function Histogram1D_Serial(Avec::AbstractVector{T}, Nbins::Int, Xmax::T) where T
    Counts = zeros(Int, Nbins);
    for idx in eachindex(Avec)
        # Find the bin index (some magic to do floating/integer math)
        bin_index = Int64(div((Avec[idx] - 1) * Nbins, Xmax) + 1);
        # Increment the count
        Counts[bin_index] += 1;
    end
    return Counts;
end
# Results, and timing
H1DS = Histogram1D_Serial(Xpart, Nbins, Xmax)
@b Histogram1D_Serial($Xpart, $Nbins, $Xmax)

# Here we can "lock" the data containing location (global scale lock)
function Histogram1D_ParallelLockGlobal(Avec::AbstractVector{T}, Nbins::Int, Xmax::T) where T
    Counts = zeros(Int, Nbins);
    my_lock = ReentrantLock();

    Threads.@threads for idx in eachindex(Avec)
        # Finding the bin index is still independent
        bin_index = Int64(div((Avec[idx] - 1) * Nbins, Xmax) + 1);
        # Lock and increment the bin count
        lock(my_lock) do
            Counts[bin_index] += 1;
        end
    end
    return Counts;
end
# Warning: This will take forever to run, hence only using 40k particles
H1DPLG = Histogram1D_ParallelLockGlobal(Xpart, Nbins, Xmax)
# Compare the timings of the serial and parallellock versions
@b Histogram1D_ParallelLockGlobal($Xpart, $Nbins, $Xmax)

# We could change it so that each bin had its own lock instead
function Histogram1D_ParallelLockBin(Avec::AbstractVector{T}, Nbins::Int, Xmax::T) where T
    Counts = zeros(Int, Nbins);
    # Create a lock for each bin
    locks = [ReentrantLock() for _ in 1:Nbins];

    Threads.@threads for idx in eachindex(Avec)
        # Finding the bin index is still independent
        bin_index = Int64(div((Avec[idx] - 1) * Nbins, Xmax) + 1);
        # Lock and increment the bin count
        lock(locks[bin_index]) do
            Counts[bin_index] += 1;
        end
    end
    return Counts;
end
H1DPLB = Histogram1D_ParallelLockBin(Xpart, Nbins, Xmax)
@b Histogram1D_ParallelLockBin($Xpart, $Nbins, $Xmax)

################################
# Parallel -- Threads with reduction
################################
# This is the most complicated version, as we are going to partition our data and then reduce the answer, in
# some ways similar to what we were doing for the trivial example.
function Histogram1D_ParallelReduce(Avec::AbstractVector{T}, Nbins::Int, Xmax::T) where T
    Counts = zeros(Int64, Nbins);
    nthreads = Threads.nthreads();
    # Thread-local storage for each histogram
    CountsBuffer = [zeros(Int64, Nbins) for _ in 1:nthreads];

    # Manually partition the data
    N = length(Avec);
    # Loop over the threads, rather than the data, and each one will grab its own partition
    Threads.@threads for tid in 1:nthreads
        start_idx = div((tid - 1) * N, nthreads) + 1
        end_idx   = div(tid * N, nthreads)
        count_local = CountsBuffer[tid];

        for idx in start_idx:end_idx
            bin_index = Int64(div((Avec[idx] - 1) * Nbins, Xmax) + 1);
            count_local[bin_index] += 1;
        end
    end

    # Reduce all of the buffers serially
    for count_local in CountsBuffer
        Counts .+= count_local;
    end
    return Counts;
end
H1DPR = Histogram1D_ParallelReduce(Xpart, Nbins, Xmax)
@b Histogram1D_ParallelReduce($Xpart, $Nbins, $Xmax)

# Sanity check -- make sure all of the arrays are equal to the serial version as the truth
@assert H1DS == H1DPLG
@assert H1DS == H1DPLB
@assert H1DS == H1DPR

# Show all of the timings back to back
@b Histogram1D_Serial($Xpart, $Nbins, $Xmax)
@b Histogram1D_ParallelLockGlobal($Xpart, $Nbins, $Xmax)
@b Histogram1D_ParallelLockBin($Xpart, $Nbins, $Xmax)
@b Histogram1D_ParallelReduce($Xpart, $Nbins, $Xmax)

# Do this on a larger number of particles to actually show off the threading
Nparticles = 400_000_000;
Xmax = 1000;
Nbins = 100;
Xpart = rand(1:Xmax, Nparticles);
@b Histogram1D_Serial($Xpart, $Nbins, $Xmax)
@b Histogram1D_ParallelReduce($Xpart, $Nbins, $Xmax)

################################
# Disaster time with BLAS
################################
### NOTE: We need to do this on a linux box to actually see something!!!!
### Breaks with MKL (in theory)
using LinearAlgebra
using Base.Threads
using Chairmarks

function DotProductSum_Parallel(A::Matrix{Float64}, B::Matrix{Float64})
    N = size(A, 2)
    results = zeros(Float64, N)

    Threads.@threads for j in 1:N
        results[j] = dot(view(A, :, j), view(B, :, j))
    end

    return sum(results)
end

# Create two big matrices
N = 10_000
A = randn(N, N)
B = randn(N, N)

# BLAS single-thread
BLAS.set_num_threads(1)
println("BLAS threads = 1")
@b DotProductSum_Parallel($A, $B)

# BLAS multi-thread
BLAS.set_num_threads(Threads.nthreads())
println("BLAS threads = ", Threads.nthreads())
@b DotProductSum_Parallel($A, $B)
