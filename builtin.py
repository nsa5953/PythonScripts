# Python script for examining built-in attributes
from Bird import *

zola = Bird('Beep, beep!')
print('\nBuilt-In Instance attributes....')
for attrib in dir(zola):
    if attrib[0] == '_':
        print(attrib)

print('\nClass Directory.... ')
for item in Bird.__dict__:
    print(item, ':', Bird.__dict__[item])

print('\nInstance Directory.... ')
for item in zola.__dict__:
    print(item,':',zola.__dict__[item])
