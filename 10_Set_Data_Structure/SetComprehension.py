# SET COMPREHENSION

"""
SYNTAX :
        {expression for item in iterable_object if condition}

        e.g.
            {x*x           for     x       in      range(11)       if       x%2==0}
            {expression    for    item     in    iterable_object   if    condition}

        {[For each item in sequence (iterable_object) with if filter condition, upon applying expression]}
        It will generate some value.

"""
s = {x*x for x in range(11) if x%2==0}
print(s)  # {0, 64, 4, 36, 100, 16}


s = {x*x for x in range(5)}
print(s)  # {0, 1, 4, 9, 16}

s = {2**x for x in range(10)}
print(s)  # {32, 1, 2, 64, 4, 128, 256, 512, 8, 16}