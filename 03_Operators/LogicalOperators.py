""""
Logical Operators :-

AND &&  / OR || / NOT !

# Truth Table -

+---------+---------+---------+---------+---------+
|    a    |    b    | a and b |  a or b |  not a  |
+---------+---------+---------+---------+---------+
|   TRUE  |   TRUE  |   TRUE  |  TRUE   |  FALSE  |
+---------+---------+---------+---------+---------+
|   TRUE  |  FALSE  |  FALSE  |  TRUE   |         |
+---------+---------+---------+---------+---------+
|  FALSE  |   TRUE  |  FALSE  |  TRUE   |  TRUE   |
+---------+---------+---------+---------+---------+
|  FALSE  |  FALSE  |  FALSE  |  FALSE  |         |
+---------+---------+---------+---------+---------+
"""
# 1) Using Boolean Values :-
print("Using boolean values")
a = True
b = False
print(a and b)  # False
print(a or b)  # True
print(not b )  # True

print("===================================")
# 2) Using Non-Boolean Values :-
print("Using Non-boolean values using AND operator")

# If Zero (0) or Empty string ---> FALSE
# If Non-Zero or Non-Empty String ---> TRUE

# i) x and y --> if x is TRUE and y is TRUE then result is y
               # if x is TRUE and y is FALSE then result is y
               # if x is FALSE then result is x else it is y.

print("java" and "python")   # python
print("" and "Hollywood")   # blank_space
print("selenium" and "")  # blank_space
print(10 and 20)  # 20
print(0 and 300)  # 0
print(50 and 0)  # 0

print("=========================================")

print("Using Non-boolean values using OR operator")
# ii) x or y --> if x is FALSE and y is TRUE then result is y
               # if x is FALSE and y is FALSE then result is y
               # if x is TRUE then result is x else it is y.

print("Apple" or "Banana")   # Apple
print("" or "Motorcycle")   # Motorcycle
print("Xenomorph" or "")   # Xenomorph
print(70 or 80)  # 70
print(0 or 60)  # 60
print(90 or 0)  # 90

print("=========================================")
print("Using Using Not operator")
print(not "") # True
print(not 0)  # True






























