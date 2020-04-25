'''
A module is also just a file with a .py filename extension. The name of the module
is the same as the filename (without the .py).
For using a module add it to your code: 
[import module_name ] or [from module_name import anything]
'''
'''A good resource for finding packages is PyPi, a clever name that’s easy
to remember and short for Python Package Index. 
the URL https://pypi.org/# 
'''

# Contains custom functions for dates and currency values.
import datetime as dt
def to_date(any_str):
    """ Convert mm/dd/yy or mm/dd/yyyy string to datetime.date, or None if
    invalid date. """
    try:
        if len(any_str) == 10:
            the_date = dt.datetime.strptime(any_str,'%m/%d/%Y').date()
        else:
          the_date = dt.datetime.strptime(any_str,'%m/%d/%y').date()
    except (ValueError, TypeError):
        the_date = None
    return the_date

def mdy(any_date):
    """ Returns a string date in mm/dd/yyyy format. Pass in Python date or
    string date in mm/dd/yyyy format """
    if type(any_date) == str:
        any_date = to_date(any_date)
    # Make sure its a dateime being forwarded
    if isinstance(any_date,dt.date):
        s_date = f"{any_date:'%m/%d/%Y'}"
    else:
        s_date = "Invalid date"
    return s_date

def to_curr(anynum, len=0):
    """ Returns a number as a string with $ and commas. Length is optional """
    s = "Invalid amount"
    try:
       x = float(anynum)
    except ValueError:
        x= None
    if isinstance(x,float):
        s = '$' + f"{x:,.2f}"
        if len > 0:
            s = s.rjust(len)
    return s