import json
import datetime
import os

class Player:
    """
    attributes :
    first name
    name
    birthday date
    """
    def __init__(self, first_name, last_name, birthday_date, chess_identification, information):
        self._first_name = first_name
        self._last_name = last_name
        self._birthday_date = birthday_date
        self._chess_identification = chess_identification
        self._information = information

    @classmethod
    def input_get_player_information(cls):
        first_name = input("Enter player's first name: ")
        last_name = input("Enter player's last name: ")
        birthday_date = input("Enter player's birthday date (DD/MM/YYYY): ")
        chess_identification = input("Enter player's chess ID: ")
        information = {"First name": first_name, "Last name": last_name, "Birthday date": birthday_date,
                   "Chess ID": chess_identification}
        return cls(first_name, last_name, birthday_date, chess_identification, information)

    def store_player_information(self):
        if os.path.isfile('players/players_database.json'):
            with open('players/players_database.json', 'r') as file:
                existing_data = json.load(file)

        else:
            existing_data = []

        existing_data.append(self._information)

        with open('players/players_database.json', 'w') as file:
            json.dump(existing_data, file, indent=4)
            file.write('\n')  # Add a new line after the entries

        today = datetime.date.today()
        self._birthday_date = datetime.datetime.strptime(self._birthday_date, '%d/%m/%Y')
        age = today.year - self._birthday_date.year - (
                    (today.month, today.day) < (self._birthday_date.month, self._birthday_date.day))

        print("The player", self._information["First name"], self._information["Last name"],
              "has correctily been registered. He/She is", age, "years old")

    @classmethod
    def update_player_information(cls):
        with open('players/players_database.json', 'r') as file:
            existing_data = json.load(file)

        first_name = input("Enter the first name of the player information you want to update: ")
        last_name = input("Enter the last name of the player information you want to update: ")
        found_player = False

        for player in existing_data:
            if player["First name"] == first_name and player["Last name"] == last_name:
                found_player = True
                print("Player found. Current information: ")
                print(player)

                while True:
                    update_choice = input("What information do you want to update? "
                                          "('F' for first name, 'L' for last name, "
                                          "'B' for birthday date, 'C' for chess ID, "
                                          "'Q' to quit updating): ").upper()
                    if update_choice == "Q":
                        break
                    elif update_choice == "F":
                        new_first_name = input("Enter new first name: ")
                        player["First name"] = new_first_name
                    elif update_choice == "L":
                        new_last_name = input("Enter new last name: ")
                        player["Last name"] = new_last_name
                    elif update_choice == "B":
                        new_birthday_date = input("Enter new birthday date (DD/MM/YYYY): ")
                        player["Birthday date"] = new_birthday_date
                    elif update_choice == "C":
                        new_chess_id = input("Enter new chess ID: ")
                        player["Chess ID"] = new_chess_id
                    else:
                        print("Invalid choice.")

                print("Updated information: ")
                print(player)
                break

        if not found_player:
            print("No player found with the given name.")

        with open('players/players_database.json', 'w') as file:
            json.dump(existing_data, file, indent=4)
            file.write('\n')  # Add a new line after the entries

