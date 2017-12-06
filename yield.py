#Python Script for producing Genrator
def fib_gen():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b
fi = fib_gen()
for i in fi :
    if i > 100:
        break
    else :
        print('Generated :', i)
print(type(fi))
