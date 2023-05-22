import json
import random
class Round:
    def __init__(self, match_list):
        self._match_list = match_list
        self._start_time = None
        self._end_time = None

        pass

    @classmethod
    def get_match_list(cls):
        with open('tournament_information/tournament_database.json', 'r+') as file:
            tournament_data = json.load(file)
            players = tournament_data[0]["Player list"]

            if tournament_data[0]['Actual round'] == 1:
                random.shuffle(players)  # Randomly shuffle the players in the tournament

                players_pair = []
                for i in range(0, len(players), 2):  # Iteration of 2 in 2
                    if i + 1 < len(players):  # Check if there are 2 players left
                        players_pair.append([players[i], players[i + 1]])  # Creation of pairs
                        print(players_pair)

            else:
                # Trier les joueurs en fonction de leur score
                sorted_players = sorted(players, key=lambda player: tournament_data[0]["Players score"][player],
                                        reverse=True)

                # Générer les paires pour les matchs suivants
                players_pair = []
                used_players = set()

                for i in range(0, len(sorted_players), 2):
                    if i + 1 < len(sorted_players):
                        player1 = sorted_players[i]
                        player2 = sorted_players[i + 1]

                        # Vérifier si les joueurs se sont déjà affrontés
                        if (player1, player2) not in used_players and (player2, player1) not in used_players:
                            players_pair.append([player1, player2])
                            used_players.add((player1, player2))
                            used_players.add((player2, player1))

            # Afficher les paires créées
            for i, match in enumerate(players_pair):
                print(f"Match {i + 1}: {match}")

            round_key = f"Round {tournament_data[0]['Actual round']}:"
            pairs_dict = {round_key: {"Match List": players_pair}}

            # Vérifier si la clé "Round list" existe et initialiser un dictionnaire vide si elle est None
            if tournament_data[0]["Round list"] is None:
                tournament_data[0]["Round list"] = {}

            # Ajouter les nouvelles paires à la liste des matchs précédente
            tournament_data[0]["Round list"].update(pairs_dict)

            # Enregistrer les paires dans le fichier JSON du tournoi avec une indentation pour une meilleure lisibilité
            file.seek(0)
            json.dump(tournament_data, file, indent=4)

            print(players_pair)
            return cls(players_pair)

    def add_score(self, match_results):
        with open('tournament_information/tournament_database.json', 'r+') as file:
            tournament_data = json.load(file)
            round_key = f"Round {tournament_data[0]['Actual round']}:"
            round_data = tournament_data[0]["Round list"][round_key]

            # Add the match results
            round_data["Match Result"] = match_results

            # Calculate the players' scores
            player_list = tournament_data[0]["Player list"]
            scores = tournament_data[0].get("Players score", {player: 0 for player in player_list})
            for match_result in match_results:
                for player_result in match_result:
                    player = player_result[0]
                    score = player_result[1]
                    scores[player] = scores.get(player, 0) + score  # Add score to existing or initialize if not exists

            # Update the players' scores in the tournament data
            tournament_data[0]["Number of rounds"] = tournament_data[0].get("Number of rounds",
                                                                            0)  # Ensure the "Number of rounds" key exists
            tournament_data[0]["Players score"] = scores

            # Rewrite the updated data to the file
            file.seek(0)
            json.dump(tournament_data, file, indent=4)
            file.truncate()