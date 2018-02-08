# Python Script: Developing Application
# 1. Genrate six unique random numbers in range 1-49
# 2. A Function to clear last six random numbers from display
# USE GUI - Final Lotto program
from tkinter import *

# Create window object and image object
window = Tk()
img = PhotoImage(file = 'C:\logo.gif')

# Static Properties
window.title('Lotto Number Picker')

# Statement to prevent the user resizing the window along with both the X axis and Y axis - This will disable Windows's resize Button
window.resizable(0,0)

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

# Statement to specify text to appear on face of first Button widget
getBtn.configure(text='Get my Lucky Numbers')

# Statement to specify text to appear on face of second Button widget
resBtn.configure(text='Reset')

# Initial properties
# specifies each small entry Label should initially disply all ellipsis

label1.configure(text ='...')
label2.configure(text ='...')
label3.configure(text ='...')
label4.configure(text ='...')
label5.configure(text ='...')
label6.configure(text ='...')

# Statement to specify that second button widget should initially be disabled
resBtn.configure(state= DISABLED)

#Dynamic Properties
from random import sample

# Define function that generates and assign six unique random numbers to the small Labels and reverse state of both Buttons
def pick():
    nums = sample(range(1, 49), 6)
    label1.configure(text = nums[0])
    label2.configure(text = nums[1])
    label3.configure(text = nums[2])
    label4.configure(text = nums[3])
    label5.configure(text = nums[4])
    label6.configure(text = nums[5])
    getBtn.configure(state = DISABLED)
    resBtn.configure(state = NORMAL)

# Define function to display an ellipsis on each small Label and revert both buttons to their initial states
def reset():
    label1.configure(text ='...')
    label2.configure(text ='...')
    label3.configure(text ='...')
    label4.configure(text ='...')
    label5.configure(text ='...')
    label6.configure(text ='...')
    getBtn.configure(state = NORMAL)
    resBtn.configure(state = DISABLED)

# Statement to nominate the relevant function to be called when each button is pressed by user
getBtn.configure(command = pick)
resBtn.configure(command = reset)

# Loop statement to capture window events
# Sustain window
window.mainloop()
