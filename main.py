from players.information import Player
from tournament_information.tournament import Tournament

def main():
    tournament = Tournament.get_tournament_information()
    tournament.store_tournament_information()

main()
