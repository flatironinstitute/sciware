from typing import Optional, Union

def narrowing_example(my_var: Union[str, int]) -> str:
    if isinstance(my_var, str):
        # If this branch got taken, we know my_var is a str, so mouseover shows it
        return my_var
    # type checker knows all strs hit the "return" statement
    # So it knows by process of elimination that my_var is an int
    # And mouseover will show 'int' here
    return str(my_var)

def narrowing_example_2(a: Optional[int]) -> None:
    print(a) # here 'a' could be int or None
    if (a is None):
        raise Exception('Exception ends this branch!')
    a # here a must be int, and mouseover shows it
