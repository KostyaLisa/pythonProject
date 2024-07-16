teams = (
    "Barcelona", "Real Madrid", "Atletico Madrid", "Sevilla", "Real Sociedad",
    "Villarreal", "Real Betis", "Athletic Bilbao", "Valencia", "Osasuna",
    "Getafe", "Celta Vigo", "Espanyol", "Rayo Vallecano", "Mallorca",
    "Alaves", "Granada", "Cadiz", "Elche", "Las Palmas"
)


def display_championship_info(teams):
    # a) The first 5 classified teams
    print("The first 5 classified teams are:")
    for team in teams[:5]:
        print(team)

    # b) The last 4 classified teams
    print("\nThe last 4 classified teams are:")
    for team in teams[-4:]:
        print(team)

    # c) Teams in alphabetical order
    print("\nTeams in alphabetical order:")
    for team in sorted(teams):
        print(team)

    # d) The position of the Las Palmas team
    las_palmas_position = teams.index("Las Palmas") + 1
    print(f"\nLas Palmas is in position: {las_palmas_position}")


# Call the function to display the information
display_championship_info(teams)