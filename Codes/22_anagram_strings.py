def is_anagram(str1, str2):
    """
    Return True if two strings are anagrams.
    Anagrams contain the same letters in a different order.
    """

    # Remove spaces and convert both strings to lowercase.
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Compare the letters in both strings.
    return sorted(str1) == sorted(str2)


# Run the program directly when this file is executed.
if __name__ == "__main__":
    first = input("Enter the first string: ")
    second = input("Enter the second string: ")

    if is_anagram(first, second):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")
