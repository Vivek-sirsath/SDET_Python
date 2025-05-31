# Print 1 to 10 numbers using for loop

for x in range(1,11):
    print(x)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

print("================== even numbers 2 to 20 ========================")

# print even numbers 2 to 20 by interval of 2

for x in range(2,21,2):
    print(x)
print("================== Descending order 20 to 10 ========================")

for x in range(20,9,-1):
    print(x)

print("==================== odd numbers 1 to 19 ======================")
# print odd numbers 1 to 19 by interval of 2

for x in range(1,21,2) :
    print(x)

print("==================== Nested for loop ======================")

print("Nested for loop")

for x in range(1,6):
    for y in range(1,6):
        print(f"{x} x {y} = {x*y}", end ="\t")
    print()







