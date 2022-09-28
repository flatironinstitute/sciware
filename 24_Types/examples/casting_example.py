import xarray as xr
from typing import cast, Any, Union

def load_xarray(filename: str) -> xr.Dataset:
    unknown_results = xr.open_dataset(filename)
    # xarray doesn't publish types (yet), so open_dataset is not annotated.
    # But we know it returns a Dataset object.
    # So use cast(TYPE, VALUE) to tell the checker that VALUE is of type TYPE
    results = cast(xr.Dataset, unknown_results)
    return results


def load_xarray_better(filename: str) -> xr.Dataset:
    # In practice, this is probably better than a cast
    results: xr.Dataset = xr.open_dataset(filename)
    return results


def cast_any(input_value: Any) -> None:
    # Since a is explicitly typed Any, it always remains Any.
    a: Any
    a = cast(int, input_value)
    print(a)
    # On the other hand, b updates in response to the cast
    b: Union[int, float]
    b = cast(int, input_value)
    print(b)