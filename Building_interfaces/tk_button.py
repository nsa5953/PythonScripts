# Python script - Building interfaces - Button example

from tkinter import *
window = Tk()
window.title('Button Example')

# Create a button to exit the program when clicked
btn_end = Button(window, text='close', command=exit)

# Function to toggle window's background color when another button gets clicked
def tog():
    if window.cget('bg') == 'red':
        window.configure(bg = 'gray')
    else :
        window.configure(bg = 'red')
# Create button to call the function when clicked
btn_tog = Button(window, text='Switch', command=tog)

# Button to window with positional padding
btn_end.pack(padx = 150, pady = 20)
btn_tog.pack(padx = 150, pady = 20)

# Loop to capture window's events
window.mainloop()

#@ Notes:   1. Only Function name is specified to command option. Do not add trailing parentheses in the assignment
#           2. The 'gray' is the origional default color of the window
