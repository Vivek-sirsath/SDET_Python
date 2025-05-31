print("================= OPERATORS : OPERATIONS ON THE TUPLE ===================")

# 1) Concatenation Operator (+)
t1 = (10,20,30)
t2 = (40,50,60)
print("Tuple Concatenation")
print(t1 + t2)  # (10, 20, 30, 40, 50, 60)

# 2) Repetition Operator / Multiplication (*)
print("Repetition Operator")
print(t1*3)  # (10, 20, 30, 10, 20, 30, 10, 20, 30)

# 3) Membership Operator (in, not in)
print(40 in t2)  # True
print(80 in t1)  # False
print('k' in t1)  # False
print(50 not in t1)  # True