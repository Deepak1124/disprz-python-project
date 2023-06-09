import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 5) == 4
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 5) == -5
    assert subtract(-10, -2) == -8

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 10) == 0
    assert multiply(-2, 5) == -10

def test_divide():
    assert divide(10, 2) == 5
    assert divide(0, 5) == 0
    assert divide(-12, -3) == 4
    with pytest.raises(ValueError):
        divide(10, 0)
