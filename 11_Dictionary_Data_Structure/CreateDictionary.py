# CREATING DICTIONARY

# d = {}
d = dict()  # empty dict

print(d)  # {}
print(type(d))  # <class 'dict'>

print("==================================================")

# 1st Way to create dictionary

d[100] = 'Steve'
d[200] = 'Eva'
d[300] = 'Rosalyn'
d[200] = 'Hana'
d[400] = 'Steve'

print(d)  # {100: 'Steve', 200: 'Hana', 300: 'Rosalyn', 400: 'Steve'}
print(type(d))  # <class 'dict'>

print("==================================================")

# 2nd Way to create dictionary
# We can also create dictionary by adding elements in advance.

d = {10: 'apple', 20: 'banana', 30: 'mango', 40: 'orange'}
print(d)  # {10: 'apple', 20: 'banana', 30: 'mango', 40: 'orange'}




























