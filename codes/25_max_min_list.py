def find_max_min(numbers):
    # Handle an empty list.
    if not numbers:
        raise ValueError("The list cannot be empty.")

    # Assume the first number is both maximum and minimum.
    maximum = numbers[0]
    minimum = numbers[0]

    # Compare each remaining number.
    for number in numbers[1:]:
        if number > maximum:
            maximum = number

        if number < minimum:
            minimum = number

    # Return maximum first, then minimum.
    return maximum, minimum


if __name__ == "__main__":
    numbers = [5, 2, 9, 1, 7]
    maximum, minimum = find_max_min(numbers)

    print("Maximum:", maximum)
    print("Minimum:", minimum)
