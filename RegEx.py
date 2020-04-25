'''A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.

complete list of the metacharacters:  . ^ $ * + ? { } [ ] \ | ( )
[ , ] are used for specifying a character class: example [a-c] or [abc] is equal a,b,c
Metacharacters are not active inside classes.  
    For example, [akm$] will match any of the characters 'a', 'k', 'm', or '$'
'^'   Starts with "^hello" 	or [^5] will match any character except '5'.  If the caret appears elsewhere in a 
      character class, it does not have special meaning.
    [^arn] 	Returns a match for any character EXCEPT a, r, and n
      
'$'   Ends with   "world$"

\d    Matches any decimal digit; this is equivalent to the class [0-9].
\D    Matches any non-digit character; this is equivalent to the class [^0-9].
\s    Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
\S    Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
\w    Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
\W    Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].

\b 	  Returns a match where the specified characters are at the beginning or at the end of a word
      r"\bain" , r"ain\b"
\Z 	 Returns a match if the specified characters are at the end of the string. "Spain\Z"
For example, [\s,.] is a character class that will match any whitespace character, or ',' or '.'.

'.'   matches anything except a newline character
'*'   specifies that the previous character can be matched zero or more times, instead of exactly once.
      For example, ca*t will match 'ct' (0 'a' characters), 'cat' (1 'a'), 'caaat' (3 'a' characters), and so forth.
'+'   Another repeating metacharacter which matches one or more times. 
      For example, ca+t will match 'cat' (1 'a'), 'caaat' (3 'a's), but won’t match 'ct'.
'?'   matches either once or zero times.      
      For example, home-?brew matches either 'homebrew' or 'home-brew'    
{m,n} where m and n are decimal integers. This qualifier means there must be at least
     m repetitions, and at most n. 
     For example, a/{1,3}b will match 'a/b', 'a//b', and 'a///b'.
     {0,} is the same as *, {1,} is equivalent to +, and {0,1} is the same as ?   
'''
'''
The re module offers a set of functions that allows us to search a string for a match:
Function 	Description
findall 	Returns a list containing all matches
search 	    Returns a Match object if there is a match anywhere in the string
split   	Returns a list where the string has been split at each match
sub 	    Replaces one or many matches with a string
'''


import re

#Check if the string starts with "The" and ends with "Spain":
# If there is no match, the value None will be returned, instead of the Match Object.
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if (x):
  print("YES! We have a match!")
else:
  print("No match")

# If there is more than one match, only the first occurrence of the match will be returned
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

print('\t------------------------\n')

# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":
x = re.search(r"\bS\w+", txt)
print(x.span())  #.span() returns a tuple containing the start-, and end positions of the match.
print(x.string)  # .string returns the string passed into the function
print(x.group()) #.group() returns the part of the string where there was a match

print('\t------------------------\n')

#Split the string at every white-space character:
x = re.split("\s", txt)
print(x)

#You can control the number of occurrences by specifying the maxsplit parameter:
x = re.split("\s", txt, 1)
print(x)

print('\t------------------------\n')

#Check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)
if (x):
  print("Yes, there is a match!")
else:
  print("No match")

print('\t------------------------\n')

txt = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\d", txt)
print(x)

print('\t------------------------\n')

txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x)

print('\t------------------------\n')

#Replace all white-space characters with the digit "9":
x = re.sub("\s", "-", txt)
print(x)

# You can control the number of replacements by specifying the count parameter:
x = re.sub("\s", "-", txt, 2)
print(x)

