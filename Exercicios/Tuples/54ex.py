# Create a program that reads 4 values and
# store them in a tuple. At the end display:
#
# a) How many times does the number 7 appear.
# b) In what position was the number 5 entered.
# c) What are the even numbers.
#
# The program must inform you when it is not
# find answer.
import random

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 7, 12, 13, 14, 15, 7)

# a) How many times does the number 7 appear.
count_7 = numbers.count(7)
if count_7 == 0:
    print("Number 7 not found")
else:
    print(f"Number 7 appears {count_7} times")


# lessons

num = tuple (random.randint(1,20) for _ in range(20))
if num.count(8) <= 0 :
    print("Number number not found")
else:
    print(f"Number number appears {num.count(8)} times")


print(f'{5 in num}')
