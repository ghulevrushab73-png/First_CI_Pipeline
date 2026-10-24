import importlib

# Import Program 29.
module = importlib.import_module("29_armstrong_number")

# Get the function to test.
is_armstrong = module.is_armstrong


# Test 1: Check a three-digit Armstrong number.
def test_three_digit_armstrong():
    assert is_armstrong(153) is True


# Test 2: Check a number that is not an Armstrong number.
def test_not_armstrong():
    assert is_armstrong(123) is False


# Test 3: Check zero.
def test_zero():
    assert is_armstrong(0) is True


# Test 4: Check another Armstrong number.
def test_another_armstrong():
    assert is_armstrong(9474) is True


# Test 5: Check a negative number.
def test_negative_number():
    assert is_armstrong(-153) is False
