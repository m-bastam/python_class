'''JSON (JavaScript Object Notation) data is roughly the equivalent
     of a data dictionary in Python.
JSON is a syntax for storing and exchanging data.

Serialize: Convert an object to a string.
Deserialize: Convert a string to an object.

Python JSON Methods for Serializing and Deserializing JSON Data
Method          Purpose
json.dump()     Write (serialize) Python data to a JSON file (or stream).
json.dumps()    Write (serialize) a Python object to a JSON string.
                    input: Python Dictionary -> output: JSON string 
json.load()     Load (deserialize) JSON from a file or similar object.
json.loads()    Load (deserialize) JSON data from a string. 
                    input: JSON string -> output: Python Dictionary
'''
import json
# some JSON string:
inp = '{ "name":"John", "age":30, "city":"New York"}'
print(type(inp))
# Convert from JSON to Python::
dic = json.loads(inp)
print(type(dic))
# the result is a Python dictionary:
print(f" age = {dic['age']}, name = {dic['name']} and city = {dic['city']}")

print("\t-------------1-------------\n\n")

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York",
  1 : True
}
print(type(x))
# Convert from Python to JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
print(type(y))
print("\t\t------------2--------------\n")

'''
Python and JSON Data Conversions
Python          JSON
------          ------
dict            object
list, tuple     array
str             string
int and float   number
True            true
False           false
None            null
'''
# Convert Python objects into JSON strings, and print the values
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("\t\t------------3--------------\n")
# another example
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
x = {
  "firstName": "John",
  "lastName": "Smith",
  "isAlive": True,
  "age": 27,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": "10021-3100"
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "office",
      "number": "646 555-4567"
    }
  ],
  "children": [],
  "spouse": None
}

# convert into JSON:
y = json.dumps(x)
print(y)
print ("\t\n--------------4--------------\n")

'''You can also define the separators, default value is (". ", ": "), 
which means using a dot and a space to separate each object, 
and a colon and a space to separate keys from values
sort_keys is used to sort the result alphabetically by keys
'''
y = json.dumps(x, indent = 4, separators=(". ", " = "), sort_keys = True)

# the result is a JSON string:
print(y)
print ("\t\t-------------5---------------\n")
filename = 'example_1.json'
# Open the file (standard file open stuff)
with open(filename, 'w', encoding='utf-8') as f:
  json.dump(x,f)
# This is the Excel data (no keys)
filename = 'example_2.json'
# Open the file (standard file open stuff)
with open(filename, 'r', encoding='utf-8', newline='') as f:
    # Load the whole json file into an object named products
    ''' newline='' is used to avoid bringing in the newline character at the 
    end of each row, which isn’t really part of the data. It’s just a hidden 
    character to end the line when displaying the data on the screen.
    '''
    products = json.load(f)
    print(products)
    print(type(products), len(products))
    print(products.keys())
    result = list(products.values())
    print(result[0]['sport'])
    print(result[0]['sport']['q1']['options'][2])
  