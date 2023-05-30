from animal import Animal


class Horse(Animal):
    """Horses are simple animals.

    Horses have 4 legs (are "quadrupeds") and walk,
    eat grass (are "herbivores"), and say "nay" (are "naysayers").
    """

    def __init__(self):
        """Construct a new instance of the Horse class."""
        super().__init__("Horse", "grass", "galloped", "nay")

    def nuzzle(self, position):
        """Move to position (to be in range of nuzzling)."""
        self.position = position
        return self.position

    def respire(self):
        """Horse respired."""
        self.respired += 1
        return "This horse respired through its muzzle."
