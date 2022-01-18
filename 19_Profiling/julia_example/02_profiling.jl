# This example is modified version of the array access example
# https://julia-doc.readthedocs.io/en/latest/manual/performance-tips/
using Profile
using PProf

function add_no_prealloc(x::Vector{Float64})
    x_new = zeros(Float64, length(x))
    x_new .+= 3
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

    @time (
        for i = 1:1e7
            add_no_prealloc(x)
        end
    )

    @time (
        for i = 1:1e7
            add_prealloc!(x)
        end
    )

    # Profile and collect data
    Profile.clear()
    @profile (
        for i = 1:1e7
            add_no_prealloc(x)
        end
    )
    Profile.print(format = :tree, maxdepth = 12)

    # Visualize Results with PProf
    # See http://localhost:57599
    pprof()
    sleep(60) # Make longer to tinker with PProf longer
end

main()