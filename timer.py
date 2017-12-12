#Python script for running timer
#
from time import *

# Initialize a variable with floating point number i.e current elapsed time since epoch
start_timer = time()

# statement to create struct_time object from elapsed time value
struct = localtime(start_timer)

# Announce that countdown timer will begin  from current time
print('\nStarting Countdown at :', strftime('%X', struct))
# %X - Time appropriate for locale

# Add loop to Initialize and print counter variable value then decrement the
# counter by one and pause for one second on each iteration
i = 15
while i > -1 :
    print(i)
    i -= 1
    sleep(1)

end_timer = time()
difference = round (end_timer - start_timer)
print('\nRuntime :', difference, 'Seconds')
