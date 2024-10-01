# Create a program that reads a number of
# 0 to 20 entered by the user.
# Then you must show in full the
# number entered.


print("Enter a number  0 and 20: ")

list = []

for i in range(1, 21):
    number = int(input(f"Enter number {i}: "  ))
    list.append(number)

print(list)

