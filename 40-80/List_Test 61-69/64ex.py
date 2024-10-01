#
# Create a program that sorts the order of
# played in a game by “throwing a die at the
# air". Each player will have a number
# random associated within a
# dictionary. At the end, order the ranking
# to see the play order.


import random

# Create a dictionary to store players and their scores
players = {
    "Player 1": random.randint(1, 6),
    "Player 2": random.randint(1, 6),
    "Player 3": random.randint(1, 6),
    "Player 4": random.randint(1, 6),
}

# Sort the dictionary by values (scores) in descending order
sorted_players = dict(sorted(players.items(), key=lambda item: item[1], reverse=True))

# Print the sorted ranking
print("Sorted Ranking:")
for rank, (player, score) in enumerate(sorted_players.items(), start=1):
    print(f"{rank}. {player}: {score}")


