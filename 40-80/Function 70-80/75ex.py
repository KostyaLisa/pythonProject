# Create a program that has a function
# that receives an integer and displays the
# multiplication table of that number.


def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

numbers = input("Number: ")
multiplication_table(int(numbers))