"""Summarize a batch of data."""

import numpy as np


def summarize(values):
    """Return the (mean, std) of the readings, ignoring failed measurements."""
    arr = np.asarray(values, dtype=np.float_)  # np.float_: removed in NumPy 2.0
    arr[arr == -999.0] = np.NaN                # np.NaN:    removed in NumPy 2.0
    return np.nanmean(arr), np.nanstd(arr)


# A handful of readings; -999.0 marks a measurement that failed
data = [12.3, 11.8, -999.0, 12.1, 12.5, -999.0, 11.9]

mean, std = summarize(data)
print(f"mean = {mean:.3f}, std = {std:.3f}")
