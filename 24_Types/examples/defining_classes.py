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
        
def test_use_of_MyClass_annotation() -> None:
    a: MyClass = MyClass()