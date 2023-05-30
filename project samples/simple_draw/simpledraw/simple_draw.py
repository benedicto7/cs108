"""
This module implements SimpleDraw, a canvas-based paint application.

@author: Keith VanderLinden (kvlinden)
@date: Summer, 2015
@date: Spring, 2021 - ported to GuiZero
"""

from guizero import App, Drawing, PushButton, Box, ButtonGroup
from figure import Line, Squiggle, Rectangle, Ellipse


class SimpleDraw:
    """This class provides the GUI for the SimpleDraw figure editor."""

    def __init__(self, app):
        """Creates the GUI and the list of figures"""

        app.title = 'SimpleDraw'
        UNIT = 300
        CONTROL_UNIT = 80
        app.width = UNIT
        app.height = UNIT + CONTROL_UNIT
        
        # The main drawing canvas
        self.drawing = Drawing(app, width=400, height=300)
        self.drawing.when_left_button_pressed = self.process_mouse_press
        self.drawing.when_mouse_dragged = self.process_mouse_motion
        self.drawing.when_left_button_released = self.process_mouse_release
        self.figure_choice = ButtonGroup(
            app, ['line', 'rectangle', 'ellipse', 'squiggle'], selected='line',
            horizontal=True
        )
        self.color_choice = ButtonGroup(
            app, ['black', 'red', 'green', 'blue'], selected='black',
            horizontal = True
        )
        self.fill_choice = ButtonGroup(
            app, ['unfilled', 'filled'], selected='unfilled',
            horizontal=True
        )

        # Create the list of model objects, which starts empty,
        # and refresh the drawing canvas (to whitewash it).
        self.figures = []
        self.draw_figures()

        # Temporary coordinates used by the drawing methods
        self.saved_x = None
        self.saved_y = None

    def process_mouse_press(self, event):
        """Starts a new figure where the user presses the mouse based on the
        mode settings
        """
        self.saved_x = event.x
        self.saved_y = event.y
        self.temporary_figure = \
            self.create_figure(event, self.fill_choice.value=='filled',
                               self.color_choice.value)
        self.temporary_figure.render(self.drawing)

    def process_mouse_motion(self, event):
        """Displays a temporary version of the figure and erase the previous
        temporary version
        """
        if self.figure_choice.value == 'squiggle':
            # Squiggles are special in that they don't have temporary versions.
            self.temporary_figure.add_point((event.x, event.y))
            self.temporary_figure.render(self.drawing)
        else:
            # Erase the previous version by redrawing it in white.
            self.temporary_figure.set_color('White')
            self.temporary_figure.render(self.drawing)
            self.temporary_figure = \
                self.create_figure(event, self.fill_choice.value=='filled',
                                   self.color_choice.value)
            self.temporary_figure.render(self.drawing)

    def process_mouse_release(self, event):
        """Create and save the final version of the figure"""
        if self.figure_choice.value == 'squiggle':
            self.temporary_figure.add_point((event.x, event.y))
            self.figures.append(self.temporary_figure)
        else:
            self.figures.append(
                self.create_figure(event,
                                   self.fill_choice.value=='filled',
                                   self.color_choice.value))
        self.draw_figures()
        
    def create_figure(self, event, filled, color):
        """Creates a figure based on the given mode settings -
        The figure can be either temporary or permanent. The calls to the
        constructors for closed figures must convert upper-left and lower-right
        points into upper-left point and dimensions for the constructors.
       """
        if self.figure_choice.value == 'line':
            return Line((self.saved_x, self.saved_y), (event.x, event.y),
                        color=color)
        elif self.figure_choice.value == 'rectangle':
            return Rectangle((self.saved_x, self.saved_y),
                             (event.x - self.saved_x, event.y - self.saved_y),
                             filled=filled, color=color)
        elif self.figure_choice.value == 'ellipse':
            return Ellipse((self.saved_x, self.saved_y),
                           (event.x - self.saved_x, event.y - self.saved_y),
                           filled=filled, color=color)
        elif self.figure_choice.value == 'squiggle':
            return Squiggle((self.saved_x, self.saved_y), color=color)
    
    def draw_figures(self):
        """Redraw all the stored figures on a fresh background"""
        self.drawing.rectangle(0, 0,
                               self.drawing.width, self.drawing.height,
                               color='white')
        for figure in self.figures:
            figure.render(self.drawing)

        
app = App()
SimpleDraw(app)
app.display()
