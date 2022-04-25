from guizero import App, Text, PushButton, TextBox

class HelloApp:

    def __init__(self, app):
        app.title = 'Hello Application'
        app.font = 'Helvetica'
        app.text_size = 12
        
        self.text_box = TextBox(app)
        self.message_text = Text(app, text="Hello, GuiZero!")
        PushButton(app, text='Press Me!', command=self.button_pressed)

    def button_pressed(self):
        self.message_text.value = 'You typed: ' + self.text_box.value


app = App()
HelloApp(app)
app.display()

