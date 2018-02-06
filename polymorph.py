# Python Script: Polymorphism
# Python script by making feature of both classes(Duck and Mouse) available
from Duck import *
from Mouse import *

# Defind function that accepts any single object as its arugment
# and attempts to call methods of that object
def describe(object):
    object.talk()
    object.coat()

# create instance object of each class
donald = Duck()
mickey = Mouse()

# Add statement to call the function and pass each instance object to its as an argument
describe(donald)
describe(mickey)

#Note: A class can have only one method with given name - method overloading is not supported
# in Python
