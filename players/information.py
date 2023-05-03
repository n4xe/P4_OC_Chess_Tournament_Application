import json
import datetime
import os

class Player:
    def __init__(self):

        self.information = {}

    def set_information(self, first_name, name, birthday_date):

        self.information["First name"] = first_name
        self.information["Family name"] = name
        self.information["Birthday date"] = birthday_date
        self.birthday_date = datetime.datetime.strptime(birthday_date, '%d/%m/%Y')

    def store_player_information(self):
        if os.path.isfile('../database.json'):
            with open('../database.json', 'r') as file:
                existing_data = json.load(file)

        else:
            existing_data = []

        print(existing_data)
        print(self.information)

        existing_data.append(self.information)
        print(existing_data)

        with open('../database.json', 'w') as file:
            json.dump(existing_data, file, indent=4)
            file.write('\n')  # Add a new line after the entries

        today = datetime.date.today()
        age = today.year - self.birthday_date.year - (
                    (today.month, today.day) < (self.birthday_date.month, self.birthday_date.day))

        print("The player", self.information["First name"], self.information["Family name"],
              "has correctily been registered. He/She is", age, "years old")

    def update_information(self, first_name, name, new_information):
        with open('../database.json', 'r') as file:
            existing_data = json.load(file)

        for player in existing_data:
            if player["First name"] == first_name and player["Family name"] == name:
                player.update(new_information)
                break
            else:
                print("This player does not exist in the database")

        with open('../database.json', 'w') as file:
            json.dump(existing_data, file, indent=4)
            file.write('\n')

        print("The player", first_name, name, "has been updated with the following information:", new_information)

