count = 0

sumCount = 0
numbers = 1
while numbers != 0:
    num = int(input('Digite um numero [zero parapr] :'))
if num == 0:
    count += 1
sumCount += num

print(f'faram digitados {count}')
print(f'A soma dos nomerus {sumCount}')
