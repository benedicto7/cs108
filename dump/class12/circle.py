
class Circle:

    def __init__(self, x, y, radius, color='black'):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, drawing):
        drawing.oval(
            self.x - self.radius, self.y - self.radius,
            self.x + self.radius, self.y + self.radius,
            outline=True,
            outline_color='black',
            color=self.color
        )