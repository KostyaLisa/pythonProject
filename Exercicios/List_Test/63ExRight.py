import random


palpites = list()
numeros = list()
estrelas = list()

while True:
    numero = random.randint(1, 100)


    if len(palpites) < 3:
        estrela = random.randint(1, 12)

    if numero in numeros:
        continue
    else:
        numeros.append(numero)

    if estrela in estrelas:
        continue
    else:
        estrelas.append(estrela)

    if len(numeros) == 5 and len(estrelas) == 10:

        print(f"Os números sorteados foram: {palpites}")