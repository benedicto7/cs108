"""CS 108 Lab/Homework 11.0

Gui Practice

@author: Keith VanderLinden (kvlinden)
@date: Spring, 2021
@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

from guizero import App, Text, TextBox, PushButton


class MyApp:

    def __init__(self, app):

        # Configure the application GUI.
        app.title = 'My Application'
        app.width = 300
        app.height = 150
        app.font = 'Helvetica'
        app.text_size = 12

        # Add the widgets. 
        hello_text = Text(app, text='Please enter your name:')      # writes the string into gui.
        TextBox(app)                                                # creates an box for the user to write
        PushButton(app, text='Goodbye!', command=app.destroy)       # creates a push button and destroys the app when clicked
           
# Create the GuiZero application.
app = App()
my_app = MyApp(app)
app.display()
