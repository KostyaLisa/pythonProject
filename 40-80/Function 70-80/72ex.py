# Create a program that has a function
# that receives 3 parameters: start, end and
# step. The program must perform 3
# counts through the function.
#
# a) From 1 to 20, every two
# b) From 10 to 0, from 1 to 1
# c) Custom count


def count_numbers(start, end, step):
    count = start
    while count <= end:
        print(count, end=" ")
        count += step
    print()
    count=end


    while count >= start:
        print(count, end=" ")
        count -= step
    print()

# Test cases
count_numbers(1, 20, 2)
count_numbers(10, 0, -1)
