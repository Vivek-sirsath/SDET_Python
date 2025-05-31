"""
Functions on Tuple :
 As tuple is immutable
 These functions are NOT APPLICABLE on Tuple
  --> append()
      insert()
      remove()
      pop()
      extend()

APPLICABLE FUNCTIONS on Tuple
  --> len()
      count()
      index()
      sorted()
      min()
      max()

"""

tuple_1 = (10,20,30,20,50,40,20,60,70)
print(len(tuple_1))  # 9
print(tuple_1.count(20))  # 3
print(tuple_1.index(40))  # 5
print(tuple_1.index(20))  # 1 - First occurrence
# print(tuple_1.index(100))  # ValueError: tuple.index(x): x not in tuple
print(sorted(tuple_1))  # [10, 20, 20, 20, 30, 40, 50, 60, 70]
print(sorted(tuple_1,reverse=True))  # [70, 60, 50, 40, 30, 20, 20, 20, 10]
print(max(tuple_1))  # 70
print(min(tuple_1))  # 10






















