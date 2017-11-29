# Precedense.py
a = 2
b = 4
c = 8
print('\na=',a)
print('b=',b)
print('c=',c)

print('\nMultiplication & Addition')
print('Default Order:\t',a,'*',c,"+",b,'=',a * c + b)
print('Forced Order:\t',a,'*(',c,'+',b,')=',a*(c + b))

print('\nDivision & Substraction')
print('Default Order:\t',c,'//',b,'-',a,'=', c // b - a)
print('Forced Order:\t',c,'//(',b,'-',a,')=', c // (b - a))

print('\nAddition and Modulus')
print('Default Order:\t',c,'%',a,'+',b,')=',c % a + b)
print('Forced Order:\t',c,'%(',a,'+',b,')=',c % (a + b))

print('\nExponent & Addition')
print('Default Order:\t',c,'**',a,'+',b,')=',c ** a + b)
print('Forced Order:\t',c,'**(',a,'+',b,')=',c ** (a + b))
