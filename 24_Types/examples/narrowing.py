from typing import Optional, Union

def narrowing_example(my_var: Union[str, int]) -> int:
    if isinstance(my_var, str):
        # In this branch, we know my_var is a str
        return len(my_var)
    # All strs exit the function at the "return" statement
    # So by process of elimination, my_var must be an int
    # And mouseover will show 'int' here
    return my_var + 1

def narrowing_example_2(a: Optional[int]) -> None:
    print(a) # here 'a' could be int or None
    if (a is None):
        raise Exception('Exception ends this branch!')
    print(a) # here a must be int