def sumsquares(a):
    """Return the sum of the squares of the elements of a NumPy array."""
    return sum(a*a)

if __name__ == "__main__":
    # if this module is simply run, does a self-test for floating-point array
    import numpy as np
    if sumsquares(np.array((3.0,4.0))) == 25.0:
        print('pass')
    else:
        print('fail')


    
