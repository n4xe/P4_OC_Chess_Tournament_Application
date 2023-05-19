import json
import random
class Round:
    def __init__(self, match_list):
        self._match_list = match_list
        self._start_time = None
        self._end_time = None

        pass

    @classmethod
    def get_pairs(cls):

        """ Generate pairs according to the actual round.
        For the first one, pairs are generated randomly
        For the others, pairs are generated according to the score of the players (first vs second, third vs fourth).
        If they already met, the ...TO DO"""

        with open('tournament_information/tournament_database.json', 'r') as file:
            tournament_data = json.load(file)
            players = tournament_data[0]["Player list"]

            if tournament_data[0]['Actual round'] == 0:
                random.shuffle(players)  # Randomly shuffle the players in the tournament

                players_pair = []
                for i in range(0, len(players), 2):  # Iteration of 2 in 2
                    if i + 1 < len(players):  # Check if there are 2 players left
                        players_pair.append([players[i], players[i + 1]])  # Creation of pairs
                        print(players_pair)

            else:
                # Generation of pairs according to the score of the players
                sorted_players = sorted(players, key=lambda player: player.get('score', 0), reverse=True)
                players_pair = []
                for i in range(0, len(sorted_players), 2):
                    if i + 1 < len(sorted_players):
                        players_pair.append([sorted_players[i], sorted_players[i + 1]])

            # Afficher les paires créées
            for i, match in enumerate(players_pair):
                print(f"Match {i + 1}: {match}")

            round_key = f"Round {tournament_data[0]['Actual round']}:"
            pairs_dict = {round_key: players_pair}

            tournament_data[0]["Round list"] = pairs_dict

            # Enregistrer les paires dans le fichier JSON du tournoi avec une indentation pour une meilleure lisibilité
            with open('tournament_information/tournament_database.json', 'w') as file:
                json.dump(tournament_data, file, indent=4)

            return cls(players_pair)

    def set_pairs(self):
        self._match_list.append(players_pair)
        pass


    def start_round(self, Tournament):
        Tournament.start_round()
        pass



