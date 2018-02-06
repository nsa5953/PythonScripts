#@@ Classs: Songbird.py
# Making feature of class file available
from Songbird import *

# create instance of class then display instance attributes and its identity address

bird_1 = Songbird('Koko', 'Tweet, Tweet!\n')
print(bird_1.name, 'ID', id(bird_1))
bird_1.sing()

# delete this instance calling its destructor method
del bird_1

# Now create two more instances of class then display their instance attribute values
# and their identity address

bird_2 = Songbird('Louie', 'Chirp, chirp...\n')
print(bird_2.name, 'ID', id(bird_2))
bird_2.sing()

bird_3 = Songbird('Misty', 'Squawk, squawk...\n')
print(bird_3.name, 'ID', id(bird_3))
bird_3.sing()

# Finally delete this instances - calling their destructors
del bird_2
del bird_3
