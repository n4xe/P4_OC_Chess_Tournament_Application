from players.information import *
from tournament_information.tournament import Tournament
from players.match import Match
from players.round import Round

def main():
    tournament1 = Tournament.get_tournament_information()
    tournament1.set_tournament_information()

    for round_number in range(1, tournament1._number_of_rounds + 1):
        tournament1.start_round()
        current_round = Round.get_match_list()
        current_match = Match.player_pairs()
        current_match_results = current_match.perform_match()
        current_match.store_results(current_match_results)
        current_round.add_score(current_match_results)

        # Optionally, you can check if it's the last round and perform additional actions
        if round_number == tournament1._number_of_rounds:
            # Perform actions for the last round
            pass


main()
