print("----menu----")
print("[ 1 ] ")
print("[ 2 ] ")
print("[ 3 ] ")
print("[ 4 ] ")

num = int(input(" "))

if num == 1:
    print("")
    num1 = int(input(""))
    operation = input("Operation [ + - * / ]").lower()
    num2 = int(input(""))

    if operation == "+":
        print(f"{num1}+{num2} = {num1 + num2}")
    elif operation == "-":
        print(f"{num1}-{num2} = {num1 - num2}")
    elif operation == "-":
        print(f"{num1}+{num2} = {num1 + num2}")
    elif operation == "*":
        print(f"{num1}+{num2} = {num1 + num2}")


