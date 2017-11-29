#bitwise.py
a = 10
b = 5
print('a=', a, '\tb=', b)

# 1010 ^ 0101 = 1111(Decimal 15)
a = a ^ b

print(a)

# 1111 ^ 0101 = 1010(Decimal 10)
b = a ^ b
print(b)

# 1111 ^ 1010 = 0101(Decimal 5)
a = a ^ b
print(a)

print('a=', a, '\tb=', b)
