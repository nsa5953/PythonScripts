# Python Script for Overriding base methods
# Declare base class with initializer method to set an instance
# variable and second method to display that variable value

class Person :
    "'A Base class to define person properties'"
    def __init__(self, name):
        self.name = name

    def speak(self, msg='(Calling the Base Class)'):
        print(self.name, msg)
