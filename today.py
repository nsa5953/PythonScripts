#Python script of date time
#-------------------------------------------------------------------------------------
# Note 1 :  import datetime module to make its feature available
#-------------------------------------------------------------------------------------
from datetime import *

today = datetime.today()
print ('Today is: ', today)

# Add loop to display each attribute value individually
for attr in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond'] :
    print(attr, ':\t', getattr(today, attr))

# Add statement to display time using dot notation
print('Time :', today.hour, ':', today.minute, sep="")

# Assign formatted day and month names to vairables
day = today.strftime('%A') # %A is used to display full Weekday name
month = today.strftime('%B') # %B is used to display full month name

#-------------------------------------------------------------------------------------
# Note 2 - Default datetime objects are stored as numeric values
# but to can be display transformed into text equivalent using its "strftime()" method
#-------------------------------------------------------------------------------------

# Add Statement to display formatted datetime
print('Date :', today.day, month, day)
