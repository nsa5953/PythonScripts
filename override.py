# Python script for Overriding base methods
# Reference class: @Person.py
# Python script by making features of both (man and Hombre)
# derived classes available
from Man import *
from Hombre import *

# Create instance of each derived class, initializing "name" instance
# variable attribute

guy_1 = Man('Timepass')
guy_2 = Hombre('Timepass2')

# Call the overriding method of each derived class , assigning differernnt values to "msg" argument

guy_1.speak('It\'s a beautiful evening.\n')
guy_2.speak('Es una tarde hermosa.\n')

# Explicitly call the base class method , passing a reference to each derived class -
# but none for the "msg" variable so default values will be used

Person.speak(guy_1)
Person.speak(guy_2)
