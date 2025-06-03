# Check if a filename starts with a letter (Either lowercase OR uppercase)
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
    print("Valid file name :", matchObj.group())   # Valid file name : R
else:
    print("Invalid file name, it should start with a letter.")








