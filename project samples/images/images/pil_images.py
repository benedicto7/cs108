"""
Draw an image on the drawing canvas or a button.

The image is stored in memory and reused, which avoids reloading
it constantly from disk in an animation.

@author: kvlinden
@date: Summer, 2016
@date: Spring, 2021 - ported to GuiZero
@author: kcarnold
@date: Spring 2021 - store the image in memory
"""

from guizero import App, Drawing, Picture, PushButton
from PIL import Image

class MyApp:

    def __init__(self, app):

        app.title = 'Image Demo'
        app.width = 128
        app.height = 3 * app.width
        app.font = 'Helvetica'
        app.text_size = 12

        # Load the image into memory.
        self.tux_image = Image.open('tux-128.gif')
        # Nb. The image object must be stored somewhere (e.g., on self)
        # or it will not actually show up.

        # If needed, you can manipulate the image, e.g.: rotate and resize.
        # print("Image size:", self.tux_image.width, "X", self.tux_image.height)
        # self.tux_image = self.tux_image.rotate(-15).resize((80, 80))
        # For details, see:
        # https://pillow.readthedocs.io/en/stable/reference/Image.html

        # Draw the image on a drawing canvas.
        self.drawing = Drawing(app, width=app.width, height=app.width)
        self.drawing.image(0, 0, self.tux_image)

        # You can also show the image on buttons and widgets.
        PushButton(app, image=self.tux_image)
        Picture(app, image=self.tux_image)


# Create the GuiZero application.
app = App()
my_app = MyApp(app)
app.display()
