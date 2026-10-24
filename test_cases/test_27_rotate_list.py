import importlib

# Import Program 27.
module = importlib.import_module("27_rotate_list")

# Get the function to test.
rotate_list = module.rotate_list


# Test 1: Rotate a list to the right by two positions.
def test_rotate_by_two():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


# Test 2: Rotate by zero positions.
def test_rotate_by_zero():
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]


# Test 3: Rotate an empty list.
def test_empty_list():
    assert rotate_list([], 2) == []


# Test 4: Rotate by more positions than the list length.
def test_large_rotation():
    assert rotate_list([1, 2, 3], 4) == [3, 1, 2]


# Test 5: Rotate a single-element list.
def test_single_element():
    assert rotate_list([7], 3) == [7]
