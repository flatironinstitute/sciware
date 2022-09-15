from typing import List, Literal, Tuple, Callable, TypeAlias, Union
from math import sin

RuleType: TypeAlias = Union[Literal['left'], Literal['right'], Literal['midpoint'], Literal['trapezoidal']]
# but consider whether this is better handled by an Enum!
ParameterTuple: TypeAlias = Tuple[Callable[[float], float], float, float, str, RuleType, int]
# But consider using a NamedTuple or dataclass!

def get_interval_value(interval: Tuple[float, float], rule: RuleType, f: Callable[[float], float]) -> float:
    left = min(interval)
    right = max(interval)
    span = (right - left)
    result: float = 0
    if rule == 'left':
        result = f(left)
    elif rule == 'right':
        result = f(right)
    elif rule == 'midpoint':
        result = f((left + right) / 2)
    elif rule == 'trapezoidal':
        a = f(left)
        b = f(right)
        result = (a + b) / 2
    else:
        raise Exception("Can't happen: Unknown rule type.")
    return result * span


def split_range(integral_range: Tuple[float, float], number_of_intervals: int) -> List[Tuple[float, float]]:
    x0 = min(integral_range)
    xf = max(integral_range)
    per_interval_span = (xf - x0) / number_of_intervals
    values = []
    for i in range(number_of_intervals):
        range_start = x0 + (i * per_interval_span)
        range_end = range_start + per_interval_span
        values.append((range_start, range_end))
    return values


def compute_sum(f: Callable[[float], float], x0: float, xf: float, rule: RuleType, number_of_intervals: int) -> float:
    intervals = split_range((x0, xf), number_of_intervals)
    return sum([get_interval_value(i, rule, f) for i in intervals])


def report_run(parameters: ParameterTuple) -> None:
    (fn, x0, xf, desc, rule, interval_count) = parameters
    print(f"Running {desc} with {interval_count} intervals over range ({x0}, {xf}) using {rule}")
    print(f"\tResult: {compute_sum(fn, x0, xf, rule, interval_count)}")


if __name__ == '__main__':
    fn: Callable[[float], float] = lambda x: x**2
    square_runs: List[ParameterTuple] = [
        (fn, 1.0, 5.0, "x^2", 'left', 4),
        (fn, 1.0, 5.0, "x^2", 'right', 4),
        (fn, 1.0, 5.0, "x^2", 'midpoint', 4),
        (fn, 1.0, 5.0, "x^2", 'trapezoidal', 4),
        (fn, 1.0, 5.0, "x^2", 'midpoint', 12),
        (fn, 1.0, 5.0, "x^2", 'trapezoidal', 12),
        (fn, 1.0, 5.0, "x^2", 'trapezoidal', 20),
    ]
    print("\tReference correct answer for x^2 over (1, 5): 41.3-bar")
    for d in square_runs:
        report_run(d)

    f2: Callable[[float], float] = lambda x: sin(x)
    sin_runs: List[ParameterTuple] = [
        (f2, 1.0, 2.0, "sin(x)", 'left', 4),
        (f2, 1.0, 2.0, "sin(x)", 'right', 4),
        (f2, 1.0, 2.0, "sin(x)", 'midpoint', 4),
        (f2, 1.0, 2.0, "sin(x)", 'trapezoidal', 4),
        (f2, 1.0, 2.0, "sin(x)", 'midpoint', 20),
        (f2, 1.0, 2.0, "sin(x)", 'trapezoidal', 20),
        (f2, 1.0, 2.0, "sin(x)", 'trapezoidal', 200),
    ]
    print("\n\tReference correct answer for sin(x) over (1, 2) ~= 0.95644914241")
    for p in sin_runs:
        report_run(p)
