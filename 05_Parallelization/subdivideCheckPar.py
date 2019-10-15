#!/bin/env python3
# Parallel example using rank parallelism

import sys
from math import pi
from random import randint, seed

def findZero(f, l, u, eps):
    """Find and return a root of f(x), l<=x<=u s.t. |f(x)| < eps, using simple bracketing and return it, or None if none is found."""
    fl = f(l)
    if abs(fl) < eps: return l
    fu = f(u)
    if abs(fu) < eps: return None
    # if f(u) and f(l) have the same sign, stop:
    if (fl*fu) >= 0.0: return None
    # There's a zero in there somewhere...
    for r in range(64):
        # Bisect the current range based on the sign of the midpoint
        m = (l+u)/2.
        fm = f(m)
        if abs(fm) < eps: return m
        if (fm*fl) >= 0.0:
            l = m
            fl = fm
        else:
            u = m
            fu = fm
    raise Exception('Failed to find zero.')

def subdivideCheck(lower, upper, func, step, eps):
    """Subdivide the range upper<=x<=lower into segments of size at most 1, and then call findZero(func, l, u, eps) on each."""
    if (upper - lower) > 1:
        # proxy for recursive exploration of a data space or structure.
        mid = (upper + lower)/2.
        subdivideCheck(lower, mid, func, step, eps)
        subdivideCheck(mid, upper, func, step, eps)
    else:
        # proxy for determining if this interval should be searched. 1 in 4 chance.
        if 1 == randint(0, 3):
            if own():
                x = lower
                while x < upper:
                    z = findZero(func, x, min(x+step, upper), eps)
                    if z is not None: print(z)
                    x += step

def testFunc(x):
    """Target function we will look for zeros of."""
    x = pi * (x % 2)
    t, s = 1., 1.
    r = 0
    for i in range(20):
        r += s*t
        t, s = t*(x/(2*i+1))*(x/(2*i+2)), s*-1
    return r

import os
iterCount, workLoad = 0, 0
rank = int(os.environ['RANK'])
ranks = int(os.environ['RANKS'])

def own():
    global iterCount, workLoad
    r = rank == (iterCount % ranks)
    iterCount += 1
    if r: workLoad += 1
    return r

if __name__ == '__main__':
    seed(7350)
    subdivideCheck(float(sys.argv[1]), float(sys.argv[2]), testFunc, 1e-6, 1e-8)
    print('Rank: %d/%d'%(rank, ranks), ', iterCount:', iterCount, ', workLoad:', workLoad, sep='')
