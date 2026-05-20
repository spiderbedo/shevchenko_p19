class TrafficLight:
    """
    A class representing a traffic light.
    """

    permissible_values = ["green", "yellow", "red", "yellow"]

    def __init__(self):
        """
        Initialize the traffic light with green signal.
        """
      
        self._index = 0
        self.current_signal = self.permissible_values[self._index]

  
    def next_signal(self) -> None:
        """
        Switch to the next signal.
        """
      
        self._index = (
            (self._index + 1) % len(self.permissible_values)
        )
        self.current_signal = self.permissible_values[self._index]

  
    def __str__(self) -> str:
        """
        Return the string representation of the signal.
        """
      
        return self.current_signal

  
    __repr__ = __str__
