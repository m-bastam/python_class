''' 
There are basically two types of files:
Text files: Text files contain plain text characters. When you open these in a
    text editor, they show human-readable content.
Binary files: A binary file stores information in bytes that aren’t quite so
    humanly readable. 

Syntax:
open(filename.ext[,mode])
mode is optional and can be:
r: (Read): Allows Python to open the file but not make any changes. This is the
    default if you don’t specify a mode. 
r+: (Read/Write): Allows Python to read and write to the file.
a: (Append): Opens the file and allows Python to add new content to the end of the
    file but not to change existing content. If the file doesn’t exist, this mode
    creates the file.
w: (Write): Opens the file and allows Python to make changes to the file.
    Creates the file if it doesn’t exist.
x: (Create): Creates the file if it doesn’t already exist. If the file does exist, it
    raises a FileExistsError exception
If you already specified one of the above modes, just add this as another letter.
If you use just one of the letters below on its own, the file opens in Read mode.

t: (Text): Open as a text file, read and write text.
b: (Binary): Open as a binary file, read and write bytes.
'''
# - Basic syntax to open, read, and display file contents.
f = open('cars.csv')
filecontents = f.read()
print(filecontents)
# Some attributes of file.
print('File is closed: ', f.closed)
print('File Mode: ', f.mode)
print('File name: ', f.name)
# Closes the file.
f.close() #Close the file.

print(f.closed)
print() # Print a blank line.

# ---------------- Contextual syntax
# The contextual syntax because it’s generally the preferred and recommended syntax
with open('cars.csv') as f:
    filecontents = f.read()
    print(filecontents)

# The unindented line below is outside the with... block;
print('File is closed: ', f.closed)

'''
Binary files have no human-readable content in them. Nor do they have lines of text.
So readline() and readlines() aren’t a good choice for looping through binary files. 
But you can use .read() with a specified size to achieve a similar result with binary files.
'''
with open('class-template.png', 'rb') as f:
    filecontents = f.read()
    print(filecontents)

# with open('test_file.txt', 'r', encoding= 'utf-8') as f:    
# # with open('test_file.txt', 'r') as f:
#     filecontents = f.read()
#     print(filecontents)