# Python Script: Developing Application
# Developing application: Genrating Random numbers

from random import random, sample

# Assign a random floating-point number to variable then display its value
num = random()
print('Random Fload 0.0 - 1.0 :', num)

# Multiply the floating-point number and cast it to become an integer then display its value
num = int(num * 10)
print('Random Integer 0 - 9 :', num)

# loop to Assign multiple random integers to list then display list items
nums = []; i = 0
while i < 6 :
    nums.append(int(random() * 10) + 1)
    i += 1
print('Random Multiple integers 1 - 10:', nums)

# Assign multiple unique random integers to the list then display the list items
nums = sample(range(1, 49), 6)
print('Random Integer Sample 1 -49:', nums)
