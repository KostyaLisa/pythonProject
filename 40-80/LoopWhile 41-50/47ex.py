qtdNotes =0
media=0
maior=0
menor=0


while True:
    notas = float(input('Digite uma nota'))
    if notas == 999:
        break
    else:
        qtdNotes+= 1
        media += notas

        if qtdNotes ==1:
            maior=notas
            menor= notas
        else:
            if notas> maior:
                maior=notas
            if notas< menor:
                menor = notas

print(qtdNotes)
print(media)
print(maior)
print(menor)