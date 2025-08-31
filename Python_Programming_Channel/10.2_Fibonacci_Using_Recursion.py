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

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(n):
    print(fibonacci(i), end=" ")