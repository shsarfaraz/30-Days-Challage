import pytest
from calculator_app import calculate

def test_add():
    assert calculate(1, 2, "add") == 3
    assert calculate(-1, 1, "add") == 0
    assert calculate(0, 0, "add") == 0

def test_subtract():
    assert calculate(5, 3, "subtract") == 2
    assert calculate(3, 5, "subtract") == -2
    assert calculate(0, 0, "subtract") == 0

def test_multiply():
    assert calculate(2, 3, "multiply") == 6
    assert calculate(-2, 3, "multiply") == -6
    assert calculate(0, 5, "multiply") == 0

def test_divide():
    assert calculate(6, 3, "divide") == 2
    assert calculate(5, 2, "divide") == 2.5
    assert calculate(10, 0, "divide") == "Cannot divide by zero!"
    assert calculate(0, 5, "divide") == 0
