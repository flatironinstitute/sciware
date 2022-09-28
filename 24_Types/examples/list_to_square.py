from typing import List, Union
import numpy as np
import numpy.typing as npt
import math


def turn_a_list_into_a_square_matrix(values):
    root = math.sqrt(len(values))
    # ^-- this line will fail if values is not a valid input to len()
    # (For example, a scalar int or float)
    if root < 1 or root % 1 != 0:
        return None
    array = np.asarray(values)
    array = array.reshape((root, root))
    # ^-- this breaks. ndarray.reshape needs a tuple of ints, not
    # a tuple of floats that happen to be integer-valued.
    return array


def turn_a_list_into_a_square_matrix_typed(values: List[int]) -> Union[npt.NDArray, None]:
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
    untyped = turn_a_list_into_a_square_matrix(input_int)
    untyped_bad_input = turn_a_list_into_a_square_matrix(input_str)
    typed_bad_input = turn_a_list_into_a_square_matrix_typed(input_int)
    typed_worse_input = turn_a_list_into_a_square_matrix_typed(input_str)
    typed = turn_a_list_into_a_square_matrix_typed([1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(typed)
