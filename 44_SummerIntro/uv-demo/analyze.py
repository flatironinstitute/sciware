"""Summarize a batch of detector readings."""

from measurements import summarize

# A handful of readings; -999.0 marks a measurement that failed
readings = [12.3, 11.8, -999.0, 12.1, 12.5, -999.0, 11.9]

mean, std = summarize(readings)
print(f"mean = {mean:.3f}, std = {std:.3f}")
