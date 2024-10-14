
from sciware_package.util import canonicalize_string
from sciware_package.util.enums import Mode


def multiply(a: int | float, b: int | float):
    """Multiply two numbers.

    Args:
        a (int | float): First number
        b (int | float): Second number

    Returns:
        int | float: The product of the input numbers.
    """
    return float(a * b)


def describe_operation(desc: str, left_operand: int | float, right_operand: int | float):
    """A trivial function that calls a few functions defined in a few modules.

    Multiplies two numbers, as well as a string describing the operation performed.

    Args:
        desc (str): Description of the operation.
        left_operand (int | float): The first number.
        right_operand (int | float): The second number.
    """
    canonical_string = canonicalize_string(desc)
    product = multiply(left_operand, right_operand)
    print(f"{canonical_string}\n\t{product}")


def main(mode: Mode, l: int | float, r: int | float):
    """Entry point function. Multiplies two numbers, and describes them either
    succinctly or verbosely, based on the mode.

    Args:
        mode (Mode): If SIMPLE, will use a succinct description. If ADVANCED,
            will use a verbose description.
        l (int | float): First number to multiply.
        r (int | float): Second number to multiply.
    """
    if mode == Mode.SIMPLE:
        describe_operation("times", l, r)
    else:
        describe_operation("multiplication of two numbers", l, r)


if __name__ == "__main__":
    main(Mode.ADVANCED, 3, 5)
