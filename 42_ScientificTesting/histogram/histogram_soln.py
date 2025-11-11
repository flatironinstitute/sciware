# Here's one possible way to rewrite histogram.py to make it easier to test.
from typing import Generator
from unittest.mock import patch
import pytest
from math import floor
import random

def parse_line(line: str) -> Generator[str, None, None]:
    l = line.rstrip()
    yield from l.split()


def parse_lines(line_source: Generator[str, None, None]) -> dict[str, int]:
    data = {}

    for line in line_source:
        for token in parse_line(line):
            if token not in data:
                data[token] = 0
            data[token] += 1
    return data


def read_file(filename: str) -> Generator[str, None, None]:
    with open(filename, 'r') as file:
        yield from file


def compute_zoomed_abundance(count: int, total: int, zoom_factor: int = 9):
    normalized_frequency = zoom_factor * count / total
    return normalized_frequency


def compute_width(normalized_frequency: float, max_width: int = 76) -> int:
    return min(floor(max_width * normalized_frequency), max_width)


def report_histogram(data: dict[str, int], max_width: int = 76, top_count: int = 12, zoom: int = 9):
    sorted_data = sorted(data, key=lambda x: data[x], reverse = True)
    total_count = sum(data.values())

    for i in range(top_count):
        element = sorted_data[i]
        count = data[element]
        freq = compute_zoomed_abundance(count, total_count, zoom)
        width = compute_width(freq, max_width)
        label = f"{element}:"
        print(f"{label:<4}{'#' * width}")


def histogram(file, max_width = 76):
    file_handler = read_file(file)
    data = parse_lines(file_handler)
    report_histogram(data, max_width, top_count=12, zoom=9)


if __name__ == '__main__':
    histogram('histogram.data', 100)



## Tests might look like this:

def test_parse_line():
    values = ["a", "b", "C", "D54"]
    value_string = " ".join(values) + "\n"
    i = 0
    for v in parse_line(value_string):
        assert v == values[i]
        i += 1


def test_parse_lines():
    # Build some fake data
    data = { 'a': 12, 'bb': 3, 'Cc': 6 }
    # and build a set of strings holding that data
    lines = []
    for k in data.keys():
        this_str = f'{k} ' * data[k]
        lines.append(this_str)
    # and a fake generator to feed our strings into the fn
    def fake_line_source():
        yield from lines

    # And now, act and assert
    result = parse_lines(fake_line_source())
    assert result == data


# Another approach might break these parameterized options out into
# more specifically-named tests based on what they're testing--
# the first case is a base case;
# the second case checks what happens when the count equals the overall
#  count; and
# the third case checks that the zoom value is being used to magnify
#  the natural abundance figure.
@pytest.mark.parametrize("n,t,zoom,expected",[
    (1, 10, 1, 0.1),
    (10, 10, 1, 1),
    (2, 10, 3, 0.6)
])
def test_compute_zoomed_abundance(n, t, zoom, expected):
    assert compute_zoomed_abundance(n, t, zoom) == pytest.approx(expected)


@pytest.mark.parametrize("freq,max", [
    (0.4, 100),
    (1.2, 100),
    (0.2, 10),
])
def test_compute_width(freq, max):
    expected = freq * max
    if expected > max:
        expected = max
    assert compute_width(freq, max) == expected


def test_report_histogram_prints_correct_number_of_lines():
    top_count = 2
    with patch("builtins.print") as mock_print:
        data = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
        assert len(data) > top_count
        report_histogram(data, top_count=top_count)
        assert mock_print.call_count == top_count


def test_report_histogram_respects_max_width():
    max_width = 42
    data = {'a': 50, 'b': 50, 'c': 50, 'd': 50}
    with patch("builtins.print") as mock_print:
        report_histogram(data, max_width, top_count=4)
        # call_args_list gets the list of arguments used to call the mock,
        # in chronological order.
        # Each one of these is a tuple of (positional_arguments, named_arguments)
        # So to get the arguments used to call print() -- i.e. a single positional
        # argument -- we would take calls[n][0][0], where n is the nth time
        # "print" was called, the first [0] is the positional arguments list,
        # and the second [0] is the first positional argument.
        calls = mock_print.call_args_list
        assert len(calls) == 4
        for print_call_args in calls:
            # for each call, take the first positional argument.
            # Since this is the print() function, that's just the
            # string we wrote to the output.
            assert len(print_call_args[0][0]) == max_width + 4

    
def test_report_histogram_computes_widths():
    max_width = 20
    data = {'a': 50, 'b': 25, 'c': 25}
    # with this data we'd expect one bar of 1/2 maxwidth and 2 of 1/4 maxwidth
    # which would lead to max_width instances of the character in total
    with patch("builtins.print") as mock_print:
        report_histogram(data, max_width, top_count=3, zoom=1)
        calls = mock_print.call_args_list
        total_output = " ".join(call[0][0] for call in calls)
        assert total_output.count("#") == max_width


def test_report_histogram_sorts_data():
    data = {"Aa": 20, "Gg": 6000}
    for key in "Bb Cc Dd Ee Ff Hh Ii Jj Kk Ll Mm Nn Oo Pp".split():
        data[key] = random.randint(100, 4000)

    with patch("builtins.print") as mock_print:
        report_histogram(data, top_count=len(data), zoom=2)
        calls = mock_print.call_args_list
        # These are in chrono order, so we expect
        # the longest printout to come first.
        all_strings = [call[0][0] for call in calls]
        last_len = len(all_strings[0])
        for s in all_strings:
            assert len(s) <= last_len
            last_len = len(s)


def test_histogram_dispatches_correctly():
    # This is *not* a high-priority test. It's included for two
    # reasons:
    # 1) It shows how we can assert that the original interface
    # function is calling the correct refactored functions and
    # using the values they return; and
    # 2) It illustrates a bit of unintuitiveness of patching in
    # python: if you're patching out a function, you need to patch
    # it from the package under test, NOT necessarily from where
    # it's defined.
    # So here we patch read_file, parse_lines, etc. from the
    # 'histogram_soln' package.
    # Similarly, if we wanted to patch the `floor` function used in
    # compute_width, we would need to patch `histogram_soln.floor`,
    # *NOT* `math.floor`.
    with patch("histogram_soln.read_file") as mock_read_file:
        with patch("histogram_soln.parse_lines") as mock_parse_lines:
            with patch("histogram_soln.report_histogram") as mock_report:
                histogram("foo")
                mock_read_file.assert_called_once_with("foo")
                mock_parse_lines.assert_called_once_with(mock_read_file.return_value)
                report_histogram.assert_called_once_with(
                    mock_parse_lines.return_value,
                    76,
                    top_count=12,
                    zoom=9
                )
