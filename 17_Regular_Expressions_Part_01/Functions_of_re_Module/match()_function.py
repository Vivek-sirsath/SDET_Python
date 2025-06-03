# 1) match()

# - Checks if a string starts with a pattern. Returns a match object if found, otherwise None.
# - Matches only start of a string.

print("======== Check if a filename starts with a letter (Either lowercase OR uppercase) ========")
import re

# Case 1

filename = "Report2025.pdf"
pattern = "[a-zA-Z]"
matchObj = re.match(pattern,filename)

if matchObj:
    print("Valid file name :", matchObj.group())   # Valid file name : R
else:
    print("Invalid file name, it should start with a letter.")



# Case 2

filename = "1Report2025.pdf"
pattern = "[a-zA-Z]"
matchObj = re.match(pattern,filename)

if matchObj:
    print("Valid file name :", matchObj.group())
else:
    print("Invalid file name, it should start with a letter.")  # Invalid file name, it should start with a letter.

#              X---------------X---------------X---------------X---------------X

print("============ Check if a username starts with a character ============")

# Case 1

username = "akg4512"
pattern = "[a-zA-Z]"
matchObj = re.match(pattern,username)
print(matchObj.group())  # a



# Case 2

username = "1akg4512"
pattern = "[a-zA-Z]"
matchObj = re.match(pattern,username)
print(matchObj)  # None