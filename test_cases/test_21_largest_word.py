import importlib

module = importlib.import_module("21_largest_word")

largest_word = module.largest_word


# Test 1: Find the longest word in a normal sentence.
def test_simple_sentence():
    assert largest_word("I love programming") == "programming"


# Test 2: Ignore punctuation around words.
def test_punctuation_is_ignored():
    assert largest_word("Hello, world!") == "Hello"


# Test 3: Return the first word when lengths are equal.
def test_tie_returns_first_word():
    assert largest_word("cat dog bat") == "cat"


# Test 4: Handle a sentence containing one word.
def test_single_word():
    assert largest_word("Python") == "Python"


# Test 5: Handle an empty sentence.
def test_empty_sentence():
    assert largest_word("") == ""
