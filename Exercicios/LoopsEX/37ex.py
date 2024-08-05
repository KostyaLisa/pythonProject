for i in range(1, 11):
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("prime number")
    else:
        print(number)

num = int(input())
contr = 0
for c in range(0, num):
    if num % (c + 1) == 1:
        contr += 1

        if contr == 2:
            print(f'Prime integer {num}')
        else:
            print(f'Not prime {num}')
