print("========================= FUNCTIONS OF SET ================================")

print("=============== add() ===================")
s = {10,20,30}
s.add(40)
print(s)  # {40, 10, 20, 30}

print("=============== len() ===================")
print(len(s))  # 4

print("=============== update() ===================")
s.update([50,60,70],["Vivek",13.8,False])
print(s)  # {False, 'Vivek', 70, 40, 10, 13.8, 50, 20, 60, 30}

print("=============== copy() ===================")
print("Original :-",s)  # {False, 70, 40, 'Vivek', 10, 13.8, 50, 20, 60, 30}
s1 = s.copy()
print("Duplicate :-",s1)  # {False, 70, 40, 'Vivek', 10, 13.8, 50, 20, 60, 30}
s.add(500)
print("Modified Original :-",s)   # {False, 70, 40, 'Vivek', 10, 13.8, 50, 20, 500, 60, 30}
print("Duplicate :-",s1)  # {False, 70, 40, 'Vivek', 10, 13.8, 50, 20, 60, 30}

print("=============== pop() ===================")
# It removes and return some random elements from the set.
print(s.pop())  # False
print(s)  # {70, 40, 10, 13.8, 50, 20, 500, 'Vivek', 60, 30}

print("=============== remove() ===================")
s.remove(50)
print(s)  # {70, 40, 10, 13.8, 20, 500, 'Vivek', 60, 30}
# s.remove(120)
# print(s)  # KeyError: 120

print("=============== discard() ===================")
s.discard(300)
print(s)  # Will not raise KeyError - {70, 40, 10, 13.8, 20, 500, 'Vivek', 60, 30}
s.discard(40)
print(s)  # {70, 10, 13.8, 20, 500, 'Vivek', 60, 30}

print("=============== clear() ===================")
s.clear()
print(s)  # set() # Empty Set










































