# We can use Positional as well as Keyword Arguments combined.
# But, first we should specify Positional and then Keyword Arguments.

def greet(name, msg):
    print("Hello", name,msg)

greet("Isha","Good Morning!")  # Hello Isha Good Morning!  # VALID
greet("Isha", msg = "Good Morning!")  # Hello Isha Good Morning!  # VALID
# greet(name= "Isha","Good Morning..!")   # SyntaxError: positional argument follows keyword argument   # INVALID



















