using Pkg

println("Adding packages FileIO, FlameGraphs, and PProf")
println("This may take a minute!\n")
Pkg.add(["PProf", "FileIO", "FlameGraphs"])