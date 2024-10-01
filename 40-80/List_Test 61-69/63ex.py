# Create a program that creates guesses for
# o Euro millions. The program must
# ask how many keys will be generated
# and must randomly draw 5 numbers
# from 1 to 50 [without repeating] and 2 stars
# 1 to 12 [without repeating]. Each draw must
# be stored in a composite list.


import random

def generate_numbers():
    numbers = random.sample(range(1, 51), 5)
    stars = random.sample(range(1, 13), 2)
    return numbers + stars

def main():
    num_keys = int(input("How many keys will be generated? "))
    guesses = []

    for _ in range(num_keys):
        guess = generate_numbers()
        guesses.append(guess)

    print("Generated guesses:")
    for guess in guesses:
        print(guess)


if __name__ == "__main__":
    main() # Call the main function
    # When running this program from the command line, it will generate guesses for o Euro millions.

    # When running this program in a Python environment, you can call the main function directly to generate guesses for o Euro millions.
    # For example:
    #   >>> main()
    #   Generated guesses:
    #   [19, 21, 25, 31, 32, 1]
    #   [12, 8, 11, 1, 20, 10]
    #   ... (more guesses)
    #   >>>
    #   ...
    #   >>> main()
    #   Generated guesses:
    #   [42, 15, 17, 5, 20, 1]
    #   [11, 10, 7, 3, 18, 1]
    #   ... (more guesses)
    #   >>>
    #   ...
