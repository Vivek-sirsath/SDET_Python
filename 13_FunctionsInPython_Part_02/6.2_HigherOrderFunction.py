# HIGHER ORDER FUNCTION :

# EXAMPLE 1 :-

def apply_function(func,value):
    return func(value)
def square(num):
    return num**2

# Here, apply_function() calling another function square()

print(apply_function(square,3))  # 9

print("=======================================================================")

# EXAMPLE 2 :-

def areaOfCircle(func,radius):
    return func(radius)
def squareOfRadius(radius):
    return 3.14*radius**2

print(areaOfCircle(squareOfRadius,5))  # 78.5







