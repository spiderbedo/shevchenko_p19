class StrandsDNA:
    """
    A class representing DNA strands storage.
    """

    def __init__(self):
        """
        Initialize an empty list of DNA strands.
        """
      
        self.all_strands = []

  
    def add_strands(self, strands: str) -> None:
        """
        Add DNA strands from a space-separated string.
        """
      
        self.all_strands.extend(strands.split())

  
    def get_max_strands(self) -> str:
        """
        Return unique longest strands in sorted order.
        """
      
        if not self.all_strands:
            return ""
        max_len = max(len(s) for s in self.all_strands)
        result = sorted({s for s in self.all_strands if len(s) == max_len})
        return " ".join(result)

  
    def __str__(self) -> str:
        """
        Return all strands as a string.
        """
      
        return " ".join(self.all_strands)

    __repr__ = __str__

