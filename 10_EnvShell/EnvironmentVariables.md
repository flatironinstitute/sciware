# Why Environment Variables?

When you run a program that you wrote, say `myProg`, you can arrange for it to accept arguments via the command line that will alter its behavior:  
`myProg arg0 arg1 ...`  

But what if you are trying to alter the behavior of something that is running "behind the scenes" beyond the reach of command line arguments?
A library? The mechanism Linux uses to launch a program?
Compilation options deep within a build process?

One, if not *the*, mechanism to do this is via modifications to the "environment" in which a program executes. This "environment" is simply a namespace,
a collection of names and the values associated with them. Standard library functions provide a way for a program to query this namespace and thus determine the
value associated with a name, and then alter its behavior accordingly.

# Shells and the Environment

Shells provide mechanisms for users to modify the environment. For `bash` this mechanism is identical to managing
normal variables. Environment variables are distinguished by being marked for "export". Some examples (note: `env` is used here to display the environment,
but it can do more):

    [carriero@scclin001 ~]$ myVar0=000
    [carriero@scclin001 ~]$ env | grep myVar
    [carriero@scclin001 ~]$ export myVar0
    [carriero@scclin001 ~]$ env | grep myVar
    myVar0=000
    [carriero@scclin001 ~]$ export myVar1=111
    [carriero@scclin001 ~]$ env | grep myVar
    myVar1=111
    myVar0=000
    [carriero@scclin001 ~]$ myVar2=222 bash -c "env | grep myVar"
    pmyVar2=222
    myVar1=111
    myVar0=000
    [carriero@scclin001 ~]$ env | grep myVar
    myVar1=111
    myVar0=000
    [carriero@scclin001 ~]$ 

Certain names are, in effect, "reserved", that is they are dedicated for a well defined, documented use. We'll discuss a few of those
here:  

PATH  
LD_LIBRARY_PATH  
LD_PRELOAD  
PYTHONPATH  
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

To help gain a better understanding of what's going, these examples user `strace` to look at the system calls being invoked.
We use a combination of filters to reduce this to just the relevant bits.  

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

For day to day use, `which` is your friend here. `which myProg` will return the full path (if one is found) of the executable that would be
invoked if you were to have entered just `myProg`.

Ordering is significant (will stop with the first found).  
Keeping your `PATH` tidy reduces the risk of accidental collisions, and could make the shell a little more responsive (think about
how much work it has to do to find the program).  

Note that this behavior is not confined to the shell:

    [carriero@scclin001 carriero]$ echo $PATH
    /here:/there:/everywhere:/bin:/usr/bin
    [carriero@scclin001 carriero]$ strace -f -o >(grep foodle) python -c 'import os; os.execvp("foodle", ["foodle"])'
    1789869 execve("/bin/python", ["python", "-c", "import os; os.execvp(\"foodle\", ["...], [/* 18 vars */]) = 0
    1789869 execve("/here/foodle", ["foodle"], [/* 18 vars */]) = -1 ENOENT (No such file or directory)
    1789869 execve("/there/foodle", ["foodle"], [/* 18 vars */]) = -1 ENOENT (No such file or directory)
    1789869 execve("/everywhere/foodle", ["foodle"], [/* 18 vars */]) = -1 ENOENT (No such file or directory)
    1789869 execve("/bin/foodle", ["foodle"], [/* 18 vars */]) = -1 ENOENT (No such file or directory)
    1789869 execve("/usr/bin/foodle", ["foodle"], [/* 18 vars */]) = -1 ENOENT (No such file or directory)
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/usr/lib64/python2.7/os.py", line 344, in execvp
	_execvpe(file, args)
      File "/usr/lib64/python2.7/os.py", line 380, in _execvpe
	func(fullname, *argrest)
    OSError: [Errno 2] No such file or directory
    [carriero@scclin001 carriero]$


### LD_LIBRARY_PATH
This should be set to a ":" separated list of *directories*.  

List the locations to search for shared libraries when executing a program.

### LD_PRELOAD
This should be set to a ":" separated list of shared object *files*.  

Very powerful. Very dangerous. Can be used, for example, to
swap out one memory allocation scheme for another.

### PYTHONPATH
This should be set to a ":" separated list of *directories*.  

Same general idea as LD_LIBRARY_PATH, but for python modules.

    [carriero@scclin001 ~]$ python3
    Python 3.6.8 (default, Apr 25 2019, 21:02:35) 
    [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import sys
    >>> for e in sys.path:
    ...    print(e)
    ... 

    /usr/lib64/python36.zip
    /usr/lib64/python3.6
    /usr/lib64/python3.6/lib-dynload
    /mnt/home/carriero/.local/lib/python3.6/site-packages
    /usr/lib64/python3.6/site-packages
    /usr/lib/python3.6/site-packages
    >>> 
    [carriero@scclin001 ~]$ export PYTHONPATH=/here:/there:/everywhere:$PYTHONPATH
    [carriero@scclin001 ~]$ python3
    Python 3.6.8 (default, Apr 25 2019, 21:02:35) 
    [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import sys
    >>> for e in sys.path:
    ...    print(e)
    ... 

    /here
    /there
    /everywhere
    /mnt/home/carriero
    /usr/lib64/python36.zip
    /usr/lib64/python3.6
    /usr/lib64/python3.6/lib-dynload
    /mnt/home/carriero/.local/lib/python3.6/site-packages
    /usr/lib64/python3.6/site-packages
    /usr/lib/python3.6/site-packages
    >>> 
    [carriero@scclin001 ~]$ 

## Control how programs behave
### OMP_NUM_THREADS
This is set to an integer to control the number of threads that will be used by an OMP-enabled application.

### TMPDIR
This should be set to a directory where temporary/scratch files should be written.  
Not all (even many) codes use this, but if they do, using this to
write temp files to a local storage area, rather than a shared file system, can have a big impact on the performance of your code.

### HOME
This should be set to a directory.  

Some installers do not offer an easy way to specify the target of an installation and simply put the install in a subdirectory of
your home directory. Other programs just assume they can leave behind config
and status files in your home directory, even if you don't want them to. In cases where this matters a great deal, you can try:  

    HOME=/my/install/target installer ...
    
Most would consider this to be a hack, but on occasion it is a very useful one. Use sparingly and test the results carefully.

## Control build process
### CPATH
This should be set to a ":" separated list of *directories*.  
Somewhat like `PATH`, this provides a list of locations to search for C include files.

### LIBRARY_PATH
This should be set to a ":" separated list of *directories*.  
A list of locations to search for `libxyz` when linking a program with `-lxyz`.

These are especially helpful when working with a complex source build that does you the "favor" of hiding most of the build steps, but isn't smart
enough to handle libraries in non-standard locations.  Check the GNU compiler documentation for more of these. Also note the subtle distinction
between `LIBRARY_PATH` and `LD_LIBRARY_PATH`.

# Conclusion
This is by no means an exhaustive list. The main point is that environment variables are used to alter a wide variety of behaviors. Check documentation
for new ones that might be relevant for your workflow.

Not within scope: Propagation of environment across shell invocations (and impact of rc files), salloc/srun/sbatch, mpiexec, mpirun, strange idempotency of module, ...  
