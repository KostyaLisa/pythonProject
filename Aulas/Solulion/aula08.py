turma = list()
aluno = list()

for i in range(0, 3):
    aluno.append(input("Enter  o nome do aluno: "))
    aluno.append(input("Enter o ID do aluno: "))
    aluno.append(input("Enter a media do aluno: "))
    turma.append(aluno)

print("Alunos da turma:", turma)

for linha in range(0,3):
    for coluna in range(0,3):
        print(f"Aluno: {turma[linha][coluna]}", end="\t")
    print()

