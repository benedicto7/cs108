from guizero import App, Drawing
from spot import Spot

class MyApp:

    def __init__(self, app):

        app.title = 'Hello Animation'
        app.when_clicked = self.process_mouse_event
        
        self.drawing = Drawing(app, width=app.width, height=app.height)
        self.spot = Spot(200, 25, vel_x=0, vel_y=1)

        app.repeat(30, self.draw_frame)

    def draw_frame(self):
        self.drawing.clear()
        print('drawing ' + str(self.spot))
        self.spot.draw(self.drawing)
        self.spot.move()
    
    def process_mouse_event(self, event):
        print(event.x, event.y)
        self.spot.x = event.x
        self.spot.y = event.y


app = App()
my_app = MyApp(app)
app.display()