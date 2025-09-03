# eval() function -  Evaluates the data type
# print(input("Enter data:"))  # 10
var1 = eval(input("Enter data:"))
print(type(var1))   # <class 'int'>

"""
Case 1 :
------
var1 = eval(input("Enter data:"))  # 10
print(type(var1))   # <class 'int'>


Case 2 :
------
var1 = eval(input("Enter data:"))   # 10, "Ishita", 50000.12, 26
print(type(var1))   # <class 'tuple'>


Case 3 :
------
var1 = eval(input("Enter data:"))   # [10, 'ishita', 50000, 26]
print(type(var1))   # <class 'list'>


Case 4 :
------
var1 = eval(input("Enter data:"))   # {10,20,30,40,50}
print(type(var1))   # <class 'set'>


Case 5 :
------
var1 = eval(input("Enter data:"))   # {"name":"Ishita", "Age":6, "Height":4.5}
print(type(var1))   # <class 'dict'>
 
"""
