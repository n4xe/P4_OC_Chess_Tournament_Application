import random
import json


class Match:
    def __init__(self, player_pairs):
        self._player_pairs = player_pairs
        self._start_time = None
        self._end_time = None

    @classmethod
    def player_pairs(cls):
        with open('data/tournament_database.json', 'r') as file:
            tournament_data = json.load(file)
            last_tournament = tournament_data[-1]
            actual_round = last_tournament['Actual round']
            round_key = f"Round {actual_round}:"
            pairs_data = last_tournament["Round list"][round_key]["Match List"]
            player_pairs = []
            for pair in pairs_data:
                player1 = pair[0]
                player2 = pair[1]
                player_pairs.append((player1, player2))
        return cls(player_pairs)

    def perform_match(self):
        """Perform matches according to defined pairs"""
        match_results = []
        for pair in self._player_pairs:
            player1 = pair[0]
            player2 = pair[1]
            # Simulation du match
            winner = random.choice([player1, player2, None])  # Add None to represent a draw
            if winner == player1:
                match_results.append(([player1, 1], [player2, 0]))
            elif winner == player2:
                match_results.append(([player1, 0], [player2, 1]))
            else:
                match_results.append(
                    ([player1, 0.5], [player2, 0.5]))  # Both players score 0.5 in the event of a draw

        print(match_results)

        return match_results

    def store_results(self, match_results):
        with open('data/tournament_database.json', 'r+') as file:
            tournament_data = json.load(file)
            last_tournament_index = len(tournament_data) - 1
            last_tournament = tournament_data[last_tournament_index]
            actual_round = last_tournament['Actual round']
            round_key = f"Round {actual_round}:"
            round_data = last_tournament["Round list"][round_key]

            # Add "Match Result" key to the round data
            round_data["Match Result"] = match_results

            # Rewrite the updated data to the file
            file.seek(0)
            json.dump(tournament_data, file, indent=4, separators=(',', ': '))
            file.truncate()
