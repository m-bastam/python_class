''' method read() in file
read([size]) : Reads in the entire file if you leave the parentheses empty.
    If you specify a size inside the parentheses, it reads that many characters
    (for a text file) or that many bytes (for a binary file).to	read.If	the	
    argument is -1, the	files must be read to the end.Also if no argument is given,
    the	default	is takent as -1. If the content	of the file is larger than the
    memory then only the content which can fit into the memory will be read.
    Moreover, when the read operation ends a ""(an empty string) is returned.	

readline() : Reads one line of content from a text file (the line ends wherever
    there’s a newline character).

readlines() : Reads all the lines of a text file into a list. 

readline() and readlines() are useful only for text files.
'''

# with open('students.txt') as f:
#     # Reads in all lines first, then loops through.
#     # Count each line starting at zero.
#     for one_line in enumerate(f.readlines()):
#         # If counter is even number, print with no extra newline
#         if one_line[0] % 2 == 0:
#             print(one_line[1], end='')
#         # Otherwise print a couple spaces and an extra newline.
#         else:
#             print(one_line[1])
# print('\n\t----------------------------------\n')            
# with open('students.txt') as f:
#     # Read first line to get started.
#     print(f.tell())
#     one_line = f.readline()
#     # Keep reading one line at a time until there are no more.
#     while one_line:
#         print(one_line[:-1],' ', f.tell())
#         one_line = f.readline()

        
'''
 seek() method allows you to reposition the pointer. 
    The syntax is: file.seek(position[,whence])
    0: Set position relative to the start of the file.
    1: Set position relative to the current pointer position.
    2: Set position relative to the end of the file. Use a negative number for position
    If you omit the whence value, it defaults to zero.
tell() function	returns the position of the cursor.
'''

# Specify the file to copy.
file_to_copy = 'class-template.png'
# Create new file name with _copy before the extension.
name_parts = file_to_copy.split('.')
new_file = name_parts[0] + '_copy.' + name_parts[1]
# Open the original file as read-only binary.
with open(file_to_copy,'rb') as original_file:
    # Create or open file to copy into.
    with open(new_file,'wb') as copy_to:
        # Grab a chunk of original file (4KB).
        chunk = original_file.read(4096)
        #Loop through until no more chunks.
        while len(chunk) > 0:
            copy_to.write(chunk)
            # Make sure you read in the next chunk in this loop.
            chunk = original_file.read(4096)

            
# Close is automatic after loops, show done message
print('Done!')
            