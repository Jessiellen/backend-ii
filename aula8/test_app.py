from app import multiply, factorial
import pytest

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-1, 5) == -5
    assert multiply(0, 10) == 0

@pytest.mark.parametrize(
    "input, expected",
    [
        (0, 1),
        (1, 1),
        (5, 120),
        (7, 5040),
    ]
)
def test_factorial(input, expected):
    assert factorial(input) == expected
