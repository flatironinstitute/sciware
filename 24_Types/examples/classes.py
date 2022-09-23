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


class Parent(): pass
class Child(Parent): pass

def example() -> None:
    a: Parent = Parent()
    b: Parent = Child()  # no problem: Child counts as Parent
    c: Child = Parent()  # error: Parent does not count as Child
    d: Child = b         # Works, because linter knows b is *actually* a child here