# ACCESSING DATA FROM DICTIONARY

d = {10: 'apple', 20: 'banana', 30: 'mango', 40: 'orange'}

print(d[30])  # mango
# print(d[90])  # KeyError: 90

print("==================================================")

# UPDATE DATA OF DICTIONARY

print(d)  # {10: 'apple', 20: 'banana', 30: 'mango', 40: 'orange'}
d[30] = 'strawberry'
print(d)  # {10: 'apple', 20: 'banana', 30: 'strawberry', 40: 'orange'}

# If the key is not available in the dictionary, a new entry will be created.
d[60] = 'cashew'
print(d)  # {10: 'apple', 20: 'banana', 30: 'strawberry', 40: 'orange', 60: 'cashew'}

print("==================================================")

# DELETE DATA FROM DICTIONARY

# To delete, we have to use the keyword 'del'
# This will delete permanently from the dictionary. We can't get back that data.
# This is unbound operation.

del d[10]
del d[20]
print(d)  # {30: 'strawberry', 40: 'orange', 60: 'cashew'}

# DELETE ALL DATA FROM DICTIONARY
d.clear()
print(d)  # Empty Dictionary






