# Python script to building interfaces
# Python script with statement to make the "tkinter" module GUI method
# and attributes available
from tkinter import *

# Statement to call upon a constructor to create window object
window = Tk()

# Statement to specify a title for this window
window.title('Label Example')

# Statement to call upon constructor to create label object
label = Label(window, text = 'Hello World !')

# Use the packer to add the label to window with horizontal and verical padding for positioning
label.pack(padx = 200, pady = 20)

# Mandatory statement to maintain the window by capturing events
window.mainloop()

# @Note:: Widgets will not appear in the window when running the program unless they have been added
# with geometry manager
