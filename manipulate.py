#Python script to manupulate strings
def display(s):
    '''Display an argument value'''
    print(s)

# Statement to display function discription
display(display.__doc__)

# Statement to display raw string that contains backslash character
display(r'c:\Program Files')

# String concatination
display('\nHello' + 'Python')

# Slice String range
display('Python in Easy Steps\n'[5 :])

# Seeing Characters
display('P' in 'Python')
display('p' in 'Python')
