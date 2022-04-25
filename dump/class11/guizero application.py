from guizero import App, Text, PushButton, TextBox, Box

class HelloApp:
    
    def __init__(self, app):
        app.title = 'Hello Application'
        app.font = 'Helvetica'
        app.text_size = 12
        
        TextBox(app)                          # creates a textbok
        PushButton(app, text='Press Me!')     # creates a button
        Text(app, text='Hello, GuiZero!')     # writes a string into gui
        Box(app)
    
app = App()
HelloApp(app)
app.display()