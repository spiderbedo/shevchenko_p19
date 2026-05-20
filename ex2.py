class NotSleeping:
    """
    A class representing a person counting sheep to fall asleep.
    """

    def __init__(self, name: str, count_sheeps: int = 0):
        """
        Initialize a person and initial sheep count.
        """
      
        self.name = name
        self.count_sheeps = count_sheeps

    
    def add_sheep(self) -> None:
        """
        Increase the number of counted sheep by one.
        """
      
        self.count_sheeps += 1

    
    def lost(self) -> None:
        """
        Reset the sheep count to zero.
        """
      
        self.count_sheeps = 0

    
    def get_count_sheeps(self) -> int:
        """
        Return the current number of counted sheep.
        """
      
        return self.count_sheeps


