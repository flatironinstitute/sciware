# This example is modified version of the array access example
# https://julia-doc.readthedocs.io/en/latest/manual/performance-tips/
using Profile
using BenchmarkTools

function add_no_prealloc(x::Vector{Float64})
    x_new = x .+ 3.0
    return x_new
end

function add_prealloc!(x::Vector{Float64})
    x .+= 3
    nothing
end

#
# Main
#
function main()
    x = zeros(10)

    println("Adding a number to a small vector (and copying the vector)")
    @btime add_no_prealloc($x)

    println("Adding a number to a small vector (modifying the original)")
    @btime add_prealloc!($x)

    println("\nShowing the profiling info")
    # Profile and collect data
    @profile (
        for i = 1:1e7
            add_no_prealloc(x)
            add_prealloc!(x)
        end
    )
    Profile.print(format = :tree, maxdepth = 9)

end

main()