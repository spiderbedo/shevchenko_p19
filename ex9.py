class CoordinateSystem:
    """
    A class representing a coordinate system with segments.
    """

    def __init__(self):
        """
        Initialize an empty list of segments.
        """
        self.segments = []

  
    def add_segment(self, segment) -> None:
        """
        Add a segment to the coordinate system.
        """
      
        self.segments.append(segment)

  
    def axis_intersection(self) -> int:
        """
        Return number of segments crossing exactly one axis.
        """
      
        return sum(
            1 for seg in self.segments if seg.one_intersection
        )

  
    def __str__(self) -> str:
        """
        Return string representation of segments.
        """
      
        return str(self.segments)

  
    __repr__ = __str__
