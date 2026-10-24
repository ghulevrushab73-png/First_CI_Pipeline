def sum_of_list(numbers):
    # Initialize the total.
    total = 0

    # Add each number to the total.
    for number in numbers:
        total += number

    # Return the calculated sum.
    return total


if __name__ == "__main__":
    numbers = [10, 20, 30, 40]
    print("List:", numbers)
    print("Sum:", sum_of_list(numbers))
