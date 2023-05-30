class Animal:
    """This class is a combination of many kinds of animal.

    Animals can eat, move, respire, and speak.
    Some can nuzzle and wallow.
    """

    def __init__(self, name, eats_only, moved, nasal, sound):
        """Constructs a new instance of the Animal class."""
        self.eats_only = eats_only
        self.moved = moved
        self.name = name
        self.nasal = nasal
        self.position = (0, 0)
        self.respired = 0
        self.sound = sound
        self.stomach = []

    def eat(self, item):
        """Animal eats everything or only eats_only."""
        if len(self.eats_only) == 0 or self.eats_only == item:
            self.stomach.append(item)
            return "This " + self.name + " ate " + item
        else:
            return "This " + self.name + " doesn't eat " + item

    def move(self, delta):
        """Animal moves to position."""
        self.position = (self.position[0] + delta[0],
                         self.position[1] + delta[1])
        return "This " + self.name + " " + self.moved + " to "\
               + str(self.position)

    def nuzzle(self, position):
        """Move to position (to be in range of nuzzling)."""
        self.position = position
        return self.position

    def respire(self):
        """Animal respired."""
        self.respired += 1
        return "This " + self.name + " respired through its " + self.nasal + "."

    def speak(self):
        """Animal is taciturn."""
        return self.sound

    def wallow(self):
        """Roll about in water, probably consuming a little."""
        self.stomach.append("water")
        return self.speak()
