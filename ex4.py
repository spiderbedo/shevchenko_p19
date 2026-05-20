class Game:
    """
    A class representing a basketball game.
    """

    def __init__(self, teams: dict):
        """
        Initialize the game with two teams.
        """
      
        self.command1 = teams["command1"]
        self.command2 = teams["command2"]
        self.score1 = 0
        self.score2 = 0

  
    def ball_thrown(self, command: int, points: int) -> None:
        """
        Add points to the specified team.
        """
      
        if command == 1:
            self.score1 += points
        elif command == 2:
            self.score2 += points

  
    def get_score(self) -> tuple:
        """
        Return the current score as a tuple.
        """
      
        return self.score1, self.score2

  
    def get_winner(self) -> str:
        """
        Return the winner team name or 'Ничья'.
        """
      
        if self.score1 > self.score2:
            return self.command1
        if self.score2 > self.score1:
            return self.command2
        return "Ничья"

  
    def __str__(self) -> str:
        """
        Return the string representation of the game.
        """
      
        return (
            f"{self.command1}: {self.score1}, "
            f"{self.command2}: {self.score2}"
        )

  
    __repr__ = __str__

