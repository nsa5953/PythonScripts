# Python Script: Developing Application
# 1. Genrate six unique random numbers in range 1-49
# 2. A Function to clear last six random numbers from display
# USE GUI
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
imgLbl.grid()
label1.grid()
label2.grid()
label3.grid()
label4.grid()
label5.grid()
label6.grid()
getBtn.grid()
resBtn.grid()

# Loop statement to capture window events
# Sustain window
window.mainloop()
