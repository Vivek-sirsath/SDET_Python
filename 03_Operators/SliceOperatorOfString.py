# Slice Operator of String
# Reference - 06_String_Part_01

#   print(s[ 1:9 ])
#           /   \
#          /     \
#  Exclusive     Inclusive


s = "123456789"

print(s[2:7])  # 34567    # Default step is 1
print(s[1:9])  # 23456789
print(s[1:9:2])  # 2468  # step is 2
print(s[1:6:2])  # 246

print("---------------------------------------------")

print(s[0:9:2])   # 13579
print(s[:5])   # 12345
print(s[5:])   # 6789

print("---------------------------------------------")

print(s[::])  # 123456789
print(s[4:100000:1])  # 56789
print(s[100000:5:1])  # Blank_output