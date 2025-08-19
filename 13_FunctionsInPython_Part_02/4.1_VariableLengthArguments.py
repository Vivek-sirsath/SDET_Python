# VARIABLE LENGTH ARGUMENTS -

# Length of parameters (no of parameters) is not fixed. We can pass any no of arguments (even zero) using *.
# In Variable length arguments (*n), values are stored as a tuple ().
# In Keyword Variable length arguments (**kwargs), values are stored as a dictionary {}.
# After variable length arguments there must be keyword arguments.


def order_pizza(size,*toppings):
    print(f"Order a {size} sized pizza with toppings: {','.join(toppings)}")

order_pizza("Medium")
order_pizza("Large", "Pepperoni", "Mushroom", "Olives")
order_pizza("Small", "Onion", "Corn")


print("============= Variable Length Arguments with Positional Argument ========================")


def sum(a,*b):
    print(a)
    print(b)

sum(7)   # Here a = 7 has taken.
"""
Output:
5
()
"""

print(type(sum(5)))   # 5  # () # <class 'NoneType'>

sum(2,3,4,5)
print(type(sum(3,4,5,6)))  # <class 'NoneType'>
"""
3
(4, 5, 6)
"""
print("=============================== Variable Length Arguments ===============================")

def varLengthArguments(*n):
    print(n)


varLengthArguments()  # () - EMPTY TUPLE
varLengthArguments(10)   # (10,)
varLengthArguments(10,20,30)   # (10, 20, 30)


