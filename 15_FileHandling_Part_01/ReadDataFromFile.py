# Read data from file (abc.txt)

f = open("abc.txt", "w")

list = ["Hello everyone\n", "Good morning\n", "My name is Vivek\n", "I am Senior Test Engineer"]
f.writelines(list)

print("======== Read all the lines ========")

f = open("abc.txt", "r")
# print(f.read())   # This will read all the lines from file.

"""
CONSOLE OUTPUT:

Hello everyone
Good morning
My name is Vivek
I am Senior Test Engineer
"""

print("======== Read characters using index ========")


# print(f.read(10))  # Hello ever       # read first 10 characters

# print(f.read(32))  # Output: First 32 characters

# Hello everyone
# Good morning
# My n

print("======== Read single line ========")
# line1 = f.readline()
# print(line1)   # yone
# line2 = f.readline()
# print(line2)   # Good morning

print("======== Read all the lines using for loop ========")

# lines = f.readlines()
#
# for line in lines:
#     print(line)

print("======== Read the lines using slice operator (:) ========")

lines = f.readlines()

# print(lines[-2:])   #  Returns last 2 lines  # ['My name is Vivek\n', 'I am Senior Test Engineer']
print(lines[:2])  #  Returns first 2 lines  # ['Hello everyone\n', 'Good morning\n']

# last_n_lines = lines[-10::-1]

# for line in lines[1:3]:
#     print(line)

# for line in lines[-2:]:
#     print(line)

# for line in lines[:2]:
#     print(line)

# for line in lines[10::-1]:
#     print(line)

"""
CONSOLE OUTPUT:

Good morning

My name is Vivek
"""

f.close()














