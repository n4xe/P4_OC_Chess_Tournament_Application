class TournamentControl:

    @classmethod
    def delete_tournament(cls):
        with open('tournament_information/tournament_database.json', 'r') as file:
            tournaments_data = json.load(file)

        # Affichage des tournois avec numéros
        for i, tournament in enumerate(tournaments_data, start=1):
            name = tournament['Name']
            print(f"Tournoi {i}: {name}")

        # Demande à l'utilisateur de sélectionner un tournoi
        selected_tournament = input("Veuillez entrer le numéro du tournoi à supprimer : ")

        # Vérification de la validité du numéro de tournoi
        if not selected_tournament.isdigit() or int(selected_tournament) < 1 or int(selected_tournament) > len(
                tournaments_data):
            print("Numéro de tournoi invalide.")
        else:
            index = int(selected_tournament) - 1
            deleted_tournament = tournaments_data.pop(index)
            name = deleted_tournament['Name']
            print(f"Tournoi '{name}' supprimé avec succès.")

            # Mise à jour du fichier JSON
            with open('tournament_information/tournament_database.json', 'w') as file:
                json.dump(tournaments_data, file, indent=4)