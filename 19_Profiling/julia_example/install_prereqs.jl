using Pkg

println("Adding packages CSV, DataFrames, FileIO, FlameGraphs, and PProf")
println("This may take a minute!\n")
Pkg.add(["CSV", "DataFrames", "PProf", "FileIO", "FlameGraphs"])