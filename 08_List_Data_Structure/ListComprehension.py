# LIST COMPREHENSION
"""
SYNTAX :
        {expression for item in iterable_object if condition}

        e.g.
            {x*x           for     x       in      range(11)       if       x%2==0}
            {expression    for    item     in    iterable_object   if    condition}

        {[For each item in sequence (iterable_object) with if filter condition, upon applying expression]}
        It will generate some value.
"""

print(list(range(11)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print the square of even numbers in range(11) - 0 to 10
list_1 = [x*x for x in range(11) if x%2==0]
print(list_1)  # [0, 4, 16, 36, 64, 100]

# Extracting the first character of string
Color_list = ["Red", "Pink", "Yellow", "White", "Black"]
l = [color[0] for color in Color_list]
print(l)  # ['R', 'P', 'Y', 'W', 'B']

# Extracting the last character of string
Color_list = ["Red", "Pink", "Yellow", "White", "Black"]
last_chars = [color[-1] for color in Color_list]
print(last_chars)  # ['d', 'k', 'w', 'e', 'k']















