# Python script for patter matching with re module

from re import *

# Initailize Variable with a regular expression object
pattern = compile ('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+.)+.[a-z]{2,6}(\s|$)')

# Begin function by requesting user input and attempt to match pattern
def get_address():
    address = input('Enter your Email Address :')
    is_valid = pattern.match(address)

# Add indented statement to display appropriate to describe
# whether the attempt is succeeded
    if is_valid :
        print('Valid Address', is_valid.group())
    else :
        print('Invalid Address !!, Please retry... \n')

# Call the defined function
get_address()
