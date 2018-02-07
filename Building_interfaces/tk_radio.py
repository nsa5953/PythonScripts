# Python script - Building interfaces - Messagebox feature example
# Python Script - Polling Radio Button
from tkinter import *
import tkinter.messagebox as box

# Create Window object and specify title
window = Tk()
window.title('Radio Button Example')

# Now create a frame to contain Widgets
frame = Frame(window)

# Construct a string variable object to store Selection
book = StringVar()

# Create three radio button widget whose value will be assigned to string variable upon Selection
radio_1 = Radiobutton(frame, text = 'HTML5', variable = book, value = 'HTML5 in easy steps')
radio_2 = Radiobutton(frame, text = 'CSS3', variable = book, value = 'CSS3 in easy steps')
radio_3 = Radiobutton(frame, text = 'JavaScript', variable = book, value = 'JavaScript in easy steps')

# Statement to specify which radio button will be selected by default when program starts
radio_1.select()

# Function to display a radio button selected and a Button to call this Function
def dialog():
    box.showinfo('Selection', 'Your Choice: \n' + book.get() )

btn = Button(frame, text = 'Choose', command = dialog)

# Push Button and radio button to the frame
btn.pack(side = RIGHT, padx = 5)
radio_1.pack(side = LEFT)
radio_2.pack(side = LEFT)
radio_3.pack(side = LEFT)
frame.pack(padx = 30, pady = 30)

# Loop to capture windows events
window.mainloop()
