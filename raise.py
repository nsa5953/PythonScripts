#Python script for handing multiple exception
day = 32
try:
    if day > 31 :
        raise ValueError('Invalid Day Number')
except ValueError as msg :
    print ('The Program found an', msg)

finally :
    print('But Today is Beautiful ANYWAYS....')
    
