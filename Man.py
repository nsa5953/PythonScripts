# Python script for Overriding base methods
# Reference class: @Person.py
#  Declare a derived class with a method that overrides the
# second base class method
from Person import *
"'A derived class to define Man properties.'"

class Man(Person):
    def speak(self, msg):
        print(self.name, '\n\tHello!!!', msg)
