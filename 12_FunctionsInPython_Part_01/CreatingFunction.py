# FUNCTION WITHOUT PARAMETERS

def sample_function():
    print("Hello Python")
    print("Hello Python")
    print("Hello Python")

sample_function()
sample_function()
# These functions will print multiple times
# We can call the function multiple times.

# FUNCTION WITH PARAMETERS

def sample_function(name):
    print(f"Hello {name}")

sample_function("Geethika")
sample_function("Ishita")
sample_function("Deepika")

# Here, 'name' is a parameter and 'Deepika' is an argument.
# 'name is a Formal_Argument and 'Deepika' is an Actual_Argument.

print("======================== TYPES OF FUNCTIONS ============================")
"""
1) Function with No parameters and No return value
2) Function with parameters and No return value
3) Function with parameters and return value
4) Function with No parameters and return value
"""

print("============== 1) Function with No parameters and No return value ===============")

def sunday():
    print("This is Sunday")

sunday()  # This is Sunday
print(sunday())   # This is Sunday # None [Because function do not returning any value]


print("============== 2) Function with parameters and No return value ===============")

def firstDay(day):
    print(f"This is {day}")

# firstDay("Monday")  # This is Monday  # Here Monday is an actual argument.
print(firstDay("Monday"))   # 1. This is Monday  # 2. None [Because function do not returning any value]

print("============== 3) Function with parameters and return value ===============")

def myfunc(name):
   return f"Hello {name}"
myfunc("Stacy")   # Not printed
print(myfunc("Stacy"))  # Hello Stacy # Printed only once. [Used return keyword - returning value]

print("============== 4) Function with No parameters and return value ===============")

def myfunc():
   return f"Hello Stacy"
myfunc()   # Not printed
print(myfunc())  # Hello Stacy  # Printed only once. [Function returning value]

print("============== Function in Python can return any number of values ===============")
# Those multiple values return in the form of tuple.

def myfunc():
   return "Hello Stacy", "Hello John", "Hello Tom"
t = myfunc()
print(myfunc())  # ('Hello Stacy', 'Hello John', 'Hello Tom')

# return in the form of tuple, further if we want the values separately, we can do it by tuple unpacking.
a,b,c = t   # Tuple Unpacking
print(a)
print(b)
print(c)





















