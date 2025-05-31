# CONTEXT MANAGER or 'WITH' STATEMENT :

# To close file automatically once perform operation we can go for context manager.

# with statement

with open("abc.txt", "w") as f:
    f.write("File\n")
    f.write("handling\n")
    f.write("session\n")
    print(f.closed)  # False

print(f.closed)  # True

















