# Create a program with a tuple with 20
# first place in the Championship
# Spanish Football. Then show:
#
# a) The first 5 classified.
# b) The last 4 classified.
# c) A list of teams in alphabetical order.
# d) The position of the Las Palmas team.


championship = ("Real Madrid", "Barcelona", "Atletico Madrid", "Valencia", "Sevilla", "Getafe", "Villarreal", "Levante",
                "Athletic Bilbao", "Celta Vigo", "Real Sociedad", "Espanyol", "Granada", "Sporting Gijon",
                "Rayo Vallecano", "Almeria", "Granada")

# a) The first 5 classified
print("First 5 classified:")
for i in range(5):
    print(championship[i])
# b) The last 4 classified
print("Last 4 classified:")
for j in range(len(championship) - 4, len(championship)):
    print(championship[j])

# c) A list of teams in alphabetical order
print("\nList of teams in alphabetical order:")
sorted_championship = sorted(championship)
for team in sorted_championship:
    if team != "":
        print(team)
        # d) The position of the Las Palmas team
        if team == "Las Palmas":
            print(f"Position of Las Palmas: {sorted_championship.index(team) + 1}")
            break


#
# first = (championship [0:5])
# print(f'First 5 classified: \n {first}')
# last = (championship [-4::])
# print(f'Last 4 classified: \n {last}')
#
# print(sorted(championship))
#
# num = 0;
# for elemento in championship:
#     if first == 'Las Palmas':
#         break
#     num +=1
#     print(num)
# print(num+1)


