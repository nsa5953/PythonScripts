#@@ Reference Inheritance feature - Polygon.py
# declare a derived class with method to rerun manipulated class variable set_values

from Polygon import *
class Triangle(Polygon):
    def area(self):
        return(self.width * self.height)/2
