# Create a program with a function that will
# function like the input() function, in
# However, it will validate the
# accept only a numeric value.


def get_number():
    while True:
        try:
            number = float(input("Enter a number: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


print(get_number())
