s = {}
print(s)  # {}
print(type(s))  # <class 'dict'>

# This shows the data type as dictionary, not set data type.
# But if we want to declare empty data set, use empty set function - 'set()'
#============================================================================================

s = set()  # Empty Set
print(s)  # set()
print(type(s))  # <class 'set'>
print("======================= Adding elements to Empty Set ===========================")

s.add(10)
s.add(20)
s.add(30)
s.add(40)
print(s)  # {40, 10, 20, 30}
print(type(s))  # <class 'set'>

print("==================================================")

s = {40,12.9,True,"Welcome",'k',10+5j,40,"Welcome"}
print(s)  # {True, 'Welcome', 40, (10+5j), 'k', 12.9}  # Duplicates not allowed
print(type(s))  # <class 'set'>

print("==================================================")

# s = eval(input("Enter data -"))
# print(s)  # {60,70,"John",12.5,False}
# print(type(s)) # <class 'set'> # If not used eval() function >> <class 'str'>

print("==================================================")
s = set(range(11))  # Type Casting - Set with Range Data Type
print(s)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(type(s))  # <class 'set'>

print("==================================================")
s = {10,20,30,40,20,50,60,20,70}
# print(s[1])  # TypeError: 'set' object is not subscriptable
# Indexing is not supporting in Set data structure
slist = list(s)  # We need to Type Cast with List
print(slist[1])  # 20

# Slicing is not supporting in Set data structure
# print(s[0:3])  # TypeError: 'set' object is not subscriptable

































































