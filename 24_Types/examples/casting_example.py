import xarray as xr
from typing import cast

def load_xarray(filename: str) -> xr.Dataset:
    # xarray's open_dataset returns Any, but we know it's returning a Dataset object.
    # So use cast(TYPE, VALUE) to tell the checker that VALUE is of type TYPE
    results = cast(xr.Dataset, xr.open_dataset(filename))
    return results