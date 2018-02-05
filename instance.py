## Refer bird.py file where class defined
# Display document string

from Bird import *
print('\nClass Instance of:\n', Bird.__doc__)

# Add statement to create an instance of the class and pass string argument
# vakye ti its instance variable
polly = Bird('Squawk,Squawk!')

# Display this instance variable value and call class method
print('\nNumber of Birds', polly.count)
print('Polly Says:', polly.talk())

# Create second instance nClass
harry= Bird('Tweet, tweet!')

print('\nNumber of Birds', harry.count)
print('Harry Says:', harry.talk())
