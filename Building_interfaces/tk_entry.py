# Python script - Building interfaces - Messagebox feature example
# Python Script - Gathering inputs
from tkinter import *
import tkinter.messagebox as box

# Create window object and specify title
window = Tk()
window.title('Entry Example')

# Create frame to containe an entry field for input
frame = Frame(window)
entry = Entry(frame)

# Function to disply data currently entered
def dialog():
    box.showinfo('Greetings', 'Welcome' + entry.get())

# Create button to call the function when clicked
btn = Button(frame, text='Enter Name', command=dialog)

# Button and try to frame at set sides
btn.pack(side = RIGHT, padx = 5)
entry.pack(side = LEFT)
frame.pack(padx = 20, pady = 20)

# Loop to capture window's events
window.mainloop()
