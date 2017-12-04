#Python Script for defining functions
def echo(user, lang, sys):
    print('User:', user, 'Language:', lang,'Platform:', sys)
echo('Mike', 'Python', 'Windows')
echo(lang='Python', sys='Mac Os', user='Anne')
echo (sys='Linux', user='Nilesh', lang='Python3.4')
def test(user='Carole', lang='Python'):
    print('\nUser:', user, 'Language :', lang)
test()
test(lang='Java')
test(user = 'Tony')
test('Susan', 'C++')
test('Nilesh','Shell Scripting')
test(user='Nil')
