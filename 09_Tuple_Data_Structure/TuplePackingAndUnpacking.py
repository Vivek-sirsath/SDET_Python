"""
TUPLE PACKING AND UNPACKING
---------------------------

Tuple packing is the process of combining multiple values in a single tuple in a single statement.
Tuple unpacking is the process of assigning the values from a tuple to multiple variables in a single statement.

Tuple unpacking is the reverse process of Tuple packing.

"""
# Tuple Packing :
print("================= TUPLE PACKING===================")
a = 10
b = 20
t = a,b   # --> Tuple Packing
print(t)  # (10, 20)

# Tuple Unpacking :
print("================= TUPLE UNPACKING===================")
t = (50,60,70)
# a,b,c,d = t  # ValueError: not enough values to unpack (expected 4, got 3)
# No of variables must match the no of values, otherwise 'ValueError' will occur.
a,b,c = t
print(a)  # 50
print(a,b,c)  # 50 60 70











