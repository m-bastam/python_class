import datetime as dt
# from datetime import *

names = ["Zara", "Lupe", "Hong", "Alberto", "Jake", "Tyler"]

numbers = [14, 0, 56, -4, 99, 56, -2, 14, 11, 23]

# create a list of dates, empty for starters 

datelists = []
datelists.append(dt.date(2020,12,31))
datelists.append(dt.date(2019,1,31))
datelists.append(dt.date(2018,2,28))
datelists.append(dt.date(2020,1,1))


print(names)
# sort strings in reverse order (Z to A) and show
names.sort()
print(names)
print()

print(f"list of numbers :{numbers}")
#reverse numbers not sorted reverse
numbers.reverse()
print(f"reversed numbers :{numbers}")
#sort numbers in order (smallest to Largerst) and show
numbers.sort(reverse=True)
print(print(f"sort numbers(s-l) :{numbers}"))
print()
print(datelists)
datelists.sort(reverse=True)
print(datelists)
print()
for date in datelists:
    print (f"{date:%m/%d/%Y}")

print("\t-----------------------------------------------\n\n")
# Create a list of strings.
names = ["Zara", "Lupe", "Hong", "Alberto", "Jake"]
print(names)
# Make a copy of the list
backward_names = names.copy()

names2 = names

backward_names.pop()
backward_names.append("Ali")
del backward_names[1]

# Reverse the names2
names2.reverse()
# Print the list

print(backward_names)
print(names)
print()
print(f"id names  = {id(names)}")
print(f"id names2 = {id(names2)}")
print(f"id backward_names = {id(backward_names)}")



'''
Methods for Working with Lists
Method    What it Does
append()  Adds an item to the end of the list.
clear()   Removes all items from the list, leaving it empty.
copy()    Makes a copy of a list.
count()   Counts how many times an element appears in a list.
extend()  Appends the items from one list to the end of another list.
index()   Returns the index number (position) of an element within a list.
insert()  Inserts an item into the list at a specific position.
pop()     Removes an element from the list, and provides a copy of that item that you can store in a variable.
remove()  Removes one item from the list.
reverse() Reverses the order of items in the list.
sort()    Sorts the list in ascending order. Put reverse=True inside the parentheses to sort in descending order.
del list  Remove an item of list of remove the object 
'''