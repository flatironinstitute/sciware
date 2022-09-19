class MyClass():
    def __init__(self):
        # WARNING: mypy won't check this with no explicit annotations!
        pass

    # PyLance (VSCode) gives a warning for using MyClass here; mypy is fine with it
    def compare(self, other: MyClass) -> int:
        return 5

    # PyLance successfully resolves this MyClass reference in quotes
    def vscode_compare(self, other: "MyClass") -> int:
        return 6


class MyOtherClass(MyClass): pass

def example() -> None:
    b: MyClass = MyClass()
    c: MyOtherClass = MyOtherClass()
    d: MyOtherClass = b
    b = c # No warning: a MyOtherClass is a MyClass, so this is fine
    e: MyOtherClass = b  # No warning: mypy knows b is now a MyOtherClass!
    b = 5 # This is still an error
