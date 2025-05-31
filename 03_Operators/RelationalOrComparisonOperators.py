a = 5
b = 2

print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)

print("===========================================")

# Chaining of relational operators is also possible.
# True --> if all comparisons are true.
# False --> if at least one comparison is false.

print(10<20<30<40>50)  # False
print(10==20==30==40!=50)  # False

print("===========================================")

print(10<20<30<40<50)  # True

