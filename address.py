#Python Script for Addressing class attributes
from Bird import *

# Create an instance of class then add a new attribute with
# assigned vlaue using dot notation

chick = Bird('Cheep, cheep!')
chick.age='1 Week'

# Display the values in both instance variable and attribute
print('\nChick Says', chick.talk())
print('Chick age:', chick.age)

# modify the new attribute using dot notations
chick.age='2 weeks'
print('Chick Now:', chick.age)

# Modify new attribute once more
setattr(chick,'age','3 Weeks')

# Display a list of all non-private instance and their respective
# values using built-in functions

print('\nChick Attributes....')
for attrib in dir(chick):
    if attrib[0] != '_':
        print(attrib, ':', getattr(chick, attrib))

delattr(chick, 'age')
print('\nChick age Attributes?', hasattr(chick, 'age'))
