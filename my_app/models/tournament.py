import json
import os
import random

class Tournament:
    """
       attributes : name, place, starting date, description, player list, round list, number of rounds
    """
    def __init__(self, name, place, starting_date, ending_date, description, player_list, information, actual_round=0,
                 round_list=None, number_of_rounds=4):

        self._name = name
        self._place = place
        self._starting_date = starting_date
        self._ending_date = ending_date
        self._round_list = round_list
        self._player_list = player_list
        self._description = description
        self._actual_round = actual_round
        self._number_of_rounds = number_of_rounds
        self._information = information

    @classmethod
    def get_tournament_information(cls):
        """Get tournament information (class attributes) from user in order to save input in the tournament database
         json file"""
        name = input("Enter tournament_information's name: ")
        place = input("Enter tournament_information's place: ")
        starting_date = input("Enter tournament_information's starting date (DD/MM/YYYY): ")
        ending_date = input("Enter tournament_information's ending date (DD/MM/YYYY): ")
        description = input("Enter tournament_information's description: ")
        with open('players/players_database.json', 'r') as file:
            player_data = json.load(file)

        player_list = [f"{player['First name']} {player['Last name']}" for player in player_data]
        information = {"Name": name, "Place": place, "Starting date": starting_date, "Ending date":ending_date,
                       "Player list": player_list, "Description": description}
        print(information)

        return cls(name, place, starting_date, ending_date, description, player_list, information)

    def set_tournament_information(self):
        """Save the information previously given by user into a json file"""

        if os.path.isfile('tournament_information/tournament_database.json'):
            with open('tournament_information/tournament_database.json', 'r') as file:
                existing_data = json.load(file)

        else:
            existing_data = []

        self._information["Actual round"] = self._actual_round
        self._information["Number of rounds"] = self._number_of_rounds
        self._information["Round list"] = self._round_list
        existing_data.append(self._information)

        with open('tournament_information/tournament_database.json', 'w') as file:
            json.dump(existing_data, file, indent=4)
            file.write('\n')  # Add a new line after the entries

        print("The", self._name, "tournament has been created. It is located in ", self._place, "where ",
              ", ".join(str(player) for player in self._player_list), "will try to win it.")

    def start_round(self):
        self._actual_round += 1
        with open('tournament_information/tournament_database.json', 'r+') as file:
            data = json.load(file)
            for tournament_data in data:
                if tournament_data['Name'] == self._name:
                    tournament_data["Actual round"] = self._actual_round
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

    @classmethod
    def add_a_player(cls):
        with open('tournament_information/tournament_database.json', 'r') as file:
            existing_data = json.load(file)

    @classmethod
    def clear_info(cls):
        with open('tournament_information/tournament_database.json', 'w') as file:
            json.dump([], file)
