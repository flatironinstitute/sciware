# Optional arguments

We saw that optional arguments with sensible default values are good things: they make it easy for a basic user
while allowing experts to adjust algorithm parameters.

We saw how they are trivial to add in Python (Julia is similar).
How to do it in other common languages?


## MATLAB

* Discuss ways to add optional arguments that have default values. There are two ones commonly used (*Hints:* ``help gmres``, ``help odeset``). Critique them.

* Critique this (Alex's) way to do it (look at docs and first 4 lines of function body):
[lfmm2d2ppart.m](https://github.com/ahbarnett/perifmms/blob/master/lap2d/lfmm2d2ppart.m)


## C

* discuss ways to add optional arguments.

* Critique how FINUFFT does it (read only to the first Warning):
[Example usage from C++ and C](https://finufft.readthedocs.io/en/latest/cex.html)

* Our interface was deliberately clunky due to wanting C-compatibility. What's the C++ way to do it?


## Fortran

* discuss ways to add optional arguments.

* Critique how FINUFFT does it:
[Usage from Fortran](https://finufft.readthedocs.io/en/latest/fortran.html)

