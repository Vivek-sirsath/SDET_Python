# Types of Function With Arguments :-
# ------------------------------

# 1. Positional Arguments :-

# These are the most common — the order matters.

def greet(name, age):
    print(f"{name} is {age} years old.")

greet("Alex", 25)


# 2. Keyword Arguments :-

# You specify the name of the argument, so order doesn’t matter.

greet(age=25, name="Alex")


# 3. Default Arguments :-

# Provide a default value so the argument becomes optional.
# In Python, parameters with default values must come after non-default ones. So x is required, y is optional.

def greet(name, city="Delhi"):
    print(f"{name} is from {city}")

greet("Riya")             # Uses default city
greet("Riya", "Mumbai")   # Overrides default
greet("Vivek")   # Vivek is from Delhi


# 4. Variable-length Arguments :-

# *args for multiple positional values (tuple)
# **kwargs for multiple keyword values (dictionary), Multiple Key-Value pairs

print("============ Example of '*args' for multiple positional values (tuple) ============")

def total(*numbers):
    return sum(numbers)

print(total(2, 4, 6))  # Outputs: 12


print("============ Example of '**kwargs' for multiple keyword values {dictionary} ============")

def display_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")
    print(data)

display_info(name="John", age=30, location="Atlanta, GA", profession="Tester")
print("")
display_info(name="Stacy", age="25", profession="Model")
