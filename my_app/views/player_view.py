import json


class PlayerView:
    @classmethod
    def display_players(cls):
        with open('data/players_database.json', 'r') as file:
            players_data = json.load(file)

        # Extract first name and last name from each player's data
        players = []
        for player_data in players_data:
            first_name = player_data['First name']
            last_name = player_data['Last name']
            players.append((first_name, last_name))

        # Sort players alphabetically by last name
        players.sort(key=lambda x: x[1])

        # Display players in the terminal
        for player in players:
            first_name, last_name = player
            print(f"{last_name}, {first_name}")
