# WORKING WITH DIRECTORIES / FOLDERS
import os

with open("pqrs.txt","w") as f:
    f.write("Good Morning...\n" * 15)

print(os.getcwd())   # returns current working directory.
# C:\Users\Admin\PycharmProjects\PythonProject\SDET_Python_Selenium\16_FileHandling_Part_02\Working_With_Directories

print(os.path.dirname(os.getcwd()))   # returns the parent of current working directory.
# C:\Users\Admin\PycharmProjects\PythonProject\SDET_Python_Selenium\16_FileHandling_Part_02

# Create a subdirectory inside current directory. Named 'Child_Directory'
# os.mkdir("Child_Directory")  # Create a subdirectory

# Create multiple directories.
# os.makedirs("Child1/Child2/Child3")   # Create nested directories (Child1 > Child2 > Child3)

# Remove single directory
# os.rmdir("Child1/Child2/Child3")   # Child3 - directory removed

# Remove multiple directories.
# os.removedirs("Child1/Child2")  # child2 and Child3 - directories removed

"""
# To join one or more path. OR  to append a file to the path.
- The os.path.join() method is a function in the os module that joins one or more path components intelligently.
- It constructs a full path by concatenating various components while automatically inserting the appropriate 
  path separator (/ for Unix-based systems and \ for Windows).
  
- For more info about 'os.path.join()' method -
  https://www.geeksforgeeks.org/python-os-path-join-method/  
  
- 

"""
path = os.getcwd()
filepath = os.path.join(path,"pqrs.txt")
print(filepath)
# C:\Users\Admin\PycharmProjects\PythonProject\SDET_Python_Selenium\16_FileHandling_Part_02\Working_With_Directories\pqrs.txt

# Remove a file from the directory.
os.remove(filepath)   # 'pqrs.txt' file removed from directory


# Rename the name of directory
# os.rename("Child_Directory","Renamed_Directory")

print("============================ Contents of child working directory ===============================")
# Get the content from the current child directory
# listdir(path) - Returns content of directory as list but not the contents of subdirectory.
print(os.listdir(os.getcwd()))  # ['Renamed_Directory', 'WorkingWithDirectories.py']


"""
# How to change the Current Working Directory to the specific path or  specific directory ?

os.chdir() method :-

- os.chdir() method in Python is used to change the current working directory to the specified path. 
  This function is part of the os module, which provides functionalities to interact with the operating system.
  
"""

# Change the current working directory to another directory.
print(os.getcwd())
# C:\Users\Admin\PycharmProjects\PythonProject\SDET_Python_Selenium\16_FileHandling_Part_02\Working_With_Directories

# Change directory to '16_FileHandling_Part_02'. Which is parent directory.
os.chdir(os.path.dirname(os.getcwd()))
# print(os.getcwd())  # Now changed to new directory.

print("============================ Contents of parent working directory ===============================")
# Get the content from the parent directory
print(os.listdir(os.getcwd()))

print(r"======================= Contents of parent working directory using dot (.) ========================")
# Also dot (".") means current working dir
# "." is same as [os.getcwd()]
print(os.listdir("."))   # Returns content of directory as list but not the contents of subdirectory.

print("==================================== walk() function ============================================")

# walk() function :-
# - It returns the contents of directories and subdirectories also.

for root,dirs,files in os.walk("."):
    print("Roots:",root,"Dirs:",dirs,"Files:",files)

