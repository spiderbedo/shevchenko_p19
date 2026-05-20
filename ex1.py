class Dog:
    """
    A class representing a dog.
    """

    def __init__(self, name: str):
        """
        Initialize a dog with a given name.
        """

        self.name = name


    def say(self) -> None:
        """
        Print the barking sound of the dog.
        """

        print("Гав!")


    def __str__(self) -> str:
        """
        Return the string representation of the dog.
        """

        return self.name


    __repr__ = __str__
