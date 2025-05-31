#  TUPLE COMPREHENSION

"""

 SYNTAX :
           (expression for item in sequence if condition)  -->  generator object

e.g.
            {x**2          for     x       in      range(1,6)     --------------- }
            {expression    for    item     in      sequence        if    condition}
"""

t = [x**2 for x in range(1,6)]

print(t)  # [1, 4, 9, 16, 25]
print(type(t))  # <class 'list'>

print("==================================================")

# Tuple comprehension gives generator object
t = (x**2 for x in range(1,6))

print(t)  # <generator object <genexpr> at 0x0000026E48A5B850>
print(type(t))  # <class 'generator'>


