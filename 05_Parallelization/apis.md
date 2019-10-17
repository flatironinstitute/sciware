# Parallel and Distributed Computing

## Abstractions and Libraries

A very quick preview of some ways to implement parallelism



## Building on example

* How much coordination/communication do you need?


### Very little

* Example was sufficient, just want to scale up
* Large parameter space
* Same operations on many input files
* Don't need to run concurrently

# disBatch

```
#DISBATCH REPEAT 1000 RANK=$DISBATCH_REPEAT_INDEX subdivideCheck.py
```

## slurm job arrays

```
#SBATCH --array=1-1000
RANK=$SLURM_ARRAY_TASK_ID subdivideCheck.py
```


### Quite a lot

* Need to synchronize with other ranks
* Need to share intermediate values between ranks

# MPI

```C
MPI_Init(&argc, &argv);
MPI_Comm_rank(MPI_COMM_WORLD, &rank);
MPI_Comm_size(MPI_COMM_WORLD, &ranks);
...
float myvalue = ...;
float allvalues[ranks];
MPI_Allgather(&myvalue, 1, MPI_FLOAT, allvalues, 1, MPI_FLOAT, MPI_COMM_WORLD);
...
MPI_Finalize();
```


## Parallel loops

* Some languages provide features to run loops in parallel

### OpenMP threads (C)

```C
#pragma omp parallel for
for (i=0; i<100000; i++) {
    ...
}
```

### MATLAB

```matlab
parfor i=1:100000
   ...
end
```



## Worker pools

* Single stream of main execution
* Assign calculation out to a pool of workers
* Input and output for sub-calculations must be sent over network
* Many languages have libraries that provide similar functionality
   * python asyncio, dask, tensorflow, ...
   * MATLAB, Julia
   * C OpenMP (threads only), MPI, ... (requires marshalling)
   * KVS (disBatch)
   * ...


## Futures

* A common abstraction for "worker pools"
* Given a *pure* function
   * All inputs passed as arguments (some implementation allow exceptions)
   * All results returned
   * No access to global data/state
* Request that this function be applied to some arguments in parallel ("asynchronously")
* Operations on a future (result)
   * Check if it's done
   * Wait for one (or more) futures to complete
   * Pass as input to another future evaluation (chaining)


### Common uses of Futures

* parfor
* parallel map: apply same function to list values, in parallel

```
for i in 1..10000
    y[i] = f(x[i])
```

```
for i in 1..10000
    yf[i] = Future(f, x[i])
y = Wait(yf)
```


### Example

```python
if 1 == randint(0, 3):
    x = lower
    while x < upper:
        z = findZero(func, x, min(x+step, upper), eps)
        if z is not None: print(z)
        x += step
```

Convert parallel part into pure function

```python
def piece(lower, upper, func, step, eps):
    x = lower
    while x < upper:
        z = findZero(func, x, min(x+step, upper), eps)
        if z is not None: print(z)
        x += step

if 1 == randint(0, 3):
    piece(lower, upper, func, step, eps)
```

Use worker pool to submit work

```python
client = distributed.Client()

if 1 == randint(0, 3):
    client.submit(piece, lower, upper, func, step, eps)
```


Return values, collect results

```python
def piece(lower, upper, func, step, eps):
    r = []
    x = lower
    while x < upper:
        z = findZero(func, x, min(x+step, upper), eps)
        if z is not None:
            print(z)
            r.append(z)
        x += step
    return r

def concat(a, b):
    return a + b
```

```python
def subdivideCheck(client, lower, upper, func, step, eps):
    if (upper - lower) > 1:
        mid = (upper + lower)/2.
        rl = subdivideCheck(client, lower, mid, func, step, eps)
        rr = subdivideCheck(client, mid, upper, func, step, eps)
        return client.submit(concat, rl, rr)
    else:
        if 1 == randint(0, 3):
            return client.submit(piece, lower, upper, func, step, eps)
        else:
            return []

r = subdivideCheck(client, ...)
print(client.gather(r))
```


## Results

* Full example: [subdivideCheckDist.py](subdivideCheckDist.py)
* Performance runtime

| Parallelism | Sequential | Rank | Pool |
| -----------:| ----------:| ----:| ----:|
| 1           |       4:54 | 4:54 | 5:04 |
| 2           |            | 2:31 | 2:37 |
| 4           |            | 1:27 | 1:31 |
| 8           |            | 0:44 | 0:46 |
| 16          |            | 0:26 | 0:28 |

* Output is out of order (but not pool result list) -- why?
* Pool overhead is greatest for pool size 1 -- why?
* Decreasing marginal improvement -- why?



# Hands-on

* Run the example code
* Identify latent parallelism in your own code
* Convert your own code to use rank-based parallelism or a worker pool
