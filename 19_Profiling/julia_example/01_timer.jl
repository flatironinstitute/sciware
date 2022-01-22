# This example is modified version of the array access example
# https://julia-doc.readthedocs.io/en/latest/manual/performance-tips/

#
# Copy vector to columns
#
function copy_cols(x::Vector{Float64})
    n = size(x, 1)
    out = zeros(Float64, n, n)
    for i = 1:n
        out[:, i] = x
    end
    out
end

#
# Copy vector to rows
#
function copy_rows(x::Vector{Float64})
    n = size(x, 1)
    out = zeros(Float64, n, n)
    for i = 1:n
        out[i, :] = x
    end
    out
end

#
# Run example
#
function main()
    N = Int(1e4)
    x = randn(N)

    println("Copying vector to columns")
    @time copy_cols(x)
    println("Copying vector to rows")
    @time copy_rows(x)
end

main()
