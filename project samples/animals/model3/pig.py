from animal import Animal


class Pig(Animal):
    """Pigs are simple animals.

    Pigs have 4 legs (are "quadrupeds") and walk,
    eat anything (are "omnivorous"), and say "oink".
    """

    def __init__(self):
        """Construct a new instance of the Pig class."""
        super().__init__("Pig", "", "ran", "oink")

    def respire(self):
        """Pig respired."""
        self.respired += 1
        return "This pig respired through its snout."

    def wallow(self):
        """Roll about in water, probably consuming a little."""
        self.stomach.append("water")
        return self.speak()
