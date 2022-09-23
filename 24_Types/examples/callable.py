from typing import Callable

def main():
    sum_then_square: Callable[[float, float], float]
    sum_then_square = lambda x, y: (x + y) ** 2
    a = sum_then_square(5, 6)

    # We can also assign a named function to a variable
    # The type would actually be inferred correctly without the explicit annotation
    sum_then_square_2: Callable[[float, float], float]
    sum_then_square_2 = explicit_sum_then_square
    b = sum_then_square_2(5, 6)
    assert(a == b)


def explicit_sum_then_square(x: float, y: float) -> float:
    return (x + y) ** 2