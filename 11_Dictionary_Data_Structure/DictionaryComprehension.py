# DICTIONARY COMPREHENSION

"""
SYNTAX :
        {expression for item in iterable_object if condition}

        e.g.
            {x*x           for     x       in      range(11)       if       x%2==0}
            {expression    for    item     in    iterable_object   if    condition}

        {[For each item in sequence (iterable_object) with if filter condition, upon applying expression]}
        It will generate some value.
"""

d = {x:x*x for x in range(1,6)}
print(d)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

d= {x:x**x for x in range(0,6)}
print(d)  # {0: 1, 1: 1, 2: 4, 3: 27, 4: 256, 5: 3125}



























