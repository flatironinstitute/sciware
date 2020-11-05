# Our own very simple rootfinder. Barnett 10/28/20
# Note the good naming, which describes the *task solved*, not the
# *specific algorithm* - better than scipy.optimize.newton !
# Note scipy.optimize.root does something else!


def rootfind1d(f, dfdx, x0, tol=1e-9):
    """Find a nearby root of a 1D scalar function.
    Inputs: f - a 1D scalar function
            dfdx - its derivative function
            x0 - an initial guess to the root
            tol (optional) - desired absolute tolerance in the root
    Returned value: approximate root x, meaning f(x)=0.
    Notes: uses the Newton-Raphson iteration.
    """
    while True:
        xnew = x0 - f(x0)/dfdx(x0)
        if abs(xnew-x0) < tol:
            break
        x0 = xnew
    return xnew

def testderiv(f, dfdx, x):
    """Test if dfdx is actually the derivative of f(x) at a given x, using
    finite differencing. Returns True iff error near expected level.
    """
    eps = 1e-5          # for choice, see Barnett FWAM2019 lecture, slide 14.
    FDderiv = (f(x+eps)-f(x-eps))/(2*eps)
    return abs(FDderiv-dfdx(x)) < 1e-9

from math import *
def test():
    # checks root x=pi of f(x)=sin(x)
    f = lambda x: sin(x)
    dfdx = lambda x: cos(x)
    if not testderiv(f,dfdx,1.4):  # good practice to test your test pair first
        print('dfdx appears not even to be the derivative of f!')
        return
    tol=1e-12                      # now actual test of rootfind...
    x = rootfind1d(f, dfdx, 2.0, tol=tol)
    if abs(x-pi)<tol:
        print('pass')
    else:
        print('fail')

test()                              # run if called as script OR (re)imported
