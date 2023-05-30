class Pig:
    """Pigs are simple animals.

    Pigs have 4 legs (are "quadrupeds") and walk,
    eat anything (are "omnivorous"), and say "oink".
    """

    def __init__(self):
        """Construct a new instance of the Pig class."""
        self.position = (0, 0)
        self.respired = 0
        self.stomach = []

    def eat(self, item):
        """Pig eats everything."""
        self.stomach.append(item)
        return "ate " + item

    def move(self, delta):
        """Pig walks on 4 legs."""
        self.position = (self.position[0] + delta[0],
                         self.position[1] + delta[1])
        return "This quadruped ran to " + str(self.position)

    def respire(self):
        """Pig respired."""
        self.respired += 1
        return "This pig respired through its snout."

    def speak(self):
        """Pig says "oink"."""
        return "oink"

    def wallow(self):
        """Roll about in water, probably consuming a little."""
        self.stomach.append("water")
        return self.speak()
