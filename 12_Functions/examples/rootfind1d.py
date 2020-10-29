# Our own very simple rootfinder. Barnett 10/28/20
# Note the good naming, which describes the *task solved*, not the
# *specific algorithm* - better than scipy.optimize.newton !
# Note scipy.optimize.root does something else!


def rootfind1d(f, dfdx, x0):
    """Find a nearby root of a 1D scalar function.
    Inputs: f - a 1D scalar function
            dfdx - its derivative function
            x0 - an initial guess to the root
    Returned value: approximate root x, meaning f(x)=0.
    Notes: uses the Newton-Raphson iteration.
    """
    while True:
        xnew = x0 - f(x0)/dfdx(x0)
        if abs(xnew-x0) < 1e-9:
            break
        x0 = xnew
    return xnew
    
if __name__ == "__main__":
    from math import *
    # if this module is simply run, does test: checks root x=pi of f(x)=sin(x) 
    f = lambda x: sin(x)
    dfdx = lambda x: cos(x)
    x = rootfind1d(f, dfdx, 2.0)
    if abs(x-pi)<1e-9:
        print('pass')
    else:
        print('fail')
