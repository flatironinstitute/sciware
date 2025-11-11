import binary_search


def test_midpoint_even():
    assert binary_search.midpoint(1, 7) == 4


def test_midpoint_odd():
    assert binary_search.midpoint(1, 8) == 4


def test_midpoint_small():
    assert binary_search.midpoint(0, 1) == 0


def test_midpoint_same():
    assert binary_search.midpoint(0, 0) == 0
    assert binary_search.midpoint(5, 5) == 5


def test_midpoint_massive():
    assert binary_search.midpoint(2**31 - 4, 2**31 - 2) == 2**31 - 3


def test_binary_search_found():
    lst = [1, 3, 5, 7, 9]
    target = 7
    assert binary_search.binary_search(lst, target) == 3


def test_binary_search_first():
    lst = [1, 3, 5, 7, 9]
    target = 1
    assert binary_search.binary_search(lst, target) == 0


def test_binary_search_last():
    lst = [1, 3, 5, 7, 9]
    target = 9
    assert binary_search.binary_search(lst, target) == 4


def test_binary_search_not_found():
    lst = [1, 3, 5, 7, 9]
    target = 4
    assert binary_search.binary_search(lst, target) == -1


def test_binary_search_empty():
    lst = []
    target = 1
    assert binary_search.binary_search(lst, target) == -1
