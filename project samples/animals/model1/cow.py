class Cow:
    """Cows are simple animals.

    Cows have 4 legs (are "quadrupeds") and walk,
    eat grass (are "herbivores"), and say "moo".
    """

    def __init__(self):
        """Construct a new instance of the Cow class."""
        self.position = (0, 0)
        self.respired = 0
        self.stomach = []

    def eat(self, item):
        """Cow eats grass."""
        if item == "grass":
            self.stomach.append(item)
            return "ate " + item
        else:
            return "This herbivore doesn't eat " + item

    def move(self, delta):
        """Cow walks on 4 legs."""
        self.position = (self.position[0] + delta[0],
                         self.position[1] + delta[1])
        return "This quadruped walked to " + str(self.position)

    def respire(self):
        """Cow respired."""
        self.respired += 1
        return "This cow respired through its nostrils."

    def speak(self):
        """Cow says "moo"."""
        return "moo"
