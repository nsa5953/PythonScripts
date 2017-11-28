a = input('Enter A number :')
b = input('Now enter another Number :')
sum = a + b
print('\nData Type Sum :', sum, type(sum))

sum = int(a) + int(b)
print('Data Type Sum :', sum, type(sum))

sum = float(sum)
print('Data Type Sum :', sum, type(sum))

sum = chr(int(sum))
print('Data Type Sum :', sum, type(sum))
