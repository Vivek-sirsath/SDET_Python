def order_pizza(size,*toppings):
    print(f"Order a {size} sized pizza with toppings: {','.join(toppings)}")

order_pizza("Medium")
order_pizza("Large", "Pepperoni", "Mushroom", "Olives")
order_pizza("Small", "Onion", "Corn")


print("===============================================================================")


def sum(a,*b):
    print(a)
    print(b)

sum(5)   # Here a = 5 has taken.
"""
Output:
5
()
"""

print(type(sum(5)))  # <class 'NoneType'>

print(type(sum(3,4,5,6))) # # <class 'NoneType'>
"""
3
(4, 5, 6)
"""
















