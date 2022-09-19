from typing import cast, List, TypeGuard, Union


# Canonical example from documentation:
def is_str_list(val: List[object]) -> TypeGuard[List[str]]:
    return all(isinstance(x, str) for x in val)
# This is good--we use the properties of the data itself to determine whether
# the type is valid.
# That's why the check works at runtime: we wrote something that works from the actual values.


# This, on the other hand, is not a good idea, even though mypy won't complain about it:
def is_int(val: Union[int, float], is_float: bool) -> TypeGuard[int]:
    return not is_float
# You shouldn't do this, because you're making a decision about val's type based on
# data that is not actually part of val. This doesn't really check anything, it's basically
# just a cast.


def might_be_int(x: Union[int, float], sent_you_a_float: bool) -> None:
    if (is_int(x, sent_you_a_float)):
        # mouseover shows analyzer now knows a is an int
        x
    else:
        # *but* it cannot conclude anything from a False result
        x

# This version doesn't pretend to know something it doesn't.
def better_might_be_int(x: Union[int, float], sent_you_a_float: bool) -> None:
    if (sent_you_a_float):
        x
        x = cast(float, x)
        x
    else:
        x
        x = cast(int, x)
        x
