# Python script for creating instance class
# Declare new class with descriptive document string
class Bird:
    "'A Base class to define bird properties.'"

# Add indented statement to declare and initialize variable attribute with
# integer zero value
    count = 0

# Define the initializer class method to initialize an instance variable and
# to increment the class variable
    def __init__(self, chat):
        self.sound = chat
        Bird.count += 1

# Finally add a class method to rerun the value of instance variable when called
    def talk(self):
        return self.sound
