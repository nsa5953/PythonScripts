# Python Script for Fomatting Strings
# Initialize variable with formatted string

# ---------------------------------------------------------------
## @ Note 1-  format() is used to format Strings
## {} and {} curly braces are used to define str object
# ---------------------------------------------------------------
snack = '{} and {}'.format('Burger', 'Fries')

# Display variable value to see text replaced in there listed order
print('\nReplaced :', snack)

# Assign differently-formatted string to variable
snack = '{1} and {0}'.format('Burger', 'Fries')

# Display the variable value again to see the text now replaced by their specified
# index element value
print('\nReplaced :', snack)

# Assign another formatted string to variable
snack = '%s and %s' %('Milk','Cookies')
print('\nSubstituted :', snack)
