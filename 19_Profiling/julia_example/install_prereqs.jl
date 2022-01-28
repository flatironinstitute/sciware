using Pkg

println("Adding packages FileIO, FlameGraphs, BenchmarkTools, and PProf")
println("This may take a minute!\n")
Pkg.add(["PProf", "FileIO", "FlameGraphs", "BenchmarkTools"])