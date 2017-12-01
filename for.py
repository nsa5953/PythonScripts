#Python script for "For loop"
chars =['A', 'B', 'C']
fruit = ('Apple', 'Banana', 'Cherry')
dict = {'name':'Mike','ref':'Python','sys':'Win'}

print('\nElements:\t',end='')
for items in chars :
    print(items, end ='')

print('\nEnumerated:\t',end='')
for items in enumerate(chars):
    print(items, end='')

print('\nZipped:\t',end='')
for items in zip(chars, fruit):
    print(items, end='')

print('\nPaired:')
for key, value in dict.items():
    print(key, '=', value)
