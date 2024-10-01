# Improve exercise 67 so that it allows
# the input of multiple players. Set a
# visualization system that allows the
# use search for the results of a
# specific player.


def calculate_average(grades):
    return sum(grades) / len(grades)


def display_player_results(name, grades):
    average = calculate_average(grades)

    if average >= 7:
        status = "approved"
    else:
        status = "not approved"

    print(f"\n{name} has an average grade of {average:.2f} and was {status}.")


def add_player(players):
    name = input("Enter player's name: ")
    grades = list(map(float, input(f"Enter {name}'s grades separated by spaces: ").split()))
    players[name] = grades


def search_player(players):
    search_name = input("Enter the name of the player to search for: ")

    if search_name in players:
        display_player_results(search_name, players[search_name])
    else:
        print(f"No results found for player: {search_name}")


def main():
    players = {}

    while True:
        print("\nOptions:")
        print("1. Add a new player")
        print("2. Search for a player's results")
        print("3. Exit")

        option = input("Choose an option (1, 2, 3): ")

        if option == '1':
            add_player(players)
        elif option == '2':
            search_player(players)
        elif option == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please try again.")


# Run the program
main()

#
# player_info = {
#     "name": "John Doe",
#     "games_played": 10,
#     "goals_per_game": 2
#     # Add more games and goals as needed
# }
#
# # Calculate the average number of goals per game
# player_info["average_goals_per_game"] = float(player_info["goals_per_game"]) / player_info["games_played"]
#
# print(player_info)
# print(f"Average goals per game: {player_info['average_goals_per_game']}")
#
# # Search for a specific player
# search_name = input("Enter the name of the player you want to search for: ")
#
# if search_name in player_info:
#     print(f"Player found: {search_name}")
#     print(f"Games played: {player_info[search_name]['games_played']}")
#     print(f"Goals per game: {player_info[search_name]['goals_per_game']}")
#     print(f"Average goals per game: {player_info[search_name]['average_goals_per_game']}")
#     print()
#     print("Game Order:")
#     for game_number, goals in enumerate(player_info[search_name]['goals_per_game'], start=1):
#         print(f"Game {game_number}: {goals} goals")
#         print()
#         print("Game Stats:")
#         print(f"Total goals: {sum(player_info[search_name]['goals_per_game'])}")
#         print(f"Average goals per game: {player_info[search_name]['average_goals_per_game']}")
#         print()
#         print("----------------------------------------")
#
#     else:
#         print("Player not found.")
#         print()
#         print("----------------------------------------")
#
# # Add more players
# player_info["Jane Doe"] = {
#     "games_played": 8,
#     "goals_per_game": [2, 3, 1, 4, 5, 4, 1, 3, 2, 4]
# }
#
# player_info["Mark Johnson"] = {
#     "games_played": 12,
#     "goals_per_game": [3, 4, 2, 4, 5, 3, 1, 3, 2, 4, 6, 2]
# }
