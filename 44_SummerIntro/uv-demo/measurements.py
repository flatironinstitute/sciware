"""Helpers for cleaning and summarizing experimental measurements."""

import numpy as np

# Our instrument writes this sentinel value when a reading fails
MISSING = -999.0


def clean(values):
    """Convert a list of readings to an array, marking failures as NaN."""
    arr = np.asarray(values, dtype=np.float_)  # np.float_: removed in NumPy 2.0
    arr[arr == MISSING] = np.NaN               # np.NaN:    removed in NumPy 2.0
    return arr


def summarize(values):
    """Return the (mean, std) of the readings, ignoring failed measurements."""
    arr = clean(values)
    return np.nanmean(arr), np.nanstd(arr)
