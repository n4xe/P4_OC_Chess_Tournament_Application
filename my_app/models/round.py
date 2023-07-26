import json
import random
from datetime import datetime, timedelta

class Round:
    def __init__(self, match_list):
        self._match_list = match_list
        self._start_time = None
        self._end_time = None

        pass

    @classmethod
    def get_match_list(cls):
        with open('data/tournament_database.json', 'r+') as file:
            tournament_data = json.load(file)
            players = tournament_data[-1]["Player list"]  # Use the last tournament

            if tournament_data[-1]['Actual round'] == 1:
                random.shuffle(players)  # Randomly shuffle the players in the tournament

                players_pair = []
                for i in range(0, len(players), 2):  # Iteration de 2 en 2
                    if i + 1 < len(players):  # Check if there are 2 players left
                        players_pair.append([players[i], players[i + 1]])  # Creation of pairs

            else:
                # Sort players according to their score
                sorted_players = sorted(players, key=lambda player: tournament_data[-1]["Players score"][player],
                                        reverse=True)

                # Generate pairs for next rounds
                players_pair = []
                used_players = set()

                for i in range(0, len(sorted_players), 2):
                    if i + 1 < len(sorted_players):
                        player1 = sorted_players[i]
                        player2 = sorted_players[i + 1]

                        # Check if players already played against
                        if (player1, player2) not in used_players and (player2, player1) not in used_players:
                            players_pair.append([player1, player2])
                            used_players.add((player1, player2))
                            used_players.add((player2, player1))

            # Display created pairs
            for i, match in enumerate(players_pair):
                print(f"Match {i + 1}: {match}")

            round_key = f"Round {tournament_data[-1]['Actual round']}:"
            pairs_dict = {round_key: {"Match List": players_pair}}

            # Check if the "Round list" key exists and initialize an empty dictionary if it is None
            if tournament_data[-1].get("Round list") is None:
                tournament_data[-1]["Round list"] = {}

            # Add new pairs to previous match list
            tournament_data[-1]["Round list"].update(pairs_dict)


            # Save pairs in the tournament JSON file with indentation for better readability
            file.seek(0)
            json.dump(tournament_data, file, indent=4)

            return cls(players_pair)

    @classmethod
    def add_date(cls):
        with open('data/tournament_database.json', 'r+') as file:
            tournament_data = json.load(file)
            round_key = f"Round {tournament_data[-1]['Actual round']}:"
            round_data = tournament_data[-1]["Round list"][round_key]

            # Calculate round dates
            start_date = datetime.strptime(tournament_data[-1]['Starting date'], "%d/%m/%Y")
            end_date = datetime.strptime(tournament_data[-1]['Ending date'], "%d/%m/%Y")
            tournament_duration = end_date - start_date
            round_duration = tournament_duration / tournament_data[-1]['Number of rounds']
            round_start_date = start_date + round_duration * (tournament_data[-1]['Actual round'] - 1)
            round_end_date = round_start_date + round_duration

            # Adjust round start date based on previous rounds' end date
            if tournament_data[-1]['Actual round'] > 1:
                previous_round_key = f"Round {tournament_data[-1]['Actual round'] - 1}:"
                previous_round_end_date = datetime.strptime(
                    tournament_data[-1]["Round list"][previous_round_key]["Dates"]["End Date"], "%d/%m/%Y %H:%M"
                )
                round_start_date = max(round_start_date, previous_round_end_date)

            # Define time range for round start and end
            start_time_range = datetime.strptime("07:00", "%H:%M").time()
            end_time_range = datetime.strptime("14:00", "%H:%M").time()

            # Combine date and time for round start and end
            round_start_date = datetime.combine(round_start_date.date(), start_time_range)
            round_end_date = datetime.combine(round_end_date.date(), end_time_range)

            round_data["Dates"] = {
                "Start Date": round_start_date.strftime("%d/%m/%Y %H:%M"),
                "End Date": round_end_date.strftime("%d/%m/%Y %H:%M")
            }

            # Save updated tournament data in the JSON file with indentation for better readability
            file.seek(0)
            json.dump(tournament_data, file, indent=4)

    def add_score(self, match_results):
        with open('data/tournament_database.json', 'r+') as file:
            tournament_data = json.load(file)
            round_key = f"Round {tournament_data[-1]['Actual round']}:"
            round_data = tournament_data[-1]["Round list"][round_key]

            # Add the match results
            round_data["Match Result"] = match_results

            # Calculate the players' scores
            player_list = tournament_data[-1]["Player list"]
            scores = tournament_data[-1].get("Players score", {player: 0 for player in player_list})
            for match_result in match_results:
                for player_result in match_result:
                    player = player_result[0]
                    score = player_result[1]
                    scores[player] = scores.get(player, 0) + score  # Add score to existing or initialize if not exists

            # Update the players' scores in the tournament data
            tournament_data[-1]["Number of rounds"] = tournament_data[-1].get("Number of rounds", 0)
            tournament_data[-1]["Players score"] = scores

            # Rewrite the updated data to the file
            file.seek(0)
            json.dump(tournament_data, file, indent=4)
            file.truncate()




