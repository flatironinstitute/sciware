# Why Environment Variables?

When you run a program that you wrote, say `myProg`, you can arrange for it to accept arguments via the command line that will alter its behavior:  
`myProg arg0 arg1 ...`  

But what if you are trying to control the behavior of something that is running "behind the scenes"? A library? The mechanism Linux uses to launch a program?
Compilation options deep within a build process?

One, if not *the*, mechanism to do this is via modifications to the "environment" in which a program executes. This "environment" is simply a namespace,
a collection of names and values associated with them. Standard library functions provide a way for a program to query this namespace and thus determine the
value associated with a name.

# Shells and the Environment

Shells provide mechanisms for users to modify the environment. For `bash` this mechanism is identical to managing
normal variables. Environment variables are distinguished by being marked for "export". Some examples, note: `env` is used here to display the environment,
but it can do more:

    [carriero@scclin001 carriero]$ myVar=1234
    [carriero@scclin001 carriero]$ env | grep myVar
    [carriero@scclin001 carriero]$ export myVar
    [carriero@scclin001 carriero]$ env | grep myVar
    myVar=1234
    [carriero@scclin001 carriero]$ export myVar2=4321
    [carriero@scclin001 carriero]$ env | grep myVar
    myVar2=4321
    myVar=1234
    [carriero@scclin001 carriero]$ myVar3=5678 bash -c "env | grep myVar"
    myVar3=5678
    myVar2=4321
    myVar=1234
    [carriero@scclin001 carriero]$


Certain names are, in effect "reserved", that is they are dedicated for a well defined, documented use. We'll discuss a few of those
here:  

PATH  
LD_LIBRARY_PATH  
LD_PRELOAD  
OMP_NUM_THREADS  
HOME  
TMPDIR  
LIBRARY_PATH  
CPATH  
  
Unfortunately, "reserved" status doesn't carry any special protection. Nothing prevents you from setting one of these to a value inappropriate for it. If you do,
the impact can be very far reaching and the results very unpleasant. 

But aside from reserved names like these, you are free to use this namespace for your own purposes too. In practice, it can be difficult to determine exactly
what is "reserved", so you'll want to give your variables long names with a prefix strongly related to your program context.

# Examples of Environment Variables
## Control how programs are started
### PATH  
This should be set to a ":" separated list of *directories*.  

When, at the shell prompt, you type:  
`foo/bar/myProg`   
the underlying system call used to run the program looks for the executable in the location you specified. If, however, you type:  
`myProg`  
that library call will begin searching for the executable using the value of `PATH`.

Starting with a "vanilla" PATH:  

    [carriero@scclin001 carriero]$ echo $PATH     
    /bin:/usr/bin       
    [carriero@scclin001 carriero]$ strace -e stat -o >(grep date) bash -c date
    stat("/bin/date", {st_mode=S_IFREG|0755, st_size=62296, ...}) = 0
    stat("/bin/date", {st_mode=S_IFREG|0755, st_size=62296, ...}) = 0
    stat("/bin/date", {st_mode=S_IFREG|0755, st_size=62296, ...}) = 0
    stat("/bin/date", {st_mode=S_IFREG|0755, st_size=62296, ...}) = 0
    stat("/bin/date", {st_mode=S_IFREG|0755, st_size=62296, ...}) = 0
    stat("/bin/date", {st_mode=S_IFREG|0755, st_size=62296, ...}) = 0
    Thu Aug  6 10:34:34 EDT 2020
    [carriero@scclin001 carriero]$ strace -e stat -o >(grep foodle) bash -c foodle
    stat("/bin/foodle", 0x7ffdab36e030)     = -1 ENOENT (No such file or directory)
    stat("/usr/bin/foodle", 0x7ffdab36e030) = -1 ENOENT (No such file or directory)
    bash: foodle: command not found

Let's try searching a few other directories:  

    [carriero@scclin001 carriero]$ PATH=/here:/there:/everywhere:$PATH
    [carriero@scclin001 carriero]$ strace -e stat -o >(grep foodle) bash -c foodle
    stat("/here/foodle", 0x7ffece34e890)    = -1 ENOENT (No such file or directory)
    stat("/there/foodle", 0x7ffece34e890)   = -1 ENOENT (No such file or directory)
    stat("/everywhere/foodle", 0x7ffece34e890) = -1 ENOENT (No such file or directory)
    stat("/bin/foodle", 0x7ffece34e890)     = -1 ENOENT (No such file or directory)
    stat("/usr/bin/foodle", 0x7ffece34e890) = -1 ENOENT (No such file or directory)
    bash: foodle: command not found

I mean it this time (why is this relevant?):  

    [carriero@scclin001 carriero]$ PATH=/here:/there:/everywhere:$PATH
    [carriero@scclin001 carriero]$ strace -e stat -o >(grep foodle) bash -c foodle
    stat("/here/foodle", 0x7fff4a6edec0)    = -1 ENOENT (No such file or directory)
    stat("/there/foodle", 0x7fff4a6edec0)   = -1 ENOENT (No such file or directory)
    stat("/everywhere/foodle", 0x7fff4a6edec0) = -1 ENOENT (No such file or directory)
    stat("/here/foodle", 0x7fff4a6edec0)    = -1 ENOENT (No such file or directory)
    stat("/there/foodle", 0x7fff4a6edec0)   = -1 ENOENT (No such file or directory)
    stat("/everywhere/foodle", 0x7fff4a6edec0) = -1 ENOENT (No such file or directory)
    stat("/bin/foodle", 0x7fff4a6edec0)     = -1 ENOENT (No such file or directory)
    stat("/usr/bin/foodle", 0x7fff4a6edec0) = -1 ENOENT (No such file or directory)
    bash: foodle: command not found

A very common mistake:

    [carriero@scclin001 carriero]$ PATH=/here:/there:/everywhere
    [carriero@scclin001 carriero]$ strace -e stat -o >(grep foodle) bash -c foodle
    bash: grep: command not found
    bash: strace: command not found
    [carriero@scclin001 carriero]$


Ordering is significant (will stop with the first found).  
Keeping your `PATH` tidy reduces the risk of accidental collisions, and could make the shell a little more responsive (think about
how much work it has to do to find the program).  

### LD_LIBRARY_PATH
This should be set to a ":" separated list of *directories*.  

List the locations to search for shared libraries when executing a program.

### LD_PRELOAD
This should be set to a ":" separated list of shared object *files*. Very powerful. Very dangerous. Can be used, for example, to
swap out one memory allocation scheme for another.

## Control how programs behave
### OMP_NUM_THREADS
This is set to an integer to control the number of threads that will be used by an OMP-enabled application.

### TMPDIR
This should be set to a directory where temporary/scratch files should be written.  
Not all (even many) codes use this, but if they do, using this to
write temp files to a local storage area, rather than a shared file system, can have a big impact on the performance of your code.

### HOME
This should be set to a directory.  

Some installers do not offer an easy way to specify the target of an installation. Other programs just assume they can leave behind config
and status files in your home directory, even if you don't want them to. In cases where this matters a great deal, you can try:  

    HOME=/my/install/target installer ...
    
Most would consider this to be a hack, but on occasion it is a very useful one. Use sparingly and test the results carefully.

## Control build process
### CPATH
This should be set to a ":" separated list of *directories*.  
Somewhat like `PATH` provides a list of locations to search for C include files.

### LIBRARY_PATH
This should be set to a ":" separated list of *directories*.  
A list of locations to search for `libxyz` when linking a program with `-lxyz`.

These are especially helpful when working with a complex source build that does you the "favor" of hiding most of the build steps, but isn't smart
enough to handle libraries in non-standard locations.  Check the GNU compiler documentation for more of these. Also note the subtle distinction
between `LIBRARY_PATH` and `LD_LIBRARY_PATH`.

# Conclusion
This is by no means an exhaustive list. The main point is that environment variables are used to alter a wide variety of behaviors. Check documentation
for new ones that might be relevant for your workflow.

Not within scope: Propagation of environment across shell invocations (and impact of rc files), salloc/srun/sbatch, mpiexec, mpirun, ...  