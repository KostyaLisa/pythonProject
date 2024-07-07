import random
from time import sleep

number = random.randint(0, 7)

print("-="*11)
sleep(1)
print("guess number")

print()

your = int(input())

if your == number:
    print("you win")
elif your>number:
    print()
elif your<number:
    print()
else:
    print("you lose")