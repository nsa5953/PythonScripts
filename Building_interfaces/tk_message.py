# Python script - Building interfaces - Messagebox feature example
from tkinter import *
import tkinter.messagebox as box

# Create a Window object and specify title
window = Tk()
window.title('Message Box Example')

# Function to display various message boxes
def dialog():
    var = box.askyesno('Message Box', 'Proceed?')
    if var == 1 :
        box.showinfo('Yes Box', 'Proceeding....')
    else :
        box.showwarning('No Box','Cancelling...')

# Create a button to call the function when clicked
btn = Button(window, text='Click', command=dialog)


# Button to window with positional padding
btn.pack(padx = 150, pady = 50)

# Add loop to capture window events
window.mainloop()
type = 'abortretryignore'
