def function_1(x):return x ** 2
def function_2(x): return x ** 3
def function_3(x): return x ** 4
def function_4(x): return x ** 5
callbacks = [function_1, function_2, function_3, function_4]
print('\nNamed Function :')
for function in callbacks :
    print('Result :', function(2))
callbacks = \
[lambda x : x ** 2, lambda x : x ** 3, lambda x : x ** 4, lambda x : x ** 5]
print('\nAnonymous Functions :')
for function in callbacks:
    print('Results :', function(2))
