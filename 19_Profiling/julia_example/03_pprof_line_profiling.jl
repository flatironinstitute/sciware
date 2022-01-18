using CSV, DataFrames
using Profile
using PProf
using LinearAlgebra



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
    df = CSV.read("data/noisy_data.csv", DataFrame)

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
    # _generate_data()

    # Profile and collect data
    Profile.clear()
    @profile analyze_data()
    Profile.print(format = :tree, maxdepth = 13)

    # Visualize Results with PProf see http://localhost:57599
    pprof()
    sleep(60) # Make longer to tinker with PProf longer
end

main()