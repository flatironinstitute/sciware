using Profile
using PProf
using LinearAlgebra
using FileIO

# Our big convoluted function
function complicated_func()
    # Pick parameters for our function
    # Feel free to change these!
    p = [0.1, -0.5, 0.42, -3, 0.01, -0.2]
    n = 2000000

    # Setting up our data
    x = LinRange(0, 10, n)
    y = zeros(length(x))

    for i = 1:length(p)
        y .+= p[i] * x .^ i
    end

    # Add some noise
    y .+= rand(n) * 0.01

    # Setup X for solving
    X = zeros(Float64, (length(x), length(p)))
    for i = 1:length(p)
        X[:, i] = x .^ i
    end

    # Solve  Xβ=y
    β = X \ y
    error = (β - p) / norm(p)
    # println(β)
    println("Relative error in coefficients ", error)
end


function main()
    # Profile and collect data
    Profile.init(delay = 0.0005)
    @profile complicated_func()
    Profile.print(format = :tree, maxdepth = 9)

    # Save the data for later
    save("_03_profile_data.jlprof", Profile.retrieve()...)

    # Open julia REPL and visualize the data with pprof

    # julia> using PProf, FlameGraphs, FileIO
    # julia> data = load("_03_profile_data.jlprof")
    # julia> g = flamegraph(data[1]; lidict=data[2])
    # julia> pprof(g)

    # Or all in one line
    # julia> using PProf, FlameGraphs, FileIO; data = load("_03_profile_data.jlprof"); g = flamegraph(data[1]; lidict=data[2]); pprof(g)
end

main()