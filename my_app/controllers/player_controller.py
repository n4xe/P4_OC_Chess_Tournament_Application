class PlayerController:
    @classmethod
    def update_player_information(cls):
        """
        This method allows to the user to update information of a player already stored in the json database file.
        :return:
        """
        with open('players/players_database.json', 'r') as file:
            existing_data = json.load(file)

        first_name = input("Enter the first name of the player information you want to update: ")
        last_name = input("Enter the last name of the player information you want to update: ")
        found_player = False

        for player in existing_data:
            if player["First name"] == first_name and player["Last name"] == last_name:
                found_player = True
                print("Player found. Current information: ")
                print(player)

                while True:
                    update_choice = input("What information do you want to update? "
                                          "('F' for first name, 'L' for last name, "
                                          "'B' for birthday date, 'C' for chess ID, "
                                          "'Q' to quit updating): ").upper()
                    if update_choice == "Q":
                        break
                    elif update_choice == "F":
                        new_first_name = input("Enter new first name: ")
                        player["First name"] = new_first_name
                    elif update_choice == "L":
                        new_last_name = input("Enter new last name: ")
                        player["Last name"] = new_last_name
                    elif update_choice == "B":
                        new_birthday_date = input("Enter new birthday date (DD/MM/YYYY): ")
                        player["Birthday date"] = new_birthday_date
                    elif update_choice == "C":
                        new_chess_id = input("Enter new chess ID: ")
                        player["Chess ID"] = new_chess_id
                    else:
                        print("Invalid choice.")

                print("Updated information: ")
                print(player)
                break

        if not found_player:
            print("No player found with the given name.")

        with open('players/players_database.json', 'w') as file:
            json.dump(existing_data, file, indent=4)
            file.write('\n')  # Add a new line after the entries

    @classmethod
    def remove_player(cls):
        with open('players/players_database.json', 'r') as file:
            players_data = json.load(file)

        # Affichage des joueurs avec numéros
        for i, player in enumerate(players_data, start=1):
            first_name = player['First name']
            last_name = player['Last name']
            print(f"Player {i}: {first_name} {last_name}")

        # Demande à l'utilisateur de sélectionner un joueur à supprimer
        selected_player = input("Please enter the list number of the player to delete : ")

        # Vérification de la validité du numéro de joueur
        if not selected_player.isdigit() or int(selected_player) < 1 or int(selected_player) > len(players_data):
            print("Invalid number, please try again.")
        else:
            index = int(selected_player) - 1
            deleted_player = players_data.pop(index)
            first_name = deleted_player['First name']
            last_name = deleted_player['Last name']
            print(f"Player '{first_name} {last_name}' successfully deleted.")

            # Mise à jour du fichier JSON
            with open('players/players_database.json', 'w') as file:
                json.dump(players_data, file, indent=4)


