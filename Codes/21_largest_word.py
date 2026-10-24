import string


def largest_word(sentence):
    """
    Return the longest word in the sentence.

    - Ignore punctuation around words.
    - If two words have the same length, return the first.
    - If the sentence has no words, return an empty string.
    """

    # Start with an empty string to store the longest word.
    largest = ""

    # Check each word in the sentence.
    for word in sentence.split():

        # Remove punctuation from the beginning and end of the word.
        clean = word.strip(string.punctuation)

        # Update the largest word if the current word is longer.
        if len(clean) > len(largest):
            largest = clean

    # Return the longest word.
    return largest


# Run the program directly when this file is executed.
if __name__ == "__main__":
    text = input("Enter a sentence: ")
    print("Largest word:", largest_word(text))
