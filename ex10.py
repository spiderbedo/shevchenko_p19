class Segment:
    """
    A class representing a segment between two points.
    """

    def __init__(self, point1: Point, point2: Point):
        """ 
        Initialize segment with two points.
        """
      
        self.point1 = point1
        self.point2 = point2
        self.one_intersection = self._has_one_axis()

  
    def _crosses_axis(self, a: float, b: float) -> bool:
        """
        Check if segment crosses axis by coordinates.
        """
      
        return a == 0 or b == 0 or a * b < 0

  
    def _has_one_axis(self) -> bool:
        """
        Check if segment crosses exactly one axis.
        """
      
        x_axis = self._crosses_axis(
            self.point1.y, self.point2.y
        )
        y_axis = self._crosses_axis(
            self.point1.x, self.point2.x
        )
        return x_axis ^ y_axis

  
    def __str__(self) -> str:
        """
        Return string representation of segment.
        """
      
        return f"Segment({self.point1}, {self.point2})"

  
    __repr__ = __str__

