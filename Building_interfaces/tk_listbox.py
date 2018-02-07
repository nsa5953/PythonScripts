# Python script - Building interfaces - Messagebox feature example
# Python Script - listbox
from tkinter import *
import tkinter.messagebox as box

# Create a Window object and specify title
window = Tk()
window.title('Listbox Example')

# Now create a frame to contain Widgets
frame = Frame(window)

# Create listbox widget offering three list items
listbox= Listbox(frame)

listbox.insert(1, 'HTML5 in easy steps')
listbox.insert(2, 'CSS3 in easy steps')
listbox.insert(3, 'JavaScript in easy steps')

# Add a function to display a listbox selection
def dialog():
    box.showinfo('Selection', 'Your Choice:' +\
    listbox.get(listbox.curselection() ) )

# Create a button to call the function when clicked
btn = Button(frame, text = 'Choose', command = dialog)

# Add the button and listbox to frame at set sides
btn.pack(side = RIGHT, padx = 5)
listbox.pack(side = LEFT)
frame.pack(padx = 30, pady = 30)

# Loop to capture windows events
window.mainloop()
