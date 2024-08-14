#
# aluno = list()
#
# aluno.append(input("Nome: "))
# aluno.append(input("Digital a idade: "))
#
#
# print(f"Nome: {aluno[0]}")
#
# aluno = dict()

# ----------------------------------------------------------------
# aluno["nome"] = input("Nome: ")
# aluno["nome"] = 'Kostya'
# aluno["idade"] = 23
#
# print(aluno.items )
# print(aluno.values)
# print(aluno.keys)
#
# for k, v in aluno.keys():
#     print(f"{k}: {v}")


# ----------------------------------------------------------------

turma = list()
aluno = dict()

for i in range(5):
    aluno["nome"] = input(f"Nome do aluno {i+1}: ")
    aluno["idade"] = int(input(f"Idade do aluno {i+1}: "))
    turma.append(aluno)


print(turma)
