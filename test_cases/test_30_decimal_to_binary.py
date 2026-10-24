import importlib

# Import Program 30.
module = importlib.import_module("30_decimal_to_binary")

# Get the function to test.
decimal_to_binary = module.decimal_to_binary


# Test 1: Convert a positive decimal number.
def test_positive_number():
    assert decimal_to_binary(5) == "101"


# Test 2: Convert zero.
def test_zero():
    assert decimal_to_binary(0) == "0"


# Test 3: Convert a power of two.
def test_power_of_two():
    assert decimal_to_binary(8) == "1000"


# Test 4: Convert a larger decimal number.
def test_larger_number():
    assert decimal_to_binary(10) == "1010"


# Test 5: Convert a negative number.
def test_negative_number():
    assert decimal_to_binary(-5) == "-101"
  
