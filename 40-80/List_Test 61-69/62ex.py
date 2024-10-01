# Create a program that creates an array
# 3x3 and fill in with values read by the
# keyboard. At the end show the matrix with the
# proper formatting.

# Improve exercise 61 by displaying on
# end.
# a) The sum of all even values.
# b) The sum of the values in the second column.
# c) The highest value in the third line.

matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(3):
    for j in range(3):
        matrix[i][j] = int(input(f"Enter value for [{i},{j}]: "))

        print(matrix[i])

for i in range(3):
    for j in range(3):
        print(f"{matrix[i][j]:3}", end="\t")
    print()

for i in range(3):
    for j in range(3):
        even_sum = sum([matrix[i][j] for i in range(3)])
        print(f"Sum of even values in line : {even_sum}")

        second_column_sum = sum(matrix[j][1] for j in range(3))
        print(f"Sum of values in second column: {second_column_sum}")

        max_value = max(matrix[i][j] for j in range(3))
        print(f"Highest value in line {i + 1}: {max_value}")
    print()
