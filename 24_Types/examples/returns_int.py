def returns_int():
    return 15

a = returns_int() + 3

def really_returns_int() -> int:
    return 15

b = really_returns_int()

# A Literal[<X>] type inherits from the type that would hold variable <X>
# i.e. Literal[18] is still an int, because 18 is an int
# So this raises no errors:
def takes_int(x: int) -> int:
    return x

c = takes_int(a)
