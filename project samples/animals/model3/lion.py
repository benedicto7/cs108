from animal import Animal


class Lion(Animal):
    """Lions are simple animals.

    Lions have 4 legs (are "quadrupeds") and walk,
    eat meat (are "carnivores"), and say "ROOOAR".
    """

    def __init__(self):
        """Construct a new instance of the Lion class."""
        super().__init__("Lion", "meat", "walked", "ROOOAR")
