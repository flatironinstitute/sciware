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

# Set the larger matrix size to start with
Nbins = 20_000;
Nreplicates = 20_000;
Adata = rand(0:1, Nreplicates, Nbins);

# Operate on pre-allocated memory, but still serial
function MatrixSum_Serial_Row!(B::AbstractVector{T}, A::AbstractMatrix{T}) where T
    for i in axes(A, 1) # row
        for j in axes(A, 2) # column
            B[j] += A[i, j];
        end
    end
end
function MatrixSum_Serial_Column!(B::AbstractVector{T}, A::AbstractMatrix{T}) where T
    for j in axes(A, 2) # column
        for i in axes(A, 1) # row
            B[j] += A[i, j];
        end
    end
end
# Pre-allocate the result
Bresult_row = zeros(Int64, Nbins);
Bresult_col = zeros(Int64, Nbins);
@b MatrixSum_Serial_Row!($Bresult_row, $Adata)
@b MatrixSum_Serial_Column!($Bresult_col, $Adata)

# Play around with different base types and how they interact with cache lines
Cdata = Int32.(rand(0:1, Nreplicates, Nbins));
Cresult_row = zeros(Int32, Nbins);
Cresult_column = zeros(Int32, Nbins);
@b MatrixSum_Serial_Row!($Cresult_row, $Cdata)
@b MatrixSum_Serial_Column!($Cresult_column, $Cdata)

Nparticles = 400_000_000;
Xmax = 1000;
Nbins = 100;
Xpart = rand(1:Xmax, Nparticles);
# Extra credit: we can hint that the compiler should use SIMD on the inner most loop...
function Histogram1D_ParallelReduceSIMD(Avec::AbstractVector{T}, Nbins::Int, Xmax::T) where T
    Counts = zeros(Int, Nbins);
    nthreads = Threads.nthreads();
    # Thread-local storage for each histogram
    CountsBuffer = [zeros(Int, Nbins) for _ in 1:nthreads];

    # Manually partition the data
    N = length(Avec);
    # Loop over the threads, rather than the data, and each one will grab its own partition
    Threads.@threads for tid in 1:nthreads
        start_idx = div((tid - 1) * N, nthreads) + 1
        end_idx   = div(tid * N, nthreads)
        count_local = CountsBuffer[tid];

        @inbounds @simd for idx in start_idx:end_idx
            bin_index = div((Avec[idx] - 1) * Nbins, Xmax) + 1;
            count_local[bin_index] += 1;
        end
    end

    # Reduce all of the buffers serially
    for count_local in CountsBuffer
        @inbounds Counts .+= count_local;
    end
    return Counts;
end

@b Histogram1D_Serial($Xpart, $Nbins, $Xmax)
@b Histogram1D_ParallelReduce($Xpart, $Nbins, $Xmax)
@b Histogram1D_ParallelReduceSIMD($Xpart, $Nbins, $Xmax)