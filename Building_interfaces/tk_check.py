# Python script - Building interfaces - Messagebox feature example
# Python Script - Checking boxes
from tkinter import *
import tkinter.messagebox as box

# Create Window object and specify title
window = Tk()
window.title('Check Button Example')

# create frame to contain widget
frame = Frame(window)

# Construct three integer variable objects to store values
var_1= IntVar()
var_2= IntVar()
var_3= IntVar()

# Create three check button widget whose values will be assigned to the integer variable whether checked or Note
book_1 = Checkbutton(frame, text = 'HTML5', variable = var_1, onvalue = 1, offvalue = 0)
book_2 = Checkbutton(frame, text = 'CSS3', variable = var_2, onvalue = 1, offvalue = 0)
book_3 = Checkbutton(frame, text = 'JS', variable = var_3, onvalue = 1, offvalue = 0)

# create function to display a check button Selection
def dialog():
    str = 'Your Choice :'
    if var_1.get() == 1 : str += '\nHTML5 in easy'
    if var_2.get() == 1 : str += '\nCSS3 in easy'
    if var_3.get() == 1 : str += '\nJavaScript in easy'
    box.showinfo('Selection', str)

# Create a button to call the function when clicked
btn = Button(frame, text = 'Choose', command = dialog)

# Add the push button and check buttons to the Frame
btn.pack(side = RIGHT, padx = 5)
book_1.pack(side = LEFT)
book_2.pack(side = LEFT)
book_3.pack(side = LEFT)
frame.pack(padx = 30, pady = 30)

# Loop to capture windows events
window.mainloop()
