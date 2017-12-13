# Python Script to access files
# File Operation - open(), read(), write() and close()
# readlines() method to return a list of all readlines
###################################################################################
# create file object for new text file named "example.txt" to write content into it
file = open('example.txt','r+') # Here r+ is file mode
###################################################################################
# File modes and Operations
# r - Open an existing file to readable
# w - Open an existing file to write, create a new file if non exists
# a - Append Text. Open or create text file for writing at end of line
# r+ - Open a text file to read from or write to
# w+ - Open a text file to write to or read from
# a+ - Open or creates a text file to read from or write to end of file
###################################################################################

# Statement to display the file name and mode
print('File Name :', file.name)
print('File Open Mode :', file.mode)

# Statement to display file acess permissions
print('Readable :', file.readable())
print('Writable :', file.writable())

# Define function to determine the file's status

def get_status(f):
    if(f.closed != False):
        return 'Closed'
    else :
        return 'Open'

# Statement to display current status of file, then close the file and
# display the filestatus once more

print('File Status :', get_status(file))
file.close()
print('\nFile Status :', get_status(file))
