num = 20
try:
    num1 = int (input ('please enter a number: '))
    result = num / num1
    print(result)
except ValueError: 
    print (" Please enter a digit")
except ZeroDivisionError:
    print('the second number can not be zero') 
except Exception:
    print ('there is an error')
else:
    print('there is not any error')
finally:
    print('This block will run in anyway')
    
print ("\t--------------------------\t\n")