# Python script - Building interfaces - Messagebox feature example
# Python Script - Adding image
from tkinter import *
window = Tk()
window.title('Image Example')

# Create Window object and specify title
img = PhotoImage(file = 'C:\python.gif')

# Create a lable object to display the image above colored background
label = Label(window, image = img, bg = 'yellow')

# create half-size image object from first image object
small_img = PhotoImage.subsample(img, x = 2, y = 2)

# create a button to display small PhotoImage
btn = Button(window, image = small_img)

# create a text field and embed the small image then insert some text after it
txt = Text(window, width = 25, height = 7)
txt.image_create('1.0', image = small_img)
txt.insert('1.1', 'Python Fun!')

# create canvas and paint the small image above a colored background then paint a diagonal line over the top of it
can = \
Canvas(window, width = 100, height = 100, bg = 'cyan')
can.create_image((50, 50), image = small_img)
can.create_line(0, 0, 100, 100, width = 25, fill = 'red')

# add widget to the windows
label.pack(side = TOP)
btn.pack(side = LEFT, padx = 10)
txt.pack(side = LEFT)
can.pack(side = LEFT, padx = 10)

# loop to capture windows events
window.mainloop()
