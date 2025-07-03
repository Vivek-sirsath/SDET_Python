"""
What is a Function?

A function is a reusable block of code that performs a specific task.
Think of it as a machine: you give it some input (arguments), it processes something, and then gives you output.
"""
# Defining a Function
# --------------------
# Here’s the basic structure:

# Function without parameters :-
# ---------------------------
def greet():
    print("Hello, Python learner!")

greet()   # Hello, Python learner!


# Function with parameters :-
# ------------------------
def greet(name):
    print(f"Hello, {name}!")

greet("Sam")   # Hello Sam


# Function with Return Values :
# ---------------------------
# Functions can return values instead of just printing them.

def add(a, b):
    return a + b

result = add(15, 20)
print(result)   # 35

