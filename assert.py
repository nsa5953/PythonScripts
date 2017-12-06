#Python Script for Debugging with assert statement
chars = ['Alpha', 'Beta','Gamma','Delta','Epsilon']
print (type(chars))
def display(elem):
    assert type(elem) is int, 'Argument must be Integer !'
    print('List Elements', elem, '=', chars[elem])
elem  = 4
display(elem)
elem = elem / 2
display(elem)
