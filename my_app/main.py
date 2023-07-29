from my_app.views.player_view import PlayerView
from my_app.views.tournament_view import TournamentView
from my_app.models.player import Player
from my_app.models.tournament import Tournament
from my_app.models.match import Match
from my_app.models.round import Round
from my_app.controllers.player_controller import PlayerController
from my_app.controllers.tournament_controller import TournamentControl
from my_app.views.main_view import MainView


def main():
    while True:
        choice = MainView.main_menu()

        if choice == "1":
           first_menu_choice = MainView.first_menu()
           if first_menu_choice == "1":
               player = Player.get_player_information()
               player.set_player_information()
               pass
           elif first_menu_choice == "2":
               tournament = Tournament.get_tournament_information()
               tournament.set_tournament_information()
               for round_number in range(1, tournament.number_of_rounds + 1):
                    print("\n Round ", round_number, "\n")
                    tournament.start_round()
                    current_round = Round.get_match_list()
                    Round.add_date()
                    current_match = Match.player_pairs()
                    current_match_results = current_match.perform_match()
                    current_match.store_results(current_match_results)
                    current_round.add_score(current_match_results)

                    user_input = input(
                        "Press ""Y"" to continue : ")
                    if user_input.lower() != "y":
                        break
                        pass
           elif first_menu_choice == "b":
                continue
           else:
                MainView.invalid_option()

        elif choice == "2":
            second_menu_choice = MainView.second_menu()

            if second_menu_choice == "1":
                PlayerView.display_players()
                pass
            elif second_menu_choice == "2":
                TournamentView.display_tournaments()
                pass
            elif second_menu_choice == "b":
                continue
            else:
                MainView.invalid_option()

        elif choice == "3":
            third_menu_choice = MainView.third_menu()
            if third_menu_choice == "1":
                TournamentControl.delete_tournament()
                pass
            elif third_menu_choice == "2":
                PlayerController.remove_player()
                pass
            elif third_menu_choice == "3":
                PlayerController.update_player_information()
                pass
            elif third_menu_choice == "b":
                continue
            else:
                MainView.invalid_option()

        elif choice == "q":
            MainView.goodbye()
            break

        else:
            MainView.invalid_option()


main()
