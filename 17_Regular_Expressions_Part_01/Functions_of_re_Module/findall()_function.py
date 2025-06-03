# 4) findall()

# - Finds all matches of a pattern in a string. Returns a list of matches, or an empty list if none are found.
# - Returns the list of matching objects. If not matches, returns empty list [].

import re

# EXTRACT THE EMAILS FROM THE STRING

# Case 1 (Valid emails)

text = "My name is KPR and my email addresses are kpr1234@gmail.com and kpr12$@gmail.com"
pattern = "[a-z0-9._$%]+@[a-z]{5}.[a-z]{3}"
emails = re.findall(pattern,text)
print(emails)   # ['kpr1234@gmail.com', 'kpr12$@gmail.com']



# Case 2 (Invalid emails)

text = "My name is KPR and my email addresses are kpr13wt!@gmail.com and kpr12$@3mail.com"
pattern = "[a-z0-9._$%]+@[a-z]{5}.[a-z]{3}"
emails = re.findall(pattern,text)
print(emails)   # [] - empty list


#              X---------------X---------------X---------------X---------------X


# EXTRACT THE DATES FROM THE STRING

# Case 1 (Valid Dates)

text = "The exam will start from 12/11/2025 and will ends on 03/12/2025"
pattern = r"\d{2}/\d{2}/\d{4}"
dates = re.findall(pattern,text)
print(dates)   # ['12/11/2025', '03/12/2025']



# Case 2 (Invalid Dates)

text = "The exam will start from 12/11/202 and will ends on 03/1/2025"
pattern = r"\d{2}/\d{2}/\d{4}"
dates = re.findall(pattern,text)
print(dates)   # [] - empty list

