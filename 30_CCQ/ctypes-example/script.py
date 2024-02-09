import ctypes

import numpy as np

SO_FILE = './example.so'

def main():
    
    inarr = np.arange(20)
    outarr = np.empty_like(inarr)

    lib = ctypes.CDLL(SO_FILE)
    double_arr = lib.double_arr
    # void double_arr(const size_t n, double *outarr, double const * inarr)
    double_arr.argtypes = [ctypes.c_size_t,
                           ctypes.POINTER(ctypes.c_double),
                           ctypes.POINTER(ctypes.c_double),
                          ]
    
    double_arr(
        len(inarr),
        outarr.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
        inarr.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    )
    
    print(inarr)
    print(outarr)


if __name__ == '__main__':
    main()
