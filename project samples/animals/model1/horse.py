class Horse:
    """Horses are simple animals.

    Horses have 4 legs (are "quadrupeds") and walk,
    eat grass (are "herbivores"), and say "nay" (are "naysayers").
    """

    def __init__(self):
        """Construct a new instance of the Horse class."""
        self.position = (0, 0)
        self.respired = 0
        self.stomach = []

    def eat(self, item):
        """Horse eats grass."""
        if item == "grass":
            self.stomach.append(item)
            return "ate " + item
        else:
            return "This herbivore doesn't eat " + item

    def move(self, delta):
        """Horse walks on 4 legs."""
        self.position = (self.position[0] + delta[0],
                         self.position[1] + delta[1])
        return "This quadruped galloped to " + str(self.position)

    def nuzzle(self, position):
        """Move to position (to be in range of nuzzling)."""
        self.position = position
        return self.position

    def respire(self):
        """Horse respired."""
        self.respired += 1
        return "This horse respired through its muzzle."

    def speak(self):
        """Horse says "nay"."""
        return "nay"
