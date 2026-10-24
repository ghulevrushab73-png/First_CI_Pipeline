import importlib

# Import the program because its filename starts with a number.
module = importlib.import_module("22_anagram_strings")

# Get the function we want to test.
is_anagram = module.is_anagram


# Test 1: Check two strings that are anagrams.
def test_basic_anagram():
    assert is_anagram("listen", "silent") is True


# Test 2: Check two strings that are not anagrams.
def test_not_anagram():
    assert is_anagram("hello", "world") is False


# Test 3: Check whether spaces are ignored.
def test_spaces_are_ignored():
    assert is_anagram("dirty room", "dormitory") is True


# Test 4: Check whether uppercase and lowercase are ignored.
def test_uppercase_is_ignored():
    assert is_anagram("Listen", "Silent") is True


# Test 5: Check strings of different lengths.
def test_different_lengths():
    assert is_anagram("cat", "cats") is False
