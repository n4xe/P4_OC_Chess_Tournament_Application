import json


class TournamentControl:

    @classmethod
    def delete_tournament(cls):
        with open('data/tournament_database.json', 'r') as file:
            tournaments_data = json.load(file)

        # Tournament's number display
        for i, tournament in enumerate(tournaments_data, start=1):
            name = tournament['Name']
            print(f"Tournament {i}: {name}")

        # Ask user to select a tournament
        selected_tournament = input("Please enter the tournament's number to delete : ")

        # Validity check
        if not selected_tournament.isdigit() or int(selected_tournament) < 1 or int(selected_tournament) > len(
                tournaments_data):
            print("Invalid tournament number.")
        else:
            index = int(selected_tournament) - 1
            deleted_tournament = tournaments_data.pop(index)
            name = deleted_tournament['Name']
            print(f"'{name}' tournament successfully deleted.")

            # Json update
            with open('data/tournament_database.json', 'w') as file:
                json.dump(tournaments_data, file, indent=4)
