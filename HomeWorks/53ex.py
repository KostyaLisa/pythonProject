import random


def generate_random_numbers():
    # Generate 5 random numbers and store them in a tuple
    random_numbers = tuple(random.randint(1, 100) for _ in range(5))

    # Display the list of generated numbers
    print("Generated numbers:", random_numbers)

    # Find and display the smallest number
    smallest_number = min(random_numbers)
    print("Smallest number:", smallest_number)

    # Find and display the largest number
    largest_number = max(random_numbers)
    print("Largest number:", largest_number)


# Call the function to run the program
generate_random_numbers()