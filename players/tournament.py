class Tournament:
    def __init__(self, name, place, starting_date, round_list, player_list, description, number_of_rounds=4):
        self.name = name
        self.place = place
        self.starting_date = starting_date
        self.number_of_rounds = number_of_rounds
        self.round_list = round_list
        self.player_list = player_list
        self.description = description
        pass