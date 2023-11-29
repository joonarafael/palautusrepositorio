class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        """Function to add a point."""

        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        elif player_name == self.player2_name:
            self.player2_score = self.player2_score + 1

    def check_tie_status(self):
        """Helper function to check if the game is currently tied."""

        if self.player1_score == self.player2_score:
            if self.player1_score == 0:
                return "Love-All"
            elif self.player1_score == 1:
                return "Fifteen-All"
            elif self.player1_score == 2:
                return "Thirty-All"
            else:
                return "Deuce"

        return None

    def check_end_game_status(self):
        """Helper function to check for the end game status and possible win."""

        if self.player1_score >= 4 or self.player2_score >= 4:
            difference = self.player1_score - self. player2_score

            if difference == 1:
                return f"Advantage {self.player1_name}"
            elif difference == -1:
                return f"Advantage {self.player2_name}"
            elif difference >= 2:
                return f"Win for {self.player1_name}"
            else:
                return f"Win for {self.player2_name}"

        return None

    def get_score(self):
        """Function to check the current game status."""

        score = self.check_tie_status()

        if score is not None:
            return score

        score = self.check_end_game_status()

        if score is not None:
            return score

        # game is not tied and any possible unique end game status was not present

        score = [str(self.player1_score), "-", str(self.player2_score)]

        score = list(map(lambda x: x.replace('0', 'Love'), score))
        score = list(map(lambda x: x.replace('1', 'Fifteen'), score))
        score = list(map(lambda x: x.replace('2', 'Thirty'), score))
        score = list(map(lambda x: x.replace('3', 'Forty'), score))

        return ''.join(score)
