# Parallel and Distributed Computing

## Terminology


## Parallel Computing

<img src="parallel.svg">

* Running multiple computations on the same computer at the same time


## Distributed Computing

<img src="distributed.svg">

* Running a computation across multiple, networked computers at the same time


## Parallel and Distributed Computing

<img src="pardist.svg">



# Parallel computing

### Different ways to run things in parallel


## Instruction pipelining

* Completely transparent (invisible) parallelism
* The processor may process operations in parallel
* Interleave steps: fetch input, execute, write output
* `(a+b)*(c+d)` (add, add, multiply)
* Possibly "speculatively" (before it knows they will happen, in case they do)


## Data parallelism: SIMD

* Special instructions that operate on multiple values simultaneously
* Instruction-level "vectorization"
* MMX, SSE, AVX
* Sometimes inferred by the compiler from loops
* Hand-written assembly, special functions, math libraries
* Single instruction, multiple data


## Task parallelism

* Multiple processing units ("cores") in the same computer
* Explicitly run multiple pieces of code (same or different) in parallel
* Code runs independently, may run at different speeds
* Draws on single set of resources (memory, network)


### Threads

* Parallel execution sharing resources in a single process
* (Global) variables, open files, global state: all shared
* Easy to read the same data
* Hard to write to the same data
* Simple functions allow synchronization (lock/mutex)


### Multi-threaded libraries

* Some libraries turn single function calls into multi-threaded calculations
* Don't require any explicit code changes
* Consider interaction with explicit parallelism (usage multiplies!)


### Processes

* Parallel execution in separate resource spaces
* Separate copies of all data
* Exceptions: same filesystems, "shared" memory
* Need to explicitly communicate (send messages) to coordinate




# Distributed computing

* Similar to process-level parallelization, but separate hardware
* Must communicate over network
* Sometimes shared filesystems...


### HPC: High Performance Computing

* Tightly-coupled execution, often running the same code
* Run more at once than fits on a single machine (more memory, calculations)
* Share intermediate results throughout computation

### HTC: High Throughput Computing

* Running many independent (though often parallel) computations
* Collect and store many results across a number of inputs, parameters



# General approaches

### Multiple instances

* Divide up work among themselves
* Work together in flat structure
* Coordinate/communicate to share intermediate values

### Worker pool

* Run one main process
* Hand off pieces of work to a pool of workers
* All coordination happens in main process
