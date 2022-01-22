using CSV, DataFrames
using Profile
using PProf
using LinearAlgebra
using FileIO



# Not intended for learners to use, but here for transparency
function _generate_data()
    p = [-1, 2.5]

    x = LinRange(0, 1, 100)
    y = p[1] * sin.(x) + p[2] * x .^ 2 .+ rand(100) .* 0.001

    df = DataFrame(X = x, Y = y)
    CSV.write("./data/noisy_data.csv", df)
end


function analyze_data()
    # Read in data
    df = CSV.read("data/noisy_data.csv", DataFrame; types = [Float64, Float64])

    # Shorthands
    x = Vector{Float64}(df[!, "X"])
    y = Vector{Float64}(df[!, "Y"])

    # Setup X for solving
    X = zeros(Float64, (length(x), 2))
    X[:, 1] = sin.(x)
    X[:, 2] = x .^ 2

    # Solve  Xβ=y
    β = X \ y
    println(β)
end


function main()
    # Unused in this example, but here for transparency
    # _generate_data()

    # Uncomment to see if the profile data changes
    # @time analyze_data() 

    # Profile and collect data
    Profile.clear()
    @profile analyze_data()
    Profile.print(format = :tree, maxdepth = 9)

    # Save the data for later
    save("_03_profile_data.jlprof", Profile.retrieve()...)

    # Open julia REPL and visualize the data with pprof

    # using PProf, FlameGraphs, FileIO
    # julia> data = load("_03_profile_data.jlprof")
    # julia> g = flamegraph(data[1]; lidict=data[2])
    # julia> pprof(g)
end

main()