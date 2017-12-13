# Python Script to reading and writing files
# Initialize variable with concatenated string containing newline characters
poem = 'I never saw a man who looked\n'
poem += 'With such wishful eye\n'
poem += 'Upon that little tent of blue\n'
poem += 'Which prisoners call the sky\n'

# Statement to create file object for new textfile "poem.txt" to write content into
file = open('poem.txt', 'w')

# Statement to write string contained in the variable to text file and close that files
file.write(poem)
file.close()

# Statement to create a file obkect fpr existing text file "poem.txt" to read from
file = open('poem.txt', 'r')

# Display content of text file and close file
for line in file:
    print(line, end ='')
file.close()

#Statement to append a citation to text file
file = open('poem.txt', 'a')
file.write('(Oscar Wilde)')
file.close()
