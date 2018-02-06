# Python script for collecting garbage
# Declare class with an initilizer method creating two instance variable and method
# to display one of those variable values
class Songbird:
        def __init__(self, name, song):
            self.name = name
            self.song = song
            print(self.name, 'Is Born.....')

# Add a method to simply display both variable values
        def sing(self):
            print(self.name, 'Sings:', self.song)

# Add destructor method for confirmation when instanaces of class are destroyed
        def __del__(self):
            print(self.name, 'Flew Away !\n')
