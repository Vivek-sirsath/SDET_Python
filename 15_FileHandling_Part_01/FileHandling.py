# FILE HANDLING IN PYTHON

f = open("abc.txt","w")
print(f.name)  # abc.txt
print(f.mode)   # w
print(f.readable())  # False
print(f.writable())  # True
print(f.closed)  # False

f.close()

print(f.closed)  # True


















