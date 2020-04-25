'''
dictionaries are kind of lists. But instead of each item in the list
being identified by its position in the list, each item is uniquely identified
by a key. The key in a dictionary represents one unique thing, and you can associate 
a value with that key. 
name = {key:value, key:value, key:value, key:value, ...}
Dictionaries are mutable, which means you can change the contents of the dictionary.
'''


# Make a data dictionary named people.
people = {
'Ali': 17,
'Mary': 18,
'Sara': 20,
'Ardavan': 18,
'Arghavan': 19
}
# Count the number of key:value pairs and put in a variable.
howmany = len(people)
print(howmany)
print(people)
# Change the value of the hrjackson key.
people.update({'Sara':16})
print(people)
# Update the dictionary with a new property:value pair.
people.update({'Nazanin':17})
print(people)


person = 'Farhad'
print(person in people)
'''
You can actually pass two values to get() , the second one being what you want it
to return if the get fails to find what you’re looking for
'''
# value = people[person]
value = people.get(person, -1)
print(value) 
people[person] = 15
print(people)

print(people.keys(), type(people.keys()))
res_keys = list(people.keys())
res_keys.sort()
print(res_keys, type(res_keys))
print()

res_items = list(people.items())
print(res_items)
print(res_items[4][0])
    
for key, value in people.items():
    print(f"Score of {key} is {value}")
 
    
#remove item from dic
del people['Sara']
print(people)

person = people.pop("Mary")
print(person)
print(people)

person = people.popitem()
print(person)
print(people)

# people.clear()
# print(people)


# Create a dictionary names  that has the same keys as people.
template_people = dict.fromkeys(people.keys())     
print(template_people)
    
    
'''
Data Dictionary Methods

Method          What it Does
clear()         Empties the dictionary by remove all keys and values.
copy()          Returns a copy of the dictionary.
fromkeys()      Returns a new copy of the dictionary but with only specified keys
                and values.
get()           Returns the value of the specified key, or None if it doesn’t exist.
items()         Returns a list of items as a tuple for each key-value pair.
keys()          Returns a list of all the keys in a dictionary.
pop()           Removes the item specified by the key from the dictionary, and stores
                it in a variable.
popitem()       Removes the last key-value pair.
setdefault()    Returns the value of the specified key. If the key does not exist: insert
                the key, with the specified value.
update()        Updates the value of an existing key, or adds a new key-value pair if
                the specified key isn’t already in the dictionary.
values()        Returns a list of all the values in the dictionary.
'''