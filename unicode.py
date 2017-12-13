# Python script for converting strings
#---------------------------------------------------------
#Functions used
# encode()
# decode()
#---------------------------------------------------------
# Initialize variable with string containing non-ASCII character then display
# its values, datatype and string length

s= 'RÖd'
print('\nRed String :', s)
print('Type :', type(s), '\tLength :', len(s))

# encode the string again display its value, datatype and string tLength
s = s.encode('utf-8')
print('\nEncoded String :', s)
print('Type :', type(s), '\tLength :', len(s))

# decode the string again display its value, datatype and string tLength
s = s.decode('utf-8')
print('\nDecoded String :', s)
print('Type :', type(s), '\tLength :', len(s))

# Add statement to make "unicodedata" feature available and loop to
# reveal the unicode name of each character in the strings

import unicodedata
for i in range(len(s)):
    print(s[i], unicodedata.name(s[i]), sep=":" )

# Add statement to assign variable another new value includes hexadecimal code point
# for non-ASCII character then display decoded strings

s= b'Gr\xc3\xb6n'
print('\nGreen String:', s.decode('utf-8'))

# Finally assing the vairable with new value that includes unicode character
# for non-ASCII character then display  strings values
s ='Gr\N{LATIN SMALL LETTER O WITH DIAERESIS}\n'
print('\nGreen String:', s)
