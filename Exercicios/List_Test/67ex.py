# Create a program that stores the
# use of a player
# soccer. The program should read the name,
# how many games you played and the amount of
# goals per game and save everything in one
# dictionary. In the dictionary, it should
# calculate the average number of goals per game.


player_info = {
    "name": "John Doe",
    "games_played": 10,
    "goals_per_game": [2, 3, 1, 4, 3, 5, 2, 3, 4, 5],
    # Add more games and goals as needed

    # Calculate the average number of goals per game
    "average_goals_per_game": sum(player_info["goals_per_game"]) / player_info["games_played"]
}

print(player_info)
print(f"Average goals per game: {player_info['average_goals_per_game']}")





