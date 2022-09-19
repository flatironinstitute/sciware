from typing import Literal, Union

def fn() -> None:
    direction: Union[Literal['North'], Literal['South'], Literal['East'], Literal['West']] = 'west'
    print(f"Follow me to the {direction}!")