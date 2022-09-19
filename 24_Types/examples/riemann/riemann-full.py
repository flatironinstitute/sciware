from typing import List, Literal, Tuple, Callable, TypeAlias, Union
from math import sin

IntegrableFunction: TypeAlias = Callable[[float], float]
Interval: TypeAlias = Tuple[float, float]
RuleType: TypeAlias = Union[Literal['left'], Literal['right'], Literal['midpoint'], Literal['trapezoidal']]
    # but this would be better handled by an enum!
ParameterTuple: TypeAlias = Tuple[Callable[[float], float], float, float, str, RuleType, int]
    # But it might be better to use a NamedTuple or a Dataclass

def get_interval_value(interval: Interval, rule: RuleType, f: IntegrableFunction) -> float:
    """Computes the value of function f over the interval under the Riemann-sum rule. Return value is suitable
    for summing over to compute a Riemann sum.

    Args:
        interval (Interval): Beginning and end of an interval over which the function is being applied.
        rule (RuleType): What rule to use for computing the function's representative value over that interval, e.g.
        use left value, right value, midpoint, trapezoid...
        f (IntegrableFunction): The function whose definite integral is being approximated.

    Raises:
        Exception: If an unrecognized rule type is received. Should not be possible.

    Returns:
        float: The representative value for the function over the interval, suitable for aggregation to estimate
        the definite integral.
    """
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


def split_range(integral_range: Interval, number_of_intervals: int) -> List[Interval]:
    """Computes a set of intervals (tuples of boundaries) from an overall range of values split n ways.
    The resulting intervals will be evenly spaced.

    Args:
        integral_range (Interval): Beginning and end of the overall range of input values
        number_of_intervals (int): How many ways to split the overall range.

    Returns:
        List[Interval]: List containing number_of_intervals equal-sized intervals which collectively
        exhaust the integral_range.
    """
    x0 = min(integral_range)
    xf = max(integral_range)
    per_interval_span = (xf - x0) / number_of_intervals
    values = []
    for i in range(number_of_intervals):
        range_start = x0 + (i * per_interval_span)
        range_end = range_start + per_interval_span
        values.append((range_start, range_end))
    return values


def compute_sum(f: IntegrableFunction, x0: float, xf: float, rule: RuleType, number_of_intervals: int) -> float:
    """Estimates the definite integral of a function over a range of values using a Riemann sum rule.

    Args:
        f (IntegrableFunction): Scalar-valued continuous function whose definite integral will be estimated.
        x0 (float): Beginning of the (scalar) input range.
        xf (float): End of the (scalar) input range.
        rule (RuleType): Riemann-sum rule to apply.
        number_of_intervals (int): How finely to split up the input range.

    Returns:
        float: A Riemann-sum estimate of the definite integral.
    """
    intervals = split_range((x0, xf), number_of_intervals)
    return sum([get_interval_value(i, rule, f) for i in intervals])


def report_run(parameters: ParameterTuple) -> None:
    """Run a Riemann-sum definite integral estimation and report the results.

    Args:
        parameters (ParameterTuple): Specification of the approximation to run.
    """
    (fn, x0, xf, desc, rule, interval_count) = parameters
    print(f"Running {desc} with {interval_count} intervals over range ({x0}, {xf}) using {rule}")
    print(f"\tResult: {compute_sum(fn, x0, xf, rule, interval_count)}")


if __name__ == '__main__':
    fn: IntegrableFunction = lambda x: x**2
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

    f2: IntegrableFunction = lambda x: sin(x)
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
