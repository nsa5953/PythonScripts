# Python Script: Developing Application
# 1. Genrate six unique random numbers in range 1-49
# 2. A Function to clear last six random numbers from display
# USE GUI - Change layout position
from tkinter import *

# Create window object and image object
window = Tk()
img = PhotoImage(file = 'C:\logo.gif')

# Add statement to create all necessary widgets
imgLbl = Label(window, image= img)
label1 = Label(window, relief = 'groove', width = 2)
label2 = Label(window, relief = 'groove', width = 2)
label3 = Label(window, relief = 'groove', width = 2)
label4 = Label(window, relief = 'groove', width = 2)
label5 = Label(window, relief = 'groove', width = 2)
label6 = Label(window, relief = 'groove', width = 2)
getBtn = Button(window)
resBtn = Button(window)

# Widgets to the window using grid layout manager - Ready to receive arguments to specify
# how widgets should be positioned at design stage next
# Geometry
imgLbl.grid(row =1, column = 1, rowspan = 2)
label1.grid(row =1, column = 2, padx = 10)
label2.grid(row =1, column = 3, padx = 10)
label3.grid(row =1, column = 4, padx = 10)
label4.grid(row =1, column = 5, padx = 10)
label5.grid(row =1, column = 6, padx = 10)
label6.grid(row =1, column = 7, padx = (10,20))
getBtn.grid(row =2, column = 2, columnspan = 4)
resBtn.grid(row =2, column = 6, padx = 2)


# Loop statement to capture window events
# Sustain window
window.mainloop()
