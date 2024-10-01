import random

list = list(random.randint(1, 20) for _ in range(9))

list.sort()

print(list)

list.reverse()

print(list)

listonents = [1, 545, 3, 5, 6, 7, 8, 9, 10, 11]

listonents.sort(reverse=True)

print(listonents)
