from players.information import Player
import json
import os
import datetime
class Tournament:
    """
       attributes : name, place, starting date, description, player list, round list, number of rounds
    """
    def __init__(self, name, place, starting_date, description, player_list, information, round_list=None,
                 number_of_rounds=4):
        self._name = name
        self._place = place
        self._starting_date = starting_date
        self._round_list = round_list
        self._player_list = player_list
        self._description = description
        self._number_of_rounds = number_of_rounds
        self._information = information


    @classmethod
    def get_tournament_information(cls):
        name = input("Enter tournament_information's name: ")
        place = input("Enter tournament_information's place: ")
        starting_date = input("Enter tournament_information's starting date (DD/MM/YYYY): ")
        description = input("Enter tournament_information's description: ")
        with open('players/players_database.json', 'r') as file:
            player_data = json.load(file)

        player_list = [f"{player['First name']} {player['Last name']}" for player in player_data]
        information = {"Name": name, "Place": place, "Starting date": starting_date, "Player list": player_list,
                       "Description": description}
        print(information)
        return cls(name, place, starting_date, description, player_list, information)

    def store_tournament_information(self):
        if os.path.isfile('tournament_information/tournament_database.json'):
            with open('tournament_information/tournament_database.json', 'r') as file:
                existing_data = json.load(file)

        else:
            existing_data = []

        existing_data.append(self._information)

        with open('tournament_information/tournament_database.json', 'w') as file:
            json.dump(existing_data, file, indent=4)
            file.write('\n')  # Add a new line after the entries

        print("The", self._name, "tournament_information has been created. It is located in ", self._place, "where ",
              self._player_list, " will try to win it.")

    @classmethod
    def add_a_player(self):
        with open('tournament_information/tournament_database.json', 'r') as file:
            existing_data = json.load(file)
