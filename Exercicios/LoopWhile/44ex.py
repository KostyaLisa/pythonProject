import math

n = int(input("number"))
b = math.factorial(n)
print(b)

numero = int(input("Number"))

contador = numero
factorial = 1
while contador > 0:
    factorial *= contador - 1
    contador -= 1
    if contador == 1:
        print(f'{contador}={factorial}' ,end='')

    else:
        print(f'{contador} X ', end='')
print(contador)