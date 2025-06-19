import re

# (caret) ^ and (dollar) $ symbols in regular expressions :

# - Checks the position of pattern in a string.
# - Checking means matching.

# ^ --> match the start of the string.
# $ --> Match the end of the string.


email1 = "srenggind@hotmail.com"
email2 = "vivek.sirsath007@gmail.com"

pattern1 = "^srenggind@hotmail.com$"
pattern2 = "gmail.com$"


emailObj1 = re.match(pattern1,email1)
print(emailObj1.group())  # srenggind@hotmail.com
print(re.match(pattern1,email2))    # None
print(bool(re.match(pattern1,email1)))   # True
print(bool(re.match(pattern1,email2)))   # False

email2Obj = re.search(pattern2,email2)
print(email2Obj.group())   # gmail.com
print(bool(re.search(pattern2,email2)))   # True


print("========== Validating the exact match of the string (either at start or at end) ===========")

pattern = "^Python$"

print(bool(re.fullmatch(pattern,"Python3")))  # False
print(re.fullmatch(pattern,"Python").group())  # Python
print(bool(re.fullmatch(pattern,"Python Programming")))  # False


