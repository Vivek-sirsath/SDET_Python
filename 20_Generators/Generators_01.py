# Generators :-
# 'yield' is also like 'return'. Because if it is a normal function it returns some value.
# Instead of 'return' if we use 'yield' keyword. That'll be generator function.

def my_generator():
    yield 1
    yield 2
    yield 3

# If we call 'my_generator()' function, it will return a 'Generator Object'
# print(my_generator())   # <generator object my_generator at 0x0000026BB9B65E80>

gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3  # It is able to remembers current state.
# print(next(gen))  # Error



