from io import TextIOWrapper

def write_to_file(msg: str, handle: TextIOWrapper) -> None:
    handle.write(msg)

def demo(path: str, msg: str) -> None:
    with open(path, 'w') as f:
        write_to_file(msg, f)