class Lion:
    """Lions are simple animals.

    Lions have 4 legs (are "quadrupeds") and walk,
    eat meat (are "carnivores"), and say "ROOOAR".
    """

    def __init__(self):
        """Construct a new instance of the Lion class."""
        self.position = (0, 0)
        self.respired = 0
        self.stomach = []

    def eat(self, item):
        """Lion eats meat."""
        if item == "meat":
            self.stomach.append(item)
            return "ate " + item
        else:
            return "This carnivore doesn't eat " + item

    def move(self, delta):
        """Lion walks on 4 legs."""
        self.position = (self.position[0] + delta[0],
                         self.position[1] + delta[1])
        return "This quadruped walked to " + str(self.position)

    def respire(self):
        """Lion respired."""
        self.respired += 1
        return "This lion respired through its nostrils."

    def speak(self):
        """Lion says "ROOOAR"."""
        return "ROOOAR"
