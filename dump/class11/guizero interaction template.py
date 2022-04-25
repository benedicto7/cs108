from guizero import App, Text, PushButton, TextBox, Box, ButtonGroup, Drawing

class HelloApp:
    
    def __init__(self, app):
        app.title = 'Hello Application'
        app.wdith = 600 
        app.height = 300
        app.font = 'Helvetica'
        app.text_size = 12
        
        #box = Box(app, layout='grid', border=True)
        TextBox(app)                              # creates a textbok
        self.button = PushButton(app, text='Press Me!', command=self.hide_show)         # creates a button
        self.word = Text(app, text='Hello, GuiZero!')         # writes a string into gui
        
    def hide_show(self):
        if self.word.hide() != self.word.hide():
            self.word.hide()
        else:
            self.word.show()
      
app = App()
HelloApp(app)
app.display()