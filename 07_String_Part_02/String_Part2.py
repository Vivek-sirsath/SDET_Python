print("==================== Concatenation Operator (+) ====================")
# Concatenation Operator(+)
s1 = "Welcome"
s2 = " to Python Programming"
s3 = s1+s2
print(s3) # Welcome to Python Programming

"""
s4 = s1+2  # (String + int) Not-Possible 
print(s4)  # TypeError: can only concatenate str (not "int") to str
"""
print("==================== Repetition Operator (*) ====================")

# Repetition Operator (*)
# If we want to repeat a String multiple times

# (s1 - String, 5 - int)
s5 = s1*5  # Repetition Possible
print(s5)  # WelcomeWelcomeWelcomeWelcomeWelcome

"""
s6 = s1*s2  # (String * String) Repetition Not-Possible
print(s6)  # TypeError: can't multiply sequence by non-int of type 'str'
"""
print("==================== len() ====================")

# len() - Returns the count of the sequence of characters in a String.

str = "How are you?"
print(len(str))   # 12

print("=================== Check Presence of character or substring in a string =====================")

# How to check the presence of character or substring in main string.
# Identity Operators --> is , is not
# Membership Operators --> in , not in   ---> Returns Boolean - True / False

print("y" in str)  # True
print("z" in str)  # False
print("Python" in s2)  # True  # Case sensitive
print("python" not in s2) # True   # Case sensitive
print("========================================")
print("Java" in s2) # False
print("Java" not in s2)  # True

print("=================== Remove spaces in string =====================")

# Remove spaces in string :
# rstrip() --> removes spaces from right
# lstrip() --> removes spaces from left
# strip() --> removes spaces from both sides

s = "  Hollywoo d    "
print(s.rstrip())
print(s.lstrip())
print(s.strip())  # Hollywoo d

print("================== Comparison of string =======================")

### Comparison of string :

# Done on ASCII code
# First character comparison will be done.
# If first character is same it will check for second character.

# ord() - returns ASCII code
print(ord('J'))  # 74 - ASCII code
print(ord('~'))  # 126

# chr() - returns character. If we want to return a character based on ASCII code.
print(chr(61))  # =
print(chr(75))  # K

print("==================== String Comparison based on ASCII code ====================")

s7 = "Maple"
s8 = "Apple"
print(ord('M'))  # 77
print(ord('A'))  # 65
print(s7<s8)  # False
print(s7>s8)  # True because 77 > 65

print("========================================")

s9 = "Parrot"
s10 = "Prayer"
print(ord('a'))  # 97
print(ord('r'))  # 114
print(s9<s10)  # True  # 97 < 114
print(s9>s10)  # False
print(s9==s10)  # False

print("========================================")

s11 = "Paragraph"
s12 = "Parachute"
print(ord('g'))  # 103
print(ord('c'))  # 99
print(s11<s12)  # False
print(s11>s12)  # True  # 103 > 99
print(s11==s12)  # False

print("================== Find() function - Related to substring ======================")

### Find() function - Related to substring
s = "Python is very very simple"

# find() --> Returns index of first occurrence of string  --> Returns '-1' if not found
# index() --> Same as find() --> Returns 'ValueError' if not found
#
# rfind() --> Returns index of last occurrence of string  --> Returns '-1' if not found
# rindex() --> Same as rfind() --> Returns 'ValueError' if not found

print(s.find("very"))  # 10 (starting index of first occurrence of string )
print(s.rfind("very")) # 15 (starting index of last occurrence of string )
print(s.find("java"))  # -1

print(s.index("very"))  # 10
print(s.rindex("very"))  # 15

# If string not present
#print(s.rindex("java"))  # ValueError: substring not found
#print(s.index("java"))  # ValueError: substring not found

# We can also specify boundaries indices
print(s.find("very", 12,18))  # -1 (within these boundaries, no occurrence)
print(s.find("very", 7,18))  # 10 (within these boundaries, occurrence of 'very' at starting index 10)

print("================== count() - no of times string occurred ======================")

print(s.count("very"))  # 2

print("================== replace() - replace substring in a main string ======================")

s = "Learning Python is very difficult"
print(s)  # Learning Python is very difficult
new = s.replace("difficult", "easy")
print(s)  # Learning Python is very difficult
# (String is immutable, we've to create a new string variable to store changes)
# We can not modify the original string. We've to create new object (new)
print(new)  # Learning Python is very easy

print("================== splitting and joining the string ======================")
print("================== splitting ======================")
# split() - This method split the string based on seperator and return the List
# SYNTAX: s.split(seperator)
# space - is default seperator

s = "03-12-2025"
print(s.split("-"))  # ['03', '12', '2025']
print(s.split("/"))  # ['03-12-2025'] => Because, it is without seperator of original string.

s1 = "Learning Python is very easy" # Here, space is default seperator
print(s1.split())  # ['Learning', 'Python', 'is', 'very', 'easy']

print("================== joining ======================")

# join() - This method joins the sequence based on seperator and return the String
# The sequence can be list, tuple, set, dictionary.
# SYNTAX: seperator.join(sequence)

l =["Chicago", "London", "Dubai", "Mumbai"]
# string_new = "-".join(l)
# print(string_new)  # Chicago-London-Dubai-Mumbai

# string_new = "/".join(l)
# print(string_new)  # Chicago/London/Dubai/Mumbai

string_new = " ".join(l)
print(string_new)  # Chicago London Dubai Mumbai

print("================== Changing the case of the string ======================")

s = "Learning Pyhon is very easy"
print(s.upper())  # LEARNING PYHON IS VERY EASY
print(s.lower())  # learning pyhon is very easy
print(s.swapcase())  # lEARNING pYHON IS VERY EASY

print("========================================")
# If we want to convert to title case
print(s.title())  # Learning Pyhon Is Very Easy
print(s.capitalize())  # Learning pyhon is very easy

print("================== Check type of characters present in the string ======================")

print('Priya123'.isalnum())  # True (Check whether alphanumeric)
print('Priya123'.isalpha())  # False (Check whether alphabetic)
print('Priya'.isalpha())  # True
print('Priya123'.isdigit())  # False (Check whether digits)
print('564123'.isdigit())  # True
print('Learning Python is very easy'.istitle())  # False
print('Learning Pyhon Is Very Easy'.istitle())  # True
print(' '.isspace())  # True

print("================== String formatting ======================")

name = 'Vivek'
salary = 95000
location = 'London'

# print('My name is vivek, my salary is 95000 and located in London' )  # My name is vivek, my salary is 95000 and located in London

# Using f-string
print(f"My name is {name}, my salary is {salary} and located in {location}")

# Using format() method
print('My name is {}, my salary is {} and located in {}'.format(name,salary,location))











