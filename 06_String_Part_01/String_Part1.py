
# String Creation
# 1) By using quotes

s = ''
st =""
print(s)     # empty string, blank output
print(st)    # empty string, blank output
print(type(s))   # <class 'str'>

# 2) By using type casting using 'str()' function

a = 10
print(a)  # 10
print(type(a)) # <class 'int'>
print(type(str(a))) # <class 'str'>

# - In Java, single character in single quote 'w' is a char data type. But in Python it is also a String data type.
s = 'w'
print(type(s)) # <class 'str'>

s = "123"
print(type(s)) # <class 'str'>

print("=============================================")

# Multiline Sting Literals :-

# It can be achieved by using ''' '''  OR """ """

s = "Welcome to Python Programming"
print(s) # Welcome to Python Programming

print("=============================================")

s = ("Welcome to "
     "Python "
     "Programming")
print(s)  # Welcome to Python Programming

print("=============================================")

s = """ 
        Welcome 
          to
        Python
      Programming 
    """
print(s)  # Same as above

print("===================== Use of Opposite Quotes ========================")

# We should never use same quotes inside same quotes.
# s = "Welcome to "Python" Programming"
# print(s) # SyntaxError: invalid syntax

# Use opposite quotes for the solution
s = "Welcome to 'Python' Programming"
print(s) # Welcome to 'Python' Programming

s = 'Welcome to "Python" Programming'
print(s) # Welcome to "Python" Programming

s = """ 
        Welcome 
          to
        'Python'
      Programming """
print(s) # Same as above

print("===================== Use of escape character \ backslash to resolve Quote Conflict ========================")

# Use of escape character (\) - backslash

s = """Welcome to 'Python' "Programming\""""
print(s)

print("==================== Accessing characters in String =========================")

# How to access characters in a String? :-

# 1) indexing
#    --------

"""
         String Slicing

        0   1   2   3   4   5   6
        W   E   L   C   O   M   E
       -7  -6  -5  -4  -3  -2  -1
       
"""

s = "welcome"
print(len(s))  # 7

print(s[2])  # l
print(s[6])  # e
print(s[-4])  # c

# Range of Indexes

# print(s[10])  # IndexError: string index out of range
# print(s[-8])  # IndexError: string index out of range

print("====================== Slice Operator (:) =======================")

# 2) slice operator (:)
#    --------------
print(list(range(1,10)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

s = "123456789"

print(s[2:7])  # 34567    # Default step is 1
print(s[1:9])  # 23456789
print(s[1:9:2])  # 2468
print(s[:5])   # 12345
print(s[5:])   # 6789
print(s[::])  # 123456789
print(s[4:100000:1])  # 56789
print(s[100000:5:1])  # Blank_output

print("===================== Using Step ========================")

# 123456789

print(s[::-1])  # 987654321
print(s[7:3:-1])  # 8765
print(s[7:3:1])   # Blank_output
print(s[3:7:1])  # 4567
print(s[5:5:1])   # Blank_output
print(s[5:5:-1])   # Blank_output

print("=============================================")

s = "Programming"

print(s[2:7])  # ogram     # Default step is 1
print(s[1:9])  # rogrammi
print(s[1:9:2])  # rgam
print(s[:5])   # Progr
print(s[3:])  # gramming
print(s[::])  # Programming
print(s[4:100000:1])  # ramming
print(s[100000:5:1])  # Blank_output

print("=============================================")
# 0 1 2 3 4 5 6 7 8 9 10
# P r o g r a m m i n g

print(s[::-1])  # gnimmargorP
print(s[7:3:-1])  # mmar
print(s[7:3:1])   # Blank_output  # Can not traverse in reverse index
print(s[3:7:1])  # gram
print(s[5:5:1])   # Blank_output
print(s[5:5:-1])   # Blank_output
