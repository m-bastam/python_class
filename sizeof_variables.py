import sys
"""for checking variable size """
x = 5
print (sys.getsizeof(0))
print (sys.getsizeof(x), id(x))

x = 6
print (sys.getsizeof(x), id (x))

x = 2333.12341
print (sys.getsizeof(x) , id(x))

print (sys.getsizeof(''))
x="hello the world!"
print (sys.getsizeof(x), id (x))