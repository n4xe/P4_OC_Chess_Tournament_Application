import json


class TournamentView:

    @classmethod
    def display_tournaments(cls):
        with open('data/tournament_database.json', 'r') as file:
            tournaments_data = json.load(file)

        # Tournament's number display
        for i, tournament in enumerate(tournaments_data, start=1):
            name = tournament['Name']
            print(f"Tournament's {i}: {name}")

        # Ask user to select a tournament
        selected_tournament = input("Please enter the tournament's number: ")

        # Check number validity
        if not selected_tournament.isdigit() or int(selected_tournament) < 1 or int(selected_tournament) > len(
                tournaments_data):
            print("Invalid tournament number.")
        else:
            index = int(selected_tournament) - 1
            tournament = tournaments_data[index]
            name = tournament['Name']
            starting_date = tournament['Starting date']
            ending_date = tournament['Ending date']
            location = tournament['Place']
            print("Tournament details :")
            print(f"Tournament's name : {name}")
            print(f"Starting date : {starting_date}")
            print(f"Ending date: {ending_date}")
            print(f"Place: {location}")

            choice = input(
                "Tournament details: Would you like to see the players in alphabetical order (yes/no): ")

            if choice.lower() == "yes":
                player_list = tournament["Player list"]
                print("Players by alphabetical order :")
                for player in sorted(player_list):
                    print(player)

            choice = input(
                "Tournament details: Would you like to see the rounds/matches (yes/no) ")
            if choice.lower() == "yes":
                round_list = tournament["Round list"]
                for round_name, round_data in round_list.items():
                    print(f"\nRound: {round_name}")
                    match_list = round_data["Match List"]
                    match_result = round_data["Match Result"]

                    for i, match in enumerate(match_list):
                        player1, player2 = match
                        result = match_result[i]
                        print(f"\nMatch {i + 1}:")
                        print(f"{player1} vs {player2}")
                        print(f"Result: {result[0][1]} - {result[1][1]}")
