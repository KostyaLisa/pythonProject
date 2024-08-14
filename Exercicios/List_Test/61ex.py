# Create a program that creates an array
# 3x3 and fill in with values read by the
# keyboard. At the end show the matrix with the
# proper formatting.


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
# print("Matrix:", matrix[0], matrix[1], matrix[2])
