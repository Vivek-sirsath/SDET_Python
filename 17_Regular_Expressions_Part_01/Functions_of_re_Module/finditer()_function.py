# 5) finditer()
# - Returns match details of --> Matching Objects, start() index, end() index

import re

text = "My contact numbers are 9856425174 and 9475896213"
pattern = r"\d{10}"
numbers = re.finditer(pattern,text)

# print(numbers)   # <callable_iterator object at 0x0000020148E144F0>

for number in numbers:
    print(number.group(), number.start(), number.end())

# 9856425174 23 33
# 9475896213 38 48








