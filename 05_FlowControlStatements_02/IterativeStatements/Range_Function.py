# Range Function - returns range data type
# Every data type belongs to some class

# range(stop)  --->  form 1
# range(start, stop)  --->  form 2 (Mostly used)
# range(start, stop, step)  --->  form 3 (Mostly used)

#    print(list(range(5,10)))
#                    /   \
#                   /     \
#           Inclusive     Exclusive

range(10)  # form 1
print(range(10))  # range(0, 10) # 0 comes by default
print(list(range(10))) # Converting range dataType to list dataType  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(5,10))) # [5, 6, 7, 8, 9]   # By default step is 1
print(list(range(5,10,1))) # [5, 6, 7, 8, 9]   # step of 1
print(list(range(5,10,2))) # [5, 7, 9]  # step of 2 (difference of 2)
print(list(range(1,10,3))) # [1, 4, 7]

print(list(range(10,1,-1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2]
print(list(range(-10,-5))) # [-10, -9, -8, -7, -6]
print(list(range(-5,1)))  # [-5, -4, -3, -2, -1, 0]
print(list(range(10,1,1))) # []
print(list(range(10,15,-1))) # []






















