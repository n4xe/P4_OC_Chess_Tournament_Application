import random
import json

import datetime
class Match:
    def __init__(self, player_pairs):
        self._player_pairs = player_pairs
        self._start_time = None
        self._end_time = None

    @classmethod
    def player_pairs(cls):
        with open('tournament_information/tournament_database.json', 'r') as file:
            tournament_data = json.load(file)
            actual_round = tournament_data[0]['Actual round']
            round_key = f"Round {actual_round}:"
            pairs_data = tournament_data[0]["Round list"][round_key]["Match List"]
            player_pairs = []
            for pair in pairs_data:
                player1 = pair[0]
                player2 = pair[1]
                player_pairs.append((player1, player2))
            print(player_pairs)
        return cls(player_pairs)

    def perform_match(self):
        """Effectuer les matchs selon les paires définies"""
        match_results = []

        for pair in self._player_pairs:
            player1 = pair[0]
            player2 = pair[1]
            # Simulation du match
            winner = random.choice([player1, player2, None])  # Ajout de None pour représenter un match nul
            if winner == player1:
                match_results.append(([player1, 1], [player2, 0]))
            elif winner == player2:
                match_results.append(([player1, 0], [player2, 1]))
            else:
                match_results.append(
                    ([player1, 0.5], [player2, 0.5]))  # Les deux joueurs obtiennent un score de 0.5 en cas de match nul

        print(match_results)

        return match_results

    def store_results(self, match_results):
        with open('tournament_information/tournament_database.json', 'r+') as file:
            tournament_data = json.load(file)
            round_key = f"Round {tournament_data[0]['Actual round']}:"
            round_data = tournament_data[0]["Round list"][round_key]

            # Add "Match Result" key to the round data
            round_data["Match Result"] = match_results

            # Rewrite the updated data to the file
            file.seek(0)
            json.dump(tournament_data, file, indent=4, separators=(',', ': '))
            file.truncate()