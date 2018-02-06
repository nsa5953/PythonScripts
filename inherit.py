from Rectangle import *
from Triangle import *

# Create instance of each derived class
rect = Rectangle()
trey = Triangle()

# call the class method inherited from the base class, passing arguments to assign to the class variables
rect.set_values(4,5)
trey.set_values(4,5)
print('Rectangle Area:', rect.area())
print('Triangle Area:', trey.area())
