class User:
    """
    A class representing a website user.
    """

    def __init__(self, id, nick_name, first_name, last_name="", middle_name="", gender=""):
        """
        Initialize a user with required and optional attributes.
        """
      
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

  
    def update(self, id=0, nick_name="", first_name="", last_name="", middle_name="", gender="") -> None:
        """
        Update user attributes if non-default values are provided.
        """
      
        if id != 0:
            self.id = id
        if nick_name != "":
            self.nick_name = nick_name
        if first_name != "":
            self.first_name = first_name
        if last_name != "":
            self.last_name = last_name
        if middle_name != "":
            self.middle_name = middle_name
        if gender != "":
            self.gender = gender

  
    def __str__(self) -> str:
        """
        Return the string representation of the user.
        """
      
        return (
            f"User(id={self.id}, nick_name={self.nick_name!r}, "
            f"first_name={self.first_name!r}, "
            f"last_name={self.last_name!r}, "
            f"middle_name={self.middle_name!r}, "
            f"gender={self.gender!r})"
        )

  
    __repr__ = __str__
