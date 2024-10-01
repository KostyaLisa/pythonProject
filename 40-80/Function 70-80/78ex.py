# Create a program with a function called
# factorial(), which takes two parameters:
# the first will be the number to calculate the
# factorial and the second will be optional and
# logic that indicates whether it will be displayed in the
# screen or not the process of calculating the
# factorial.


def factorial(n, display):
    result = 1
    for i in range(1, n+1):
        result *= i
    if display:
        print(f"The factorial of {n} is: {result}")
    return result
n = int(input("Number: "))
display = input("You should show processing results? (y/n): ").strip().lower() == 'y'
factorial(n, display)


# ----------------------------------------------------------------
# Avto generation ChatGPT

# def Factorial(n, show_process=False):
#     factorial = 1
#     for i in range(1, n + 1):
#         factorial *= i
#         if show_process:  # Отображение процесса, если show_process=True
#             print(f"{i}! = {factorial}")
#
#     return factorial
#
#
# # Пример использования:
# number = int(input("Введите число для вычисления факториала: "))
# show = input("Хотите видеть процесс вычисления? (да/нет): ").strip().lower() == 'да'
#
# result = Factorial(number, show)
# print(f"Факториал числа {number} = {result}")

