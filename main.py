from my_app.views.player_view import PlayerView
from my_app.views.tournament_view import TournamentView
from my_app.models.player import Player
from my_app.models.tournament import Tournament
from my_app.models.match import Match
from my_app.models.round import Round
from my_app.controllers.player_controller import PlayerController
from my_app.controllers.tournament_controller import TournamentControl


def main():
    print("Welcome to the application!")

    while True:
        print("\nMain Menu:")
        print("1. Create a tournament\n")
        print("2. View information")
        print("3. Settings and modifications")
        print("q. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\nCreate Tournament Menu:")
            print("1. Add a player")
            print("2. Start tournament")
            print("b. Back to main menu")

            create_tournament_choice = input("Choose an option: ")

            if create_tournament_choice == "1":
                player = Player.get_player_information()
                player.set_player_information()
                pass
            elif create_tournament_choice == "2":
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

                    # Ask user if he wants to go next round
                    user_input = input(
                        "Press ""Y"" to continue : ")
                    if user_input.lower() != "y":
                        break
                pass
            elif create_tournament_choice == "b":
                continue
            else:
                print("Invalid option. Please try again.")

        elif choice == "2":
            print("\nView Information Menu:")
            print("1. View results")
            print("2. View players by alphabetical order")
            print("3. View all tournaments")
            print("4. Search tournament")
            print("b. Back to main menu")

            view_information_choice = input("Choose an option: ")

            if view_information_choice == "1":
                pass
            elif view_information_choice == "2":
                PlayerView.display_players()
                pass
            elif view_information_choice == "3":
                TournamentView.display_tournaments()
                pass
            elif view_information_choice == "4":
                # Search tournament logic
                pass

            elif view_information_choice == "b":
                continue
            else:
                print("Invalid option. Please try again.")

        elif choice == "3":
            print("\nSettings and Modification Menu:")
            print("1. Delete tournament")
            print("2. Delete player")
            print("3. Modify a player")
            print("b. Back to main menu")

            settings_choice = input("Choose an option: ")

            if settings_choice == "1":
                TournamentControl.delete_tournament()
                pass
            elif settings_choice == "2":
                PlayerController.remove_player()
                pass
            elif settings_choice == "3":
                PlayerController.update_player_information()
                pass
            elif settings_choice == "b":
                continue
            else:
                print("Invalid option. Please try again.")

        elif choice == "q":
            print("Thank you for using the application. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


main()
