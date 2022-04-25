from guizero import App, Text, PushButton, TextBox, Box

class HelloApp:

    def __init__(self, app):
        app.title = 'Hello Application'
        app.font = 'Helvetica'
        app.text_size = 12

        box = Box(app, layout='grid', border=2)
        Text(box, text='Type something here: ', grid=[0,0])
        self.input_box = TextBox(box, grid=[1,0])
        PushButton(app, text='Press Me!', command=self.button_pressed)
        self.message_text = Text(app, text="Hello, GuiZero!")

    def button_pressed(self):
        self.message_text.value = 'You typed: ' + self.input_box.value

app = App()
HelloApp(app)
app.display()
