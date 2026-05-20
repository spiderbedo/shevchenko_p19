import math

class Point:
    """
    A class representing a point on a plane.
    """

    def __init__(self, coords=None):
        """
        Initialize point coordinates or set to (0, 0) by default.
        """
      
        if coords is None:
            coords = (0, 0)
        self.x, self.y = coords

  
    def get_x(self) -> float:
        """
        Return the x-coordinate.
        """
      
        return self.x

  
    def get_y(self) -> float:
        """
        Return the y-coordinate.
        """
      
        return self.y

  
    def distance(self, other) -> float:
        """
        Return the distance to another point.
        """
      
        return math.hypot(self.x - other.x, self.y - other.y)

  
    def sum(self, other):
        """
        Return a new point as the sum of two points.
        """
      
        return Point((self.x + other.x, self.y + other.y))

  
    def __str__(self) -> str:
        """
        Return the string representation of the point.
        """
      
        return f"({self.x}, {self.y})"

  
    __repr__ = __str__
