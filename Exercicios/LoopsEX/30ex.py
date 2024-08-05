#
# Write a program that simulates a
# countdown to the passage of
# year, from 10 to 0, with 1 second
# pause between them
import time

for i in range(10,-1,-1):
    print(i)
    time.sleep(1)
