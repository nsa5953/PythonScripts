# Python script for Maths operations
import math, random
# statements for rounded values
print ('Rounded up 9.5 :', math.ceil(9.5))
print('Rounded Down 9.5 :', math.floor(9.5))

num = 16 # Initialize variable
# Statement for sqare and square root of numbers
print(num, 'Squared :', math.pow(num, 2))
print(num,'Square root :', math.sqrt(num))
print(type(num))
# Statement to produce random list of six unique number between 1 and 49
nums= random.sample(range(1, 49), 5)
print('Your Lucky Numbers are', nums)
print(type(nums))
