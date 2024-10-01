# Create a program where the user
#
# can enter multiple numbers and save them
# them in a list. If the number entered
#
# is on the list it should not be
# added. At the end, show all
# values  DESCENDING order.


numbers = []
while True:
    num = int(input("Enter a number (or -1 to exit): "))
    if num == -1:
        print("Numbers in descending order:")
        print(numbers)
        numbers.sort(reverse=True)
        print(numbers)

        break
    elif num in numbers:
        print(f"Number {num} already exists in the list.")
    else:
        numbers.append(num)
        print(f"Number {num} added successfully.")

numFirse = []

for i in range(1, 6):
    numPlus = int(input(f'Enter a number {i} '))
    numFirse.append(numPlus)
    print(f'Number {numPlus} added successfully.')
    