# Continue to improve the module ``rootfind1d.py``

Yes, since it has a function and a tester, it's a module.
Iterate test-break-fix cycles to improve robustness of
[rootfind1d](../examples/rootfind1d.py) :

* add to the tester a case that causes an infinity, or near-infinity, or NaN, hence breaks it

* fix the algorithm to catch such cases

* must it always terminate? It would be sad to be stuck in this iteration forever. [Advanced: add a tester with such a case.]

Note: breaking an algorithm requires your creative brain!

* fix the algorithm to catch such a case

* Improve the error reporting to the user for the above failure modes

* What if the f sent in needs to include parameters?
Ie, f(x,a,b,...) and dfdx(x,a,b,...) ?

* What if the user doesn't want to have to send in dfdx ?
Eg, look at the poorly-named
[scipy.optimize.newton](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.newton.html). Why do I say poorly-named?
*Functions should be named for the task they solve, not the particular algorithm(s) they might use.*
