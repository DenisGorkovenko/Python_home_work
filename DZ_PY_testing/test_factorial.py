import pytest


def factorial(n):
    if n < 0:
        raise ValueError
    elif n == 0 or n == 1:
        return n
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def test_factorial_positive():
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(8) == 40320


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-5)


def test_factorial_edge_case():
    assert factorial(0) == 0
    assert factorial(1) == 1
    with pytest.raises(ValueError):
        factorial(-1)
