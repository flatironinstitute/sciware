def random_integer() -> int:
    return 15   # TODO: Pick more-random number

def do_math() -> int:
    a = random_integer() # linter knows a is an int!
    b = random_integer()
    c = a + b
    return c