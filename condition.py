a = 1
b = 2
print('\nVariable a is :','One' if (a == 1) else 'Not One')
print('\nVariable a is :','Even' if (a % 2 == 0) else 'Odd')
print('\nVariable b is :','One' if (b == 1) else 'Not One')
print('\nVariable b is :','Even' if (b %2 ==0) else 'Odd')
max = a if (a > b) else b
print('\nGreter Value is :', max)
