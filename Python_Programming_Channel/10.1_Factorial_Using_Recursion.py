"""
What is Recursion?

Recursion is when a function calls itself to solve smaller parts of a problem
- ideal for tasks that can be broken down into repetitive subproblems.
- Recursion breaks complex problems into simpler instances of the same problem, solving each recursively.
- Without a base case, the function keeps calling itself until Python’s maximum recursion depth is exceeded,
  which throws a RecursionError.

Basic Recursive Structure :-

def function_name():
    # base condition
    if condition:
        return something
    else:
        return function_name()  # recursive call

Without a base condition, the function will keep calling itself forever — causing a RecursionError.

"""

n = int(input("Enter any number: "))

def factorial(n):
    if n == 0 or n == 1:  # base case
        return 1
    else:
        return n*factorial(n-1)

print(factorial(n))   # 5! = 120

print("============================== Example 2 ==============================")

# Example 2 :-

def mystery(n):
    if n == 0:
        return 0
    else:
        return n + mystery(n - 1)

print(mystery(6))  # 6+5+4+3+2+1+0 = 21








