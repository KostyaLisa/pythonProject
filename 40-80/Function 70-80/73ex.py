# Create a program that has a function
# that receives several parameters such as
# integer values. The program must
# analyze all the values and say which
# of them is the biggest.


def find_biggest(*args):
    biggest = args[0]
    for num in args:
        if num > biggest:
            biggest = num
    return biggest


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

biggest_number = find_biggest(num1, num2, num3)
print(f"The biggest number is: {biggest_number}")
