class Parent(): pass
class Child(Parent): pass

def example() -> None:
    a: Parent = Parent()
    b: Parent = Child()  # no problem: Child counts as Parent
    c: Child = Parent()  # error: Parent does not count as Child
    d: Child = b         # Works, because linter knows b is *actually* a child here