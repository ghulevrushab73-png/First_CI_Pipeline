import importlib

# Import Program 26.
module = importlib.import_module("26_sum_of_list")

# Get the function to test.
sum_of_list = module.sum_of_list


# Test 1: Calculate the sum of ordinary numbers.
def test_sum_of_numbers():
    assert sum_of_list([10, 20, 30, 40]) == 100


# Test 2: Calculate the sum of an empty list.
def test_empty_list():
    assert sum_of_list([]) == 0


# Test 3: Calculate the sum of negative numbers.
def test_negative_numbers():
    assert sum_of_list([-1, -2, -3]) == -6


# Test 4: Calculate the sum of a list containing zero.
def test_numbers_with_zero():
    assert sum_of_list([0, 5, 10]) == 15


# Test 5: Calculate the sum of a single number.
def test_single_number():
    assert sum_of_list([7]) == 7
