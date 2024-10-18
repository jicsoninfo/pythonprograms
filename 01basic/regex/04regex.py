reg01 = '''
The findall() Function
The findall() function returns a list containing all matches.

Example
Print a list of all matches:

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
The list contains the matches in the order they are found.

If no matches are found, an empty list is returned:

Example
Return an empty list if no match was found:

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)
 
The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.

If there is more than one match, only the first occurrence of the match will be returned:

Example
Search for the first white-space character in the string:

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
If no matches are found, the value None is returned:

Example
Make a search that returns no match:

import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
 
The split() Function
The split() function returns a list where the string has been split at each match:

Example
Split at each white-space character:

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
You can control the number of occurrences by specifying the maxsplit parameter:

Example
Split the string only at the first occurrence:

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

'''

#print(reg01)

import re
#Return a list containing every occurrence of "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


#Return an empty list if no match was found:
import re
txt = "The rain in Spain"
#Check if "Portugal" is in the string:
x = re.findall("Portugal", txt)
print(x)
if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")



#Search for the first white-space character in the string:
#If there is more than one match, only the first occurrence of the match will be returned:
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start()) 


#If no matches are found, the value None is returned:
import re
txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)



#The split() function returns a list where the string has been split at each match:
#Split at each white-space character:
import re
#Split the string at every white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)


#You can control the number of occurrences by specifying the maxsplit parameter:
import re
#Split the string at the first white-space character:
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

reg02 = '''
The sub() Function
The sub() function replaces the matches with the text of your choice:

Example
Replace every white-space character with the number 9:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)
You can control the number of replacements by specifying the count parameter:

Example
Replace the first 2 occurrences:

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
 
Match Object
A Match Object is an object containing information about the search and the result.

Note: If there is no match, the value None will be returned, instead of the Match Object.

Example
Do a search that will return a Match Object:

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
Example
Print the position (start- and end-position) of the first match occurrence.

The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
Example
Print the string passed into the function:

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
Example
Print the part of the string where there was a match.

The regular expression looks for any words that starts with an upper case "S":

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
Note: If there is no match, the value None will be returned, instead of the Match Object.


'''
#print(reg02)


#The sub() function replaces the matches with the text of your choice:
#Replace every white-space character with the number 9:
import re
#Replace all white-space characters with the digit "9":
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)



#You can control the number of replacements by specifying the count parameter:
#Replace the first 2 occurrences:
import re
#Replace the first two occurrences of a white-space character with the digit 9:
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

#A Match Object is an object containing information about the search and the result.
#Note: If there is no match, the value None will be returned, instead of the Match Object.
#Do a search that will return a Match Object:
import re
#The search() function returns a Match object:
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)



#The Match object has properties and methods used to retrieve information about the search, and the result:
#.span() returns a tuple containing the start-, and end positions of the match.
#.string returns the string passed into the function
#.group() returns the part of the string where there was a match

#Print the position (start- and end-position) of the first match occurrence.

#The regular expression looks for any words that starts with an upper case "S":
import re
#Search for an upper case "S" character in the beginning of a word, and print its position:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

#Print the string passed into the function:
import re
#The string property returns the search string:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

#Print the part of the string where there was a match.
#The regular expression looks for any words that starts with an upper case "S":
import re
#Search for an upper case "S" character in the beginning of a word, and print the word:
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())



