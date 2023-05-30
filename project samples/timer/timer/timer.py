"""
This module implements a simple timer/stopwatch.

Save the Timer class in a timer.py module, import that module, and use the
timer object as shown in the sample TimerApp. You can use this approach to
display a timer value and/or to handle periodic events.

@author: kvlinden
@date: Summer, 2016
@date: Spring, 2021 - ported to GuiZero
@author: ka37
@date: Spring 2021 - separated out the model
"""

from guizero import App, Text, PushButton
from datetime import datetime

class Timer:
    def __init__(self):
        self.reset()

    def reset(self):
        self.start_time = datetime.now()

    def get_time(self):
        time_since_start = datetime.now() - self.start_time
        return time_since_start.total_seconds()


class TimerApp:

    def __init__(self, app):
        app.height = 100
        
        # Set up the timer.
        self.timer = Timer()
        self.text = Text(app)

        # Add reset button.
        PushButton(app, command=self.reset, text='Reset')

        # Start the counter.
        self.update_clock()
        app.repeat(10, self.update_clock)

    def update_clock(self):
        # Here, we update the value of the timer display on the GUI.
        self.text.value = '{:.02f}'.format(self.timer.get_time())

        # As an alternative, we could do some periodic task in your
        # application, e.g.: adding a new object to the GUI animation;
        # updating the score value.

    def reset(self):
        self.timer.reset()


app = App()
TimerApp(app)
app.display()
