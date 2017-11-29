#Dictionary
dict = {'name':'Bob','ref':'Python','Sys':'Win'}
print('Dictionary :',dict)
print('\nReference :',dict['ref'])
print('\nKeys:',dict.keys())
del dict['name']
dict['user']='Tom'
print('\nDictionary:',dict)
print('\nIs There A name Key?:','name' in dict)
print('\nIs There A Reference Key?:','ref' in dict)
