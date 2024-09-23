
from SciwarePackage.util.formatting import canonicalize_string
from SciwarePackage.util.enums import Mode


def multiply(a: int | float, b: int | float):
    return float(a * b)


def describe_operation(desc: str, left_operand: int | float, right_operand: int | float):
    canonical_string = canonicalize_string(desc)
    product = multiply(left_operand, right_operand)
    print(f"{canonical_string}\n\t{product}")


def main(mode: Mode, l: int | float, r: int | float):
    if mode == Mode.SIMPLE:
        describe_operation("times", l, r)
    else:
        describe_operation("multiplication of two numbers", l, r)


if __name__ == "__main__":
    main(Mode.ADVANCED, 3, 5)
