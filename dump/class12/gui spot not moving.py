from guizero import App, Drawing
from spot import Spot

app = App()
drawing = Drawing(app, width=app.width, height=app.height)

spot = Spot(25, 200)
spot.draw(drawing)

app.display()