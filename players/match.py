import random

import datetime
class Match:
    def __init__(self, player_pairs):
        self._player_pairs = player_pairs
        self._start_time = None
        self._end_time = None
    pass

    def perform_match(self, ):
        """Perform matches according to pairs set"""
        match_results = []

        for pair in self._player_pairs:
            player1 = pair[0]
            player2 = pair[1]
            # Match simulation
            winner = random.choice([player1, player2])
            if winner == player1:
                score1 = 1
                score2 = 0
            elif winner == player2:
                score1 = 0
                score2 = 1
            else:
                score1 = 0.5
                score2 = 0.5

    def set_start_time(self):
        self._start_time = datetime.now()

    def set_end_time(self):
        self._end_time = datetime.now()
