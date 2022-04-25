class Spot:

    def __init__(self, x, y, vel_x=0, vel_y=0):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def __str__(self):
        return 'Spot (' + str(self.x) + ', ' + str(self.y) + ')'

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def draw(self, drawing):
        drawing.oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5)