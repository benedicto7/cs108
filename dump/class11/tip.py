'''
The final version of the tip calculator presented in the GUI video demos...

Created Summer, 2015

@author: kvlinden
'''

from tkinter import *

class App:
    ''' a simple tip calculator GUI '''

    def __init__(self, window):
        
        # Add a frame that surrounds and pads the widgets.
        main_frame = Frame(window)
        main_frame.grid(padx=10, pady=10)        
    
        # Present the bill amount label and field.
        self.amount_variable = DoubleVar()
        self.amount_variable.set(0.0)
        amount_label =  Label(main_frame, text='Amount:')
        amount_label.grid(row=0, column=1, sticky=E, padx=10)
        amount_entry = Entry(main_frame, textvariable=self.amount_variable)
        amount_entry.grid(row=0, column=2, sticky=W)
        amount_entry.bind('<Return>', self.compute_tip)

        # Present the precentage label and field.
        self.percentage_variable = DoubleVar()
        self.percentage_variable.set(0.15)
#         percentage_label = Label(window, text='Percentage:')
#         percentage_label.grid(row=1, column=1, sticky=E, padx=10)
#         percentage_entry = Entry(window, textvariable=self.percentage_variable)
#         percentage_entry.grid(row=1, column=2)
        
        TIP_SUGGESTIONS = [('10%', 0.10), ('15%', 0.15), ('20%', 0.20)]
        tip_frame = Frame(main_frame)
        tip_frame.grid(row=1, column=2, sticky=W)
        for t,p in TIP_SUGGESTIONS:
            b = Radiobutton(tip_frame, text=t, value=p, variable=self.percentage_variable)
            b.pack(side=LEFT)
                
        # Present the tip label and computed value.
        self.tip_variable = DoubleVar()
        self.tip_variable.set(0.0)
        tip_label = Label(main_frame, text='Tip:')
        tip_label.grid(row=2, column=1, sticky=E, padx=10)
        tip_value_label= Label(main_frame, textvariable=self.tip_variable)
        tip_value_label.grid(row=2, column=2, sticky=W)
        
        # Present the calculate button and link it to the tip calculation method.
        entry_button = Button(main_frame, text='Compute', command=self.compute_tip)
        entry_button.grid(row=3, column=2, sticky=W)

        # Present the quit button and link it to the predefined quit function.
        quit_button = Button(main_frame, text='Quit', command=window.destroy)
        quit_button.grid(row=3, column=2, sticky=E)
        
        # Add a graphical logo to the interface.
        logo = PhotoImage(file='images/tip.gif')
        image_label = Label(main_frame, image=logo)
        image_label.image = logo
        image_label.grid(row=0, column=0, rowspan=4)

    def compute_tip(self, event=None):
        ''' 
        Compute the tip based on the amount and percentage, 
        and present it in the output label. 
        '''
#         self.tip_variable.set('testing...')
        self.tip_variable.set(self.amount_variable.value * self.percentage_variable.value)
         

if __name__ == '__main__':
    # Construct the main GUI window and start the UI event loop.
    root = Tk()
    root.title('Tip Calculator')
    App(root)
    root.mainloop()
    