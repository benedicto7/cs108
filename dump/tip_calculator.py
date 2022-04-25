"""
This module implements a tip calculator.

@author: kvlinden
@date: Summer, 2015
@date: Spring, 2021 - ported to GuiZero
"""

from guizero import App, Box, Text, TextBox, PushButton, Picture


class TipsApp:

    def __init__(self, app):

        # Configure the application GUI.
        app.title = 'Tip Calculator'
        app.width = 300
        app.height = 130
        app.font = 'Helvetica'
        app.text_size = 13

        # Create a Box in which to format the UI.
        box = Box(app, layout='grid')
        
        # Add the widgets.
        Text(box, text='Amount:', grid=[1, 0], align='right')
        self.amount_entry = TextBox(box, width=6,
                                    grid=[2, 0], align='left')
        Text(box, text='Percentage:', grid=[1, 1], align='right')
        self.percentage_entry = TextBox(box, width=6,
                                        grid=[2, 1], align='left')
        Text(box, text='Tip:', grid=[1, 2], align='right')
        self.tip_text = Text(box, width=6, text='...',
                             grid=[2, 2], align='left')
        PushButton(box, self.compute_tip, text='Compute', grid=[1, 3])
        PushButton(box, app.destroy, text='Quit', grid=[3, 3])
        Picture(box, image='images/tip.gif', grid=[0, 0, 1, 4], align='top')

    def compute_tip(self, event=None):
        self.tip_text.value = \
            float(self.amount_entry.value) * float(self.percentage_entry.value)


app = App()
TipsApp(app)
app.display()
