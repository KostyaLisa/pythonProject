# num1=8
# num2=8
# num3=8
# num4=8
# num5=10
#
# calculate = (num5+num4+num3+num2+num1)/5
#
# if calculate >=9.5:
#     print(f"passou")
# elif calculate < 8 or calculate <= 9.5 :
#     print(f"em recuperação")
# elif calculate < 8:
#     print(f"reprova")
nota1 = float(input("Enter nota 1"))
nota2 = float(input("Enter nota 2"))
nota3 = float(input("Enter nota 3"))
nota4 = float(input("Enter nota 4"))
nota5 = float(input("Enter nota 5"))

result = nota1 + nota2 + nota3 + nota4 + nota5
media = result / 5

if media >= 9.5:
    print(f"sdsd")
elif media < 8:
    print(f"")
else:
    print()
