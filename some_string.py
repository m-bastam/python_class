#Sat 11 Apr 2020 11:22:08 PM +0430 

username = """Alan"""
print(f"Hello {username}")

birth_year = 1982
birth_month = 12
birth_day = 23

message = f"My birth date is: {birth_year}/{birth_month}/{birth_day}"
print (message)

message2 = "My birth date is:{0}-{1}-{2}".format(birth_year, birth_month, birth_day)
print(message2)

print("\t-----------1--------------\n")
unit_price = 49.99
quantity = 30
print(f"Subtotal: ${quantity * unit_price}")
print(f"Subtotal: ${quantity * unit_price:,.2f}")

sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate}")
print(f"Sales Tax Rate {sales_tax_rate:.1%}")
print("\t-------------2------------\n")
s1 = ""
s2 = " "
s3 = "A B C"
print(len(s1))
print(len(s2))
print(len(s3))
# print(len(10))


print(ord("A"))
print(chr(65))
print("\t-------------3------------\n")

# for char_num in range(20, 120):
#     print(chr(char_num), ord(chr(char_num)), end = " , ")
    
print("\t-------------4------------\n")
str_text = 'This Message is written for testing some STRING methods!'
print (str_text.count("is"))
print(len(str_text))
print("m" in str_text)
print('l' not in str_text)
print('for' in str_text)
print("A#" * 15)

list_str = str_text.split("is", 1)
print(f" split string = {list_str}")
print(list(str_text))

print("\t--------------5-----------\n")
print(str_text[0])
print(str_text[20:40])
print(str_text[0::4])
print(min(str_text))
print(max(str_text))
print(str_text.index("t"))
print(str_text.count("t"))

print("\t ----------6----------\n")
s2 = "    a b c    "
s3 = "ABC"
s4 = "1235"
print(s3.capitalize())
print(s2.count(" "))
print(str_text.find("t"))
print(s2.islower())
print(s3.lower())
print(len(s2.lstrip()), s2.lstrip())
print(len(s2.rstrip()), s2.rstrip())
print(len(s2.strip()), s2.strip())
print(str_text.swapcase())
print(str_text.title())
print(str_text.lower())
print(s4.isalpha())
print(s4.isnumeric())
print("\t-------------7------------\n")

# a module for delete punctuation in sentence
import del_punc 

in_st=input("Enter a string with punctuation :" )
print(in_st)

st_without_punc = del_punc.del_punctuation(in_st)
print (st_without_punc)


'''
Built-In Methods for Python 3 Strings

Method                      Purpose
-----------------           ------------------
s.capitalize()              Returns a string with the first letter capitalized, 
				the rest lowercase.
s.count(x,[y,z])            Returns the number of times string x appears in string s.
				 Optionally you can add y as a starting point and z 
				 as an ending point to search only a portion of the string.
s.find(x,[y,z])             Returns a number indicating the first position at which string
				 x can be found in string s. Optional y and z parameters 
				 allow you to limit the search to a portion of the string.
				 Returns –1 if none found.
s.index(x,[y,z])            Similar to find but returns a “substring not found” error if 
				string x can’t be found in string y .
s.isalpha()                 Returns True if s is at least one character long and contains
				only letters (A-Z or a-z).
s.isdecimal()               Returns True if s is at least one character long and contains
				only numeric characters (0-9).
s.islower()                 Returns True if s contains letters and all those letters are lowercase.
s.isnumeric()               Returns True if s is at least one character long and contains
				only numeric characters (0-9).
s.isprintable()             Returns True if string s contains only printable characters.
s.istitle()                 Returns True if string s contains letters and the first letter 
				of each word is uppercase followed by lowercase letters.
s.isupper()                 Returns True if all letters in the string are uppercase.
s.lower()                   Returns s with all letters converted to lowercase.
s.lstrip()                  Returns s with any leading spaces removed.
s.replace(x,y)              Returns a copy of string s with all characters x replaced by character y .
s.rfind(x,[y,z])            Similar to find but searches backwards from the start of the string.
				 If y and z are provided, searches backwards from position z to
				 position y . Returns –1 if string x not found.
s.rindex()                  Same as .rfind but returns an error if the substring isn’t found.
s.rstrip()                  Returns string x with any trailing spaces removed.
s.strip()                   Returns string x with leading and trailing spaces removed.
s.swapcase()                Returns string s with uppercase letters converted to lowercase
				and lowercase letters converted to uppercase.
s.title()                   Returns string s with the first letter of every word capitalized
				and all other letters lowercase.
s.upper()                   Returns string s with all letters converted to uppercase.

s.split(sep, maxsplit)->list
                            Return a list of the words in the string, using sep as the delimiter 
                            string. sep The delimiter according which to split the string.
                            None (the default value) means split according to any whitespace,
                            and discard empty strings from the result. maxsplit Maximum number 
                            of splits to do. -1 (the default value) means no limit.

'''    
    
    
