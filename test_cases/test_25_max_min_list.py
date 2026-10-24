import importlib
import pytest

# Import Program 25.
module = importlib.import_module("25_max_min_list")

# Get the function to test.
find_max_min = module.find_max_min


# Test 1: Find maximum and minimum in an ordinary list.
def test_find_max_min():
    assert find_max_min([5, 2, 9, 1, 7]) == (9, 1)


# Test 2: Test a list containing negative numbers.
def test_negative_numbers():
    assert find_max_min([-5, -2, -9, -1]) == (-1, -9)


# Test 3: Test a list containing one number.
def test_single_number():
    assert find_max_min([7]) == (7, 7)


# Test 4: Test a list containing duplicate numbers.
def test_duplicate_numbers():
    assert find_max_min([4, 4, 4]) == (4, 4)


# Test 5: An empty list should raise ValueError.
def test_empty_list():
    with pytest.raises(ValueError):
        find_max_min([])
