# CONTEXT MANAGER or 'WITH' STATEMENT :

# Purpose of the context manager is to close file automatically once perform operation we can go for context manager.
# Because sometimes we forget to close the file.

# with statement
# f = open("abc.txt", "w") , is same as, below declaration where 'as f' is an alias.

with open("abc.txt", "w") as f:
    f.write("File\n")
    f.write("handling\n")
    f.write("in\n")
    f.write("Python")

print(f.closed)  # True

print("=========== READ THE DATA FROM THE FILE ===========")

# READ THE DATA FROM THE FILE.
with open("abc.txt","r") as f:
    print(f.read())

















