from typing import Final, List, Optional, Union, Any, cast
import numpy as np
import math


# NOTE: Can start with this
def make_a_square_untyped_buggy(values):
    root = math.sqrt(len(values))
    if root < 1 or root % 1 != 0:
        return None
    array = np.asarray(values)
    array = array.reshape((root, root)) # We know this should work but it breaks at runtime
    return array


def make_a_square_untyped(values):
    root = math.sqrt(len(values))
    int_root = int(root)
    if root < 1 or root != int_root:
        return None
    array = np.asarray(values)
    array = array.reshape((root, root))
    return array


def make_a_square_typed(values: List[int]) -> Union[np.ndarray, None]:
    root = math.sqrt(len(values))
    int_root = int(root)
    if root < 1 or root != int_root:
        return None
    array: np.ndarray = np.asarray(values)
    array = array.reshape((int_root, int_root))
    return array


if __name__ == '__main__':
    input_int = 54
    input_str = 'hello'
    untyped = make_a_square_untyped(input_int)
    untyped_bad_input = make_a_square_untyped(input_str)
    typed_bad_input = make_a_square_typed(input_int)
    typed = make_a_square_typed([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(typed)
