import datetime
import os
import json


class Player:
    """
    attributes :
    first name,
    name,
    birthday date
    """

    def __init__(self, first_name, last_name, birthday_date, chess_identification, information):
        self._first_name = first_name
        self._last_name = last_name
        self._birthday_date = birthday_date
        self._chess_identification = chess_identification
        self._information = information

    @classmethod
    def get_player_information(cls):
        """
        Ask information to user about first name, name, birthday date and ID of the player to be added.
        """
        first_name = input("Enter player's first name: ")
        last_name = input("Enter player's last name: ")
        birthday_date = input("Enter player's birthday date (DD/MM/YYYY): ")
        chess_identification = input("Enter player's chess ID: ")
        information = {"First name": first_name, "Last name": last_name, "Birthday date": birthday_date,
                       "Chess ID": chess_identification}
        return cls(first_name, last_name, birthday_date, chess_identification, information)

    def set_player_information(self):
        """
        The information stored in the dictionary "information" thanks to the method "input_get_player_information"
        is stored in the players_database.json file
        """
        if os.path.isfile('data/players_database.json'):
            with open('data/players_database.json', 'r') as file:
                existing_data = json.load(file)

        else:
            existing_data = []

        existing_data.append(self._information)

        with open('data/players_database.json', 'w') as file:
            json.dump(existing_data, file, indent=4)
            file.write('\n')  # Add a new line after the entries

        today = datetime.date.today()
        self._birthday_date = datetime.datetime.strptime(self._birthday_date, '%d/%m/%Y')
        age = today.year - self._birthday_date.year - (
                (today.month, today.day) < (self._birthday_date.month, self._birthday_date.day))

        print("The player", self._information["First name"], self._information["Last name"],
              "has correctly been registered. He/She is", age, "years old")
