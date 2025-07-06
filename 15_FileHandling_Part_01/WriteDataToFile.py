# Write data to file (pqr.txt)

f = open("pqr.txt", "w")

# f.write("Learning\n")
# f.write("Python is\n")
# f.write("very easy\n")

list = ["Hello everyone\n", "Good morning\n", "My name is Vivek\n"]
f.writelines(list)

f.close()

# writelines() method writes the 'list of lines'
# Here, data will be overwritten using writelines() method. First line will be overwritten by list of lines.
# Here 'Learning Python is very easy' these lines are overwritten by 'Hello everyone.....'
# To overcome this problem, we need to open the file in 'Append' mode (a)

# APPEND MODE :

f = open("pqr.txt", "a")
f.write("I am Senior Test Engineer")

f.close()

print("=========== Checking what we've written in file ===========")

f = open("pqr.txt", "r")
lines = f.readlines()

for line in lines:
    print(line)

f.close()

"""
CONSOLE OUTPUT:

Hello everyone
Good morning
My name is Vivek
I am Senior Test Engineer
"""


print("============== If the file is present in another directory ==============")
# Here we need to specify that path along with file name.
# Enclose the path in 'r-string', because copying the path will show error.

# Open the file in append mode
remoteFile = open(r"C:\Users\Admin\PycharmProjects\PythonProject\SDET_Python_Selenium\03_Operators\xyz.txt", "a")
remoteFile.write("This is a remote file of example of File handling.")
remoteFile.close()

# Open the file in reading mode
textFile = open(r"C:\Users\Admin\PycharmProjects\PythonProject\SDET_Python_Selenium\03_Operators\xyz.txt", "r")
lines = textFile.readlines()

for line in lines:
    print(line)

textFile.close()