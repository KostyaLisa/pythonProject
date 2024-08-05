import random

number = random.randint(1,10)
count = 0

while True:
    user= int(input("Enter number"))
    if number<user:
        print("hide")
        count += 1
    elif number>user:
        print("low")
        count += 1
    else:
        print(f'You win, attempts {count}')