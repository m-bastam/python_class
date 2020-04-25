''' Template
try:
    try to do this
except x:
    if x happens, stop here
except Exception as e:
    if something else bad happens, stop here
else:
    if no exceptions, continue on normally here
finally:
    do this code no matter what happened above

You can stack up except:, if some exception occurred that you didn’t handle, 
then you get the standard Python error message.
except Exception:  catches any exception that hasn’t already be caught by 
any preceding except: in the code. The finally: block, if included, is the 
code that runs whether an exception occurs or not.
'''

# define Python user-defined exceptions
# class Error(Exception):
#     """Base class for other exceptions"""
#     pass

# Your custom error (inherits from Error)
class EmptyFileError(Exception):
    pass



# try:
#     # Open the file name people.csv
#     thefile = open('cars.csv')
# # Watch for common error and stop program if it happens.
# except FileNotFoundError:
#     print("Sorry, I don't see a file named people.csv here")
# # Catch any unexpected error and stop program if one happens.
# except Exception as err:
#     print(err)
# # Otherwise, if nothing bad has happened by now, just keep going.
# else:
#     # File must be open by now if we got here.
#     print('\n') # Print a blank line.
#     # Print each line from the file.
#     for one_line in thefile:
#         print(one_line)
#     thefile.close()
#     print("Success!")
 
    
print("\t---------------------------------\n\n")    
print('Do this first')
try:
    thefile = open('cars.csv')
    # Count the number of lines in file.
    line_count = len(thefile.readlines())
    # If there is fewer than 2 lines, raise exception.
    if line_count < 2:
        raise EmptyFileError 
        # raise Exception
except FileNotFoundError:
    print('Cannot find file named cars.csv')
except EmptyFileError:
    print('File named cars.csv is empty')
except Exception as e:
    print('there is a error in a whole')
else:
    print('Show this if no exception.')
finally:
    print('This is in the finally block')
    
print("This is outside the try...except...else...finally")

# For a detailed list of all the different exceptions that Python can catch, take a
# look at https://docs.python.org/3/library/exceptions.html