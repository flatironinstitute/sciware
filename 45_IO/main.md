# Sciware

## Data Storage and I/O Challenges

https://sciware.flatironinstitute.org/45_IO

https://github.com/flatironinstitute/sciware/tree/main/45_IO


## Today's Agenda

- ceph in-depth
- I/O anti-patterns
- dicussion



## I/O anti-patterns

- Various I/O patterns we've observed in the wild
- Example strace output

```python
p = Path("file.txt")
if p.exists():
  with open(p, 'r') as f:
    x = f.readline()
```

```c
newfstatat(AT_FDCWD, "file.txt", {st_mode=S_IFREG|0644, st_size=2, ...}, 0) = 0
openat(AT_FDCWD, "file.txt", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=2, ...}) = 0
ioctl(3, TCGETS, 0x7fffffffdd40)        = -1 ENOTTY (Inappropriate ioctl for device)
brk(0x555555a61000)                     = 0x555555a61000
lseek(3, 0, SEEK_CUR)                   = 0
ioctl(3, TCGETS, 0x7fffffffdb60)        = -1 ENOTTY (Inappropriate ioctl for device)
read(3, "0\n", 8192)                    = 2
close(3)                                = 0
```


## Small (unbuffered) text writes

```c
write(57, "3068356 4.586100000e+01\n", 24) = 24
write(57, "3068357 4.436139000e+01\n", 24) = 24
write(57, "3068358 4.858434000e+01\n", 24) = 24
write(57, "3068359 0.000000000e+00\n", 24) = 24
write(57, "3068360 0.000000000e+00\n", 24) = 24
write(57, "3068361 0.000000000e+00\n", 24) = 24
```

- Each write requires a round-trip to the file-system
- Common culprits: flush, `python -u` (`PYTHONUNBUFFERED=1`), `std::endl`
- Example test of 1M lines (~7MB):
   - without flushing: 1.04s
   - with flushing: 73.57s


## Numeric tabular text files in general

- Much larger than binary equivalents
- More CPU time converting to text
- Example test of 1M items:
   - `numpy.save`: 0.86s
   - `numpy.savetxt`: 4.99s


## Repeated opens of same file

```c
openat(AT_FDCWD, "file.dat", O_RDONLY) = 4
lseek(4, 394092, SEEK_CUR) = 0
read(4, "...", 32, 0) = 32
close(4)                   = 0
openat(AT_FDCWD, "file.dat", O_RDONLY) = 4
lseek(4, 353022, SEEK_CUR) = 0
read(4, "...", 32, 0) = 32
close(4)                   = 0
openat(AT_FDCWD, "file.dat", O_RDONLY) = 4
lseek(4, 234464, SEEK_CUR) = 0
read(4, "...", 32, 0) = 32
close(4)                   = 0
```

- Leave files open
- `open` takes about 10x longer than `read`


## Many opens, small reads

```c
openat(AT_FDCWD, "file0047.dat", O_RDONLY) = 4
read(4, "...", 32, 0) = 32
close(4)                   = 0
openat(AT_FDCWD, "file0048.dat", O_RDONLY) = 4
read(4, "...", 32, 0) = 32
close(4)                   = 0
openat(AT_FDCWD, "file0049.dat", O_RDONLY) = 4
read(4, "...", 32, 0) = 32
close(4)                   = 0
```

- Restructure data into fewer files


## Unnecessary file locking

```c
openat(AT_FDCWD, "file0047.hdf5", O_RDONLY) = 54
fstat(54, {st_mode=S_IFREG|0600, st_size=2627776, ...}) = 0
flock(54, LOCK_SH|LOCK_NB) = 0
read(54, "\211HDF\r\n\32\n", 8, 0) = 8
lstat("file0047.hdf5", {st_mode=S_IFREG|0600, st_size=2627776, ...}) = 0
close(54)                  = 0
openat(AT_FDCWD, "file0151.hdf5", O_RDONLY) = 54
fstat(54, {st_mode=S_IFREG|0600, st_size=2627776, ...}) = 0
flock(54, LOCK_SH|LOCK_NB) = 0
pread64(54, "\211HDF\r\n\32\n", 8, 0) = 8
lstat("file0151.hdf5", {st_mode=S_IFREG|0600, st_size=2627776, ...}) = 0
close(54)                  = 0
```

- Locks are very slow...


## Unnecessary file locking

```c
openat(AT_FDCWD, "file0047.hdf5", O_RDONLY) = 54 <0.002495>
fstat(54, {st_mode=S_IFREG|0600, st_size=2627776, ...}) = 0 <0.000263>
flock(54, LOCK_SH|LOCK_NB) = 0 <0.831976>
read(54, "\211HDF\r\n\32\n", 8, 0) = 8 <0.000248>
lstat("file0047.hdf5", {st_mode=S_IFREG|0600, st_size=2627776, ...}) = 0 <0.002801>
close(54)                  = 0 <0.000353>
openat(AT_FDCWD, "file0151.hdf5", O_RDONLY) = 54 <0.001183>
fstat(54, {st_mode=S_IFREG|0600, st_size=2627776, ...}) = 0 <0.000230>
flock(54, LOCK_SH|LOCK_NB) = 0 <0.820609>
pread64(54, "\211HDF\r\n\32\n", 8, 0) = 8 <0.000275>
lstat("file0151.hdf5", {st_mode=S_IFREG|0600, st_size=2627776, ...}) = 0 <0.002651>
close(54)                  = 0 <0.000095>
```

- Locks are very slow... almost 1s each!


## Using the filesystem as a database

```c
newfstatat(AT_FDCWD, "file0040, {st_mode=S_IFREG|0600, st_size=0, ...}) = 0
newfstatat(AT_FDCWD, "file0124, {st_mode=S_IFREG|0600, st_size=0, ...}) = 0
newfstatat(AT_FDCWD, "file0493, {st_mode=S_IFREG|0600, st_size=0, ...}) = 0
newfstatat(AT_FDCWD, "file0242", 0x7fffffff87c0, 0) = -1 ENOENT
openat(AT_FDCWD, "file0242", O_WRONLY|O_CREAT|O_EXCL|O_CLOEXEC, 0644) = 6
close(6)
newfstatat(AT_FDCWD, "file0384, {st_mode=S_IFREG|0600, st_size=0, ...}) = 0
```


## Compressed files

- `npz` or other compressed files, read often
- decompression takes more (CPU) time than reading


## Pro patterns

- hdf5: flexible, fairly efficient on IO
  - at least in some use cases...
  - parallel (mpi-enabled hdf5) often harmful, multi-node contention, `cephtweaks` is an option
- Other options...
