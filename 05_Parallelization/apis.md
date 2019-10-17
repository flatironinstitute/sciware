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
   * All inputs passed as arguments\*
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
(subdivideCheck loop ...):
    if 1 == randint(0, 3):
        x = lower
        while x < upper:
            z = findZero(func, x, min(x+step, upper), eps)
            if z is not None: print(z)
            x += step
```

#### Convert parallel part into pure function

```python
def piece(lower, upper, func, step, eps):
    x = lower
    while x < upper:
        z = findZero(func, x, min(x+step, upper), eps)
        if z is not None: print(z)
        x += step

(subdivideCheck loop ...):
    if 1 == randint(0, 3):
        piece(lower, upper, func, step, eps)
```


```python
(subdivideCheck loop ...):
    if 1 == randint(0, 3):
        piece(lower, upper, func, step, eps)
```

#### Use worker pool (`client`) to submit work

```python
from dask import distributed
client = distributed.Client()

(subdivideCheck loop ...):
    if 1 == randint(0, 3):
        client.submit(piece, lower, upper, func, step, eps)
```


#### Return list of zeros

```python
def pieceWithResults(lower, upper, func, step, eps):
    r = []
    x = lower
    while x < upper:
        z = findZero(func, x, min(x+step, upper), eps)
        if z is not None:
            print(z)
            r.append(z)
        x += step
    return r
```


```python
def subdivideCheck(lower, upper, func, step, eps):
    if (upper - lower) <= 1:
        if 1 == randint(0, 3):
            client.submit(piece, lower, upper, func, step, eps)
    else:
        mid = (upper + lower)/2.
        subdivideCheck(lower, mid, func, step, eps)
        subdivideCheck(mid, upper, func, step, eps)
```

#### Merge results

```python
def subdivideCheck(client, lower, upper, func, step, eps):
    if (upper - lower) <= 1:
        if 1 == randint(0, 3):
            return client.submit(pieceWithResults, lower, upper, func, step, eps)
        else: return []
    else:
        mid = (upper + lower)/2.
        rl = subdivideCheck(client, lower, mid, func, step, eps)
        rr = subdivideCheck(client, mid, upper, func, step, eps)
        return ??? rl + rr ???
```


#### Use another pure function to combine results

```python
def concat(a, b):
    return a + b

def subdivideCheck(client, lower, upper, func, step, eps):
    if (upper - lower) <= 1:
        if 1 == randint(0, 3):
            return client.submit(pieceWithResults, lower, upper, func, step, eps)
        else: return []
    else:
        mid = (upper + lower)/2.
        rl = subdivideCheck(client, lower, mid, func, step, eps)
        rr = subdivideCheck(client, mid, upper, func, step, eps)
        return client.submit(concat, rl, rr)

r = subdivideCheck(client, ...)
print(client.gather(r))
```


### Performance (runtime)

| Parallelism | Sequential | Rank | Pool |
| (cores) | (runtime)
| -----------:| ----------:| ----:| ----:|
| 1           |       4:34 | 4:34 | 4:39 |
| 2           |            | 2:22 | 2:24 |
| 4           |            | 1:15 | 1:16 |
| 8           |            | 0:39 | 0:39 |
| 16          |            | 0:23 | 0:23 |
| 32          |            | 0:17 | 0:17 |

* Output is out of order (but not pool result list) -- why?
* Pool 1 is slower (but not 32) -- why?
* Decreasing marginal improvement -- why?



# Hands-on

* Run the example code
* Identify latent parallelism in your own code
* Convert your own code to use rank-based parallelism or a worker pool
