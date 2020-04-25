# Import all the code from module_date.py as my.
import module_date as my
# from module_date import to_date, mdy, to_curr
# Need dates in this code
from datetime import datetime as dt

# Some simple test data.
string_date = "12/31/2019"
# Convert string date to datetime.date
print(my.to_date(string_date))
today = dt.today()
# Show today's date in mm/dd/yyyy format.
print(my.mdy(today))
dollar_amt = 12345.678
# Show this big number in currency format.
print(my.to_curr(dollar_amt))

# 
'''The __name__ variable is a special Python variable. It gets its value
depending on how we execute the containing script.'''

print(" the caller of this module is :" ,__name__)

if __name__ == '__main__':
   print("************************")
   print('This module has directly run!')