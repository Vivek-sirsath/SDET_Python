d = {10: 'apple', 20: 'banana', 30: 'mango', 40: 'orange'}

print("=============== len() ===================")
print(len(d))  # 4

print("=============== get() ===================")

print(d[40])  # orange
# print(d[150])  # KeyError: 150

print(d.get(40))  # orange
print(d.get(100))  # None - It will not raise 'KeyError'

"""
2nd Way : Specifying default_value as an argument
SYNTAX :
          d.get(Key, Default_Value)
If the key is available, will return resp value.
If the key is not available, will return specified Default_Value.
"""

print(d.get(20,"lemon"))  # banana (Key is available)
print(d.get(80,"lemon"))  # lemon (Key is NOT available)
print(d.get(100,'chocolate'))  # chocolate (Key is NOT available)

print("=============== pop() ===================")
print(d)  # {10: 'apple', 20: 'banana', 30: 'mango', 40: 'orange'}

print(d.pop(20))  # banana
print(d)  # {10: 'apple', 30: 'mango', 40: 'orange'}

print("=============== popitem() ===================")
d = {10: 'apple', 20: 'banana', 30: 'mango', 40: 'orange', 50: 'strawberry'}
print(d)
print(d.popitem())  # If key not specified, it will remove a random (key-value) pair.
# It shows which item is removed.
print(type(d.popitem()))  # <class 'tuple'>
print(d)  # {10: 'apple', 20: 'banana', 30: 'mango'}

print("=============== items() ===================")

d = {10: 'apple', 20: 'banana', 30: 'mango', 40: 'orange'}
keys = d.keys()
print(keys)  # dict_keys([10, 20, 30, 40])
print(type(keys))  # <class 'dict_keys'>

values = d.values()
print(values)  # dict_values(['apple', 'banana', 'mango', 'orange'])
print(type(values))  # <class 'dict_values'>

print(d.items())  # dict_items([(10, 'apple'), (20, 'banana')])  # As Tuple
print(d)  # {10: 'apple', 20: 'banana'}

print("=============== copy() ===================")

# create duplicate independent object of Dictionary.
d = {10: 'apple', 20: 'banana', 30: 'mango', 40: 'orange'}
d1 = d.copy()
print(d1)  # {10: 'apple', 20: 'banana', 30: 'mango', 40: 'orange'}

print("=============== update() ===================")
d.update({50: 'grapes', 60: 'cherry'})
print(d)
































