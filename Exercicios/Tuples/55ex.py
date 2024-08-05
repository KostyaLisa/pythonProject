# Create a program that has a tuple with
# game names and their respective
# prices in sequence.
#
# At the end, show a price list
# organized as a table.
game_names = ("Game 1", "Game 2", "Game 3", "Game 4")
game_prices = (19.99, 29.99, 49.99, 9.99)

# Print the table header
print("Game Name\tPrice")
print("--------------------")

# Loop through the game names and prices
for i in range(len(game_names)):
    print(f"{game_names[i]}\t\t${game_prices[i]:.2f}")

