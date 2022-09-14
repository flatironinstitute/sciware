from typing import List, Tuple, Dict, Callable, TypeAlias, Union, cast
from enum import Enum
from math import sin

class RuleType(Enum):
    LEFT = 1
    RIGHT = 2
    MIDPOINT = 3
    TRAPEZOIDAL = 4

def get_interval_sum(interval: Tuple[float, float], rule: RuleType, f: Callable[[float], float]) -> float:
    left = min(interval)
    right = max(interval)
    span = (right - left)
    result: float = 0
    if rule == RuleType.LEFT:
        result = f(left)
    elif rule == RuleType.RIGHT:
        result = f(right)
    elif rule == RuleType.MIDPOINT:
        result = f((left + right) / 2)
    elif rule == RuleType.TRAPEZOIDAL:
        a = f(left)
        b = f(right)
        result = (a + b) / 2
    else:
        raise Exception("Can't happen: Unknown rule type.")
    return result * span


def divide_range(integral_range: Tuple[float, float], number_of_intervals: int) -> List[Tuple[float, float]]:
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
    intervals = divide_range((x0, xf), number_of_intervals)
    return sum([get_interval_sum(i, rule, f) for i in intervals])


ParameterDict: TypeAlias = Dict[str, Union[str, float, int, Callable[[float], float], object]]
def report_run_dict(parameters: ParameterDict) -> None:
    f = cast(Callable[[float], float], parameters['fn'])
    x0 = cast(float, parameters['x0'])
    xf = cast(float, parameters['xf'])
    interval_count = cast(int, parameters['interval_count'])
    rule = cast(RuleType, parameters['rule'])
    print(f"Running {parameters['desc']} with {interval_count} intervals over range ({x0}, {xf}) using {rule}")
    print(f"\tResult: {compute_sum(f, x0, xf, rule, interval_count)}")



from dataclasses import dataclass
@dataclass
class ReimannSettings:
    fn: Callable[[float], float]
    desc: str
    x0: float
    xf: float
    rule: RuleType
    interval_count: int

def report_run_dataclass(parameters: ReimannSettings) -> None:
    print(f"Running {parameters.desc} with {parameters.interval_count} intervals over range ({parameters.x0}, {parameters.xf}) using {parameters.rule}")
    print(f"\tResult: {compute_sum(parameters.fn, parameters.x0, parameters.xf, parameters.rule, parameters.interval_count)}")


if __name__ == '__main__':
    fn: Callable[[float], float] = lambda x: x**2
    square_runs = [
        {'fn': fn, 'x0': 1.0, 'xf': 5.0, 'desc': "x^2", 'rule': RuleType.LEFT, 'interval_count': 4},
        {'fn': fn, 'x0': 1.0, 'xf': 5.0, 'desc': "x^2", 'rule': RuleType.RIGHT, 'interval_count': 4},
        {'fn': fn, 'x0': 1.0, 'xf': 5.0, 'desc': "x^2", 'rule': RuleType.MIDPOINT, 'interval_count': 4},
        {'fn': fn, 'x0': 1.0, 'xf': 5.0, 'desc': "x^2", 'rule': RuleType.TRAPEZOIDAL, 'interval_count': 4},
        {'fn': fn, 'x0': 1.0, 'xf': 5.0, 'desc': "x^2", 'rule': RuleType.MIDPOINT, 'interval_count': 12},
        {'fn': fn, 'x0': 1.0, 'xf': 5.0, 'desc': "x^2", 'rule': RuleType.TRAPEZOIDAL, 'interval_count': 12},
        {'fn': fn, 'x0': 1.0, 'xf': 5.0, 'desc': "x^2", 'rule': RuleType.TRAPEZOIDAL, 'interval_count': 200}
    ]
    print("\tReference correct answer for x^2 over (1, 5): 41.3-bar")
    for d in square_runs:
        report_run_dict(d)

    f2: Callable[[float], float] = lambda x: sin(x)
    sin_runs = [
        ReimannSettings(f2, "sin(x)", 1.0, 2.0, RuleType.LEFT, 4),
        ReimannSettings(f2, "sin(x)", 1.0, 2.0, RuleType.RIGHT, 4),
        ReimannSettings(f2, "sin(x)", 1.0, 2.0, RuleType.MIDPOINT, 4),
        ReimannSettings(f2, "sin(x)", 1.0, 2.0, RuleType.TRAPEZOIDAL, 4),
        ReimannSettings(f2, "sin(x)", 1.0, 2.0, RuleType.MIDPOINT, 20),
        ReimannSettings(f2, "sin(x)", 1.0, 2.0, RuleType.TRAPEZOIDAL, 20),
        ReimannSettings(f2, "sin(x)", 1.0, 2.0, RuleType.TRAPEZOIDAL, 200),
    ]
    print("\n\tReference correct answer for sin(x) over (1, 2) ~= 0.95644914241")
    for p in sin_runs:
        report_run_dataclass(p)
