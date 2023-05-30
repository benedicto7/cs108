from animal import Animal


class Cow(Animal):
    """Cows are simple animals.

    Cows have 4 legs (are "quadrupeds") and walk,
    eat grass (are "herbivores"), and say "moo".
    """

    def __init__(self):
        """Construct a new instance of the Cow class."""
        super().__init__("Cow", "grass", "walked", "moo")
