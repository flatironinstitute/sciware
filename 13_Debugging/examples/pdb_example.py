import numpy as np

def compute_median(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[len(arr)/2] + arr[len(arr)/2+1])/2
    else:
        return arr[len(arr)/2]
    
def run_example(N):
    arr = np.arange(N)
    print(compute_median(arr))

run_example(123)
