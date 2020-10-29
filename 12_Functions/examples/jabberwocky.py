# this code does actually work - there's a rootfinder buried in there!
# Barnett 10/28/20

import numpy as np
from math import *

def runcible(mimsy, wabe):
    """some function of mimsy and wabe"""
    return mimsy * wabe**3 + 100

def runciblederivative(mimsy, wabe):
    """partial of runcible with respect to wabe"""
    return 3 * mimsy * wabe**2

def bandersnatch(brillig, wabe):
    """some other function that we don't understand"""
    return brillig * tanh(wabe)


# now we're in some script and find...

# script proving my gimble is frumious! (recall technical words are gibberish to other users)
for brillig in np.arange(0, pi, 0.1):
    mimsy = cos(brillig)
    wabe_guess = 1.5
    while True:
        wabe_newguess = wabe_guess - runcible(mimsy, wabe_guess) / runciblederivative(mimsy, wabe_guess)
        if abs(wabe_newguess - wabe_guess) < 1e-9:
            break
        wabe_guess = wabe_newguess
        
    print(bandersnatch(brillig, wabe_newguess))

# ok, end here in the tutorial

    
# were we to actually test the rootfinding, this would be a start:
#    print(runcible(mimsy, wabe_newguess))
