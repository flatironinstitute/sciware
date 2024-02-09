from . import struct_example_module

def main():
    s = struct_example_module.S(3)
    print()
    print(f'{s = }')
    print(f'{s.i = }')
    print(f'{s.m() = }')
    print(f'{struct_example_module.f(s) = }')
    print()

if __name__ == '__main__':
    main()
