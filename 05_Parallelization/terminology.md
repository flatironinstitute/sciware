## Parallel and Distributed Computing Terminology

<img src="img/pardist-core1.svg" width="1000" style="border:0;box-shadow:none">

* *Parallel*: Running multiple computations (often on the same computer) at the same time
* *Distributed*: Running a calculation across multiple, networked computers
* Often used together, interchangeably, especially in HPC


### Instruction-level parallelism

<img src="img/pardist-corep.svg" width="1000" style="border:0;box-shadow:none">

* Instruction pipelining
   * Completely transparent (invisible) parallelism
   * Interleave steps, independent operations, "speculative"
* Data parallelism: SIMD (Single Instruction, Multiple Data)
   * Instructions operate on multiple values simultaneously
   * *vectorization*: MMX, SSE, AVX
   * Sometimes inferred by the compiler from loops
   * Hand-written assembly, special functions, math libraries


### Running code: *Process*

<img src="img/pardist-proc1.svg" width="1000" style="border:0;box-shadow:none">

* Everything runs in a process
* Defines global state: memory contents, open files, network connections, etc.
* Only makes use of one core by default

#### *Task parallelism*: explicitly indicate pieces of code to run concurrently


### Threads

<img src="img/pardist-thread.svg" width="1000" style="border:0;box-shadow:none">

* Parallel execution sharing resources in a single process
* (Global) variables, open files, global state: all shared
* Easy to read the same data
* Hard to write to the same data
* Functions allow synchronization (lock/mutex)


### Multi-threaded libraries

<img src="img/pardist-lthreads.svg" width="1000" style="border:0;box-shadow:none">

* Some libraries turn single function calls into multi-threaded calculations
* Don't require any explicit code changes
* Consider interaction with explicit parallelism (task count multiplies!)


### Processes

<img src="img/pardist-procs.svg" width="1000" style="border:0;box-shadow:none">

* Parallel execution in separate resource spaces
* Separate copies of all data
* Need to explicitly communicate (send messages) to coordinate
* Same filesystems, fast IPC, "shared" memory



## Distributed Computing

<img src="img/distributed.svg" width="600" style="border:0;box-shadow:none">

* Various machines working together
* Must send messages to communicate, coordinate


### HPC: High Performance Computing

<img src="img/pardist-hpc.svg" width="1000" style="border:0;box-shadow:none">

* Homogeneous cluster of machines
* Low-latency network allows fast communication
   * Shared network filesystems
   * Low-latency networks (10x slower than local memory, 100x faster than SSD)
* Makes distributed computing similar to process-level parallelism


### Distributed Processes

<img src="img/pardist-dprocs.svg" width="1000" style="border:0;box-shadow:none">

* Processes running on separate hardware
* No shared memory


### Distributed Processes

<img src="img/pardist-dprocs2.svg" width="1000" style="border:0;box-shadow:none">

### Distributed, Threaded Processes

<img src="img/pardist-dthreads.svg" width="1000" style="border:0;box-shadow:none">


### HPC: High Performance Computing

* Tightly-coupled execution, often running the same code
* Run more at once than fits on a single machine (more memory, calculations)
* Share intermediate results throughout computation

### HTC: High Throughput Computing

* Running many independent (though often parallel) computations
* Collect and store many results across a number of inputs, parameters



# General approaches

### Multiple instances ("flock"/rank parallelism)

* A number of ranks work in parallel, usually running the same code
* Divide up work among themselves
* Coordinate/communicate to share intermediate values

### Worker pool

* Run one main process
* Hand off pieces of work to a pool of workers
* Coordination happens in main process
