# Create a program that generates 5 numbers
# random within a tuple. After
# shows the list of generated numbers, the
# smallest and largest.

import random

numbers = tuple(random.randint(1, 100) for _ in range(5))
print("Generated numbers:", numbers)

smallest = min(numbers)
largest = max(numbers)

print("Smallest number:", smallest)
print("Largest number:", largest)

big=small =numbers[0]

for i in numbers:
    if i > big:
        big=i
    if i >small:
        small = i

print(f'big number : {big} ')
print(f'small number : {small}')
