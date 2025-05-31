x = {10,20,30,40}
y = {30,40,50,60}

# Combined all elements in both sets
print(x.union(y))  # {40, 10, 50, 20, 60, 30}
# Common elements in both sets
print(x.intersection(y))  # {40, 30}

print("==================================================")

# Different elements in x (Which elements are different in x)
print(x.difference(y))  # {10, 20}
# Different elements in y (Which elements are different in y)
print(y.difference(x))  # {50, 60}

print("==================================================")

# Elements present in x OR y, but not in both.
print(x.symmetric_difference(y))  # {10, 50, 20, 60}
print(y.symmetric_difference(x))  # {10, 50, 20, 60}

print("==================================================")

print(250 in x)  # False
print(205 not in x)  # True

print("==================================================")

# print(x+y)  # TypeError: unsupported operand type(s) for +: 'set' and 'set'
# We need to Type Cast with List
z = list(x)+list(y)
# Will print as List []
print(z)  # [40, 10, 20, 30, 40, 50, 60, 30]

# To print as set {}
# Use se() function. This will remove duplicates because duplicates are not allowed in Set.
# Will remove 30,40
print(set(z))  # {40, 10, 50, 20, 60, 30}




























