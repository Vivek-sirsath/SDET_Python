# Slice Operator of String
# Reference - 06_String_Part_01

s = "123456789"

print(s[2:7])  # 34567    # Default step is 1
print(s[1:9])  # 23456789
print(s[1:9:2])  # 2468
print(s[:5])   # 12345
print(s[5:])   # 6789
print(s[::])  # 123456789
print(s[4:100000:1])  # 56789
print(s[100000:5:1])  # Blank_output