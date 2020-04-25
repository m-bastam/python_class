names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
names.sort(reverse=True)
print(names)

names.sort(key = len )
print(names)

def lowercaseof(anystring):
    """ Converts string to all lowercase """
    return anystring.lower()

names.sort(key = lowercaseof)
print(names)

names_lambda = names.copy()
# use lambda(ananymous) funcion
names_lambda.sort(key = lambda anystring: anystring.lower())
#The original data is still in its original uppercase and lowercase letters.
print(names)
print (names_lambda)

print("\t---------------------\n\n")
# show number in currency format
currency_format = lambda n : f"${n:,.2f}"

# show number in percent format
percent_format = lambda n : f"${n:,.2%}"

# Test currency and percent Functions
print(currency_format(99))
print(currency_format(12345.087857))
print(percent_format(0.065))
print(percent_format(.5))

id = currency_format(123.32)
print(id , type(id))

numbers = [1,2,32,4,56,12,23,2]
numbers.sort()
print(numbers)

x = lambda a : a + 10 * 2
print(x(2)) 