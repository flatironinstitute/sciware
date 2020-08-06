# Why Environment Variables?

When you run a program that you wrote, say `myProg`, you can arrange for it to accept arguments via the command line that will alter its behavior:  
`myProg arg0 arg1 ...`  

But what if you are trying to control the behavior of something that is running "behind the scenes"? A library? The mechanism Linux uses to launch a program?
Compilation options deep within a build process?

One, if not *the*, mechanism to do this is via modifications to the "environment" in which a program executes. This "environment" is simply a namespace,
a collection of names and values associated with them. Standard library functions provide a way for a program to query this namespace and thus determine the
value associated with a name. 

Certain names, are, in effect "reserved", that is dedicated for a well defined, documented use. We'll discuss a few of those
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

But aside from reserved names like these, you are free to use this namespace for your own purposes too. In practice, it can be difficult to determined exactly
what is "reserved", so it if you do this, you'll want use long names with a prefix strongly related to your program context.

# Examples of Environment Variables
## Control how programs are started
PATH  
This should be set to a ":" separated list of *directories*.  
When, at the shell prompt, you type:  
`foo/bar/myProg`   
the underlying library call used to run the program looks for the executable in the location you specified. If, however, you type:  
`myProg`  
that library call will begin searching for the executable using the value of `PATH`.

Comapre:  

    [carriero@scclin001 carriero]$ PATH=/bin:/usr/bin   
    [carriero@scclin001 carriero]$ echo $PATH     
    /bin:/usr/bin              
    [carriero@scclin001 carriero]$ strace -e stat bash -c /a/b/c/foodle 2>&1 | grep foodle    
    stat("/a/b/c/foodle", 0x7fff8d763390)   = -1 ENOENT (No such file or directory)     
    stat("/a/b/c/foodle", 0x7fff8d763370)   = -1 ENOENT (No such file or directory)    
    bash: /a/b/c/foodle: No such file or directory                   
    [carriero@scclin001 carriero]$ strace -e stat bash -c foodle 2>&1 | grep foodle     
    stat("/bin/foodle", 0x7ffe19c76a50)     = -1 ENOENT (No such file or directory)    
    stat("/usr/bin/foodle", 0x7ffe19c76a50) = -1 ENOENT (No such file or directory)    
    bash: foodle: command not found                                  
    [carriero@scclin001 carriero]$ PATH=/here:/there:/everywhere:$PATH       
    [carriero@scclin001 carriero]$ strace -e stat bash -c foodle 2>&1 | grep foodle  
    stat("/here/foodle", 0x7ffd2b1342c0)    = -1 ENOENT (No such file or directory)   
    stat("/there/foodle", 0x7ffd2b1342c0)   = -1 ENOENT (No such file or directory)   
    stat("/everywhere/foodle", 0x7ffd2b1342c0) = -1 ENOENT (No such file or directory)  
    stat("/bin/foodle", 0x7ffd2b1342c0)     = -1 ENOENT (No such file or directory)     
    stat("/usr/bin/foodle", 0x7ffd2b1342c0) = -1 ENOENT (No such file or directory)   
    bash: foodle: command not found                                                
    [carriero@scclin001 carriero]$  


Ordering is significant (will stop with the first found).  
Keeping your `PATH` tidy reduces the risk of accidental collisions, and could make the shell a little more responsive (think about
how much work it has to do to find the program).  

export VarName vs export VarName=Value vs VarName=Value
