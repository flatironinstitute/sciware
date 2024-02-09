import numpy as np

from . import array_example_module

def main():
    inarr = np.arange(20)
    outarr = np.empty_like(inarr)
    
    array_example_module.double_arr(outarr, inarr)
    
    print(inarr)
    print(outarr)

if __name__ == '__main__':
    main()
