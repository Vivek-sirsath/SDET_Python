print("================= Aliasing =================")
# Aliasing :
#   Process of giving another reference variable to the existing list.
#
#   Drawback:- If we try to change the elements using another reference variable
#   then the changes will also be done in original variable too.

# Aliasing
x = [10,20,30,40]
print("Original list before Aliasing -", x)
y = x
y[1] = 777
print(y)  # [10, 777, 30, 40]
print(x, "- Original list changed")  # [10, 777, 30, 40]
# Here, changes are also reflected in original variable too.

print("================= Cloning =================")
# Cloning :
#   The process of creating exactly duplicate independent objects is called cloning.
#   We can implement cloning by using 'slice operator [:]' OR by using 'copy()' function
# Changes will not be happened in original variable.

# Cloning
x = [10,20,30,40]
print("Original list before Cloning -", x)
# y = x[:]  # Using slice operator
y = x.copy()  # Using copy() function
y[1] = 99
print(y)  # [10, 99, 30, 40]
print(x, "- Original list not changed")  # [10, 20, 30, 40]








