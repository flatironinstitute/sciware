from timeit import default_timer

import numpy as np

from . import examplemod

def main():
    inarr = np.arange(20)
    outarr = np.empty_like(inarr)
    
    examplemod.double_arr(outarr, inarr)
    
    print(inarr)
    print(outarr)

if __name__ == '__main__':
    main()
