#Python script to modify strings
# Initialize variable with string of lowercase characters and spaces
string = 'python in easy steps'

# Display the string - Capitalized, titled and Centerd
print('\nCapitalized:\t', string.capitalize())
print('\nTitled:\t\t', string.title())
print('\nCentered:\t', string.center(30,'*'))

# Display sting in all uppercase and merged with squence of two astrisks
print('\nUppercase:\t', string.upper())
print('\nJoined:\t\t', string.join('##'))

# Display string padded with astrisks on left
print('\nJustified:\t', string.ljust(30,"*"))

# Display string padded with astrisks on right
print('\nJustified:\t', string.rjust(30,"*"))

# Display string with all occurance of the 'S' character replaced by astrisks
print('\nReplaced:\t',string.replace('python', 'Shell'))
