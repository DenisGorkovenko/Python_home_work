import pytest


def division_num(a, b):
    if b == 0:
        raise ZeroDivisionError("You cannot divide by zero")
    return a / b


@pytest.mark.parametrize("a, b, expected", [
    (12, 4, 3),
    (-1, 1, -1),
    (10, 2, 5),
    (2, 0, ZeroDivisionError)
])
def test_division_num(a, b, expected):
    if type(expected) == type and issubclass(expected, Exception):
        with pytest.raises(expected):
            division_num(a, b)
    else:
        assert division_num(a, b) == expected
