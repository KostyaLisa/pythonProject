
numeros = list()
numerosTemp = list()
somaPares = 0
somaSomaColuma = 0
maiorTerceiraLinba = 0

for linda in range(3):
    for c in range(3):
        numerosTemp.append(int(input(f"Digite um número:")))
        if numerosTemp%2 == 0:
            somaPares += numeros
        if c == 1:
            somaSomaColuma += numeros
        if linda == 2 :
            if c == 0:
                maiorTerceiraLinha = numeros
            else:
                if numeros > maiorTerceiraLinha:
                    maiorTerceiraLinha = numeros



    numeros.append(numerosTemp[:])
    numerosTemp.clear()

for linha in range(3):
    for coluna in range(3):
        print(f"{numeros[linha][coluna]}", end='\t')

    print()

    print(f"\n Soma dos números pares na coluna {somaPares}")
    print(f"{somaSomaColuma}")
    print(f"\n Maior número da terceira linha: {maiorTerceiraLinba}")
