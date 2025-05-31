# Creation of tuple
t = ()  # Empty tuple
print(t)  # ()
print(type(t))  # <class 'tuple'>

print("===================================================")

t = (10)   # If we enter only int without comma, returns int
print(t)  # 10
print(type(t))  # <class 'int'>

print("===================================================")

# t = (10,)
t = 10,   # Single valued tuple
print(t)  # (10,)
print(type(t))  # <class 'tuple'>
print("===================================================")

t = "Vivek",   # Single valued tuple
print(t)  # ('Vivek',)
print(type(t))  # <class 'tuple'>

print("===================================================")

# t = (5,12.7,"Welcome",True,'C',10+50j)  # elements in advance
t = 5,12.7,"Welcome",True,'C',10+50j
print(t)  # (5, 12.7, 'Welcome', True, 'C', (10+50j))
print(type(t))  # <class 'tuple'>

print("======================== range() ===========================")

t = range(11)
print(t)  # range(0, 11)
print(type(t))  # <class 'range'>

print("======================== type casting of range with tuple ===========================")

t = tuple(range(11))  # Type Casting of 2 classes (range + tuple)
print(t)  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(type(t))  # <class 'tuple'>

print("===================================================")

s = "Learning Python is very easy"
print(type(s))  # <class 'str'>
print(s.split())  # ['Learning', 'Python', 'is', 'very', 'easy'] - returned a list
print(type(s.split()))  # <class 'list'>

s = "Learning Python is very easy"
t = tuple(s.split())  # Type Casting
print(t)  # ('Learning', 'Python', 'is', 'very', 'easy')
print(type(t))  # <class 'tuple'>

print("================= ACCESSING THE TUPLE ===================")

t = (10,20,30,40,50,60,70,80,90,100)

# 1) By index

print(t[0])  # 10
print(t[-3])  # 80
# print(t[-10])  # IndexError: tuple index out of range

# 2) By slice operator [:]
print(t[1:4])  # (20, 30, 40)
print(t[1:20:2])  # (20, 40, 60, 80, 100)  - Slice operator won't raise IndexError
print(t[::-1])  # (100, 90, 80, 70, 60, 50, 40, 30, 20, 10)  -  In reverse order
print(t[-2:-7:-1])  # (90, 80, 70, 60, 50)  -  In reverse order

# Tuple is Immutable
# t[0] = 777      # TypeError: 'tuple' object does not support item assignment
















