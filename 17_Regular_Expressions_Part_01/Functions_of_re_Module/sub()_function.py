# 6) sub()
# - Replaces all the occurrences of a pattern in a string or text and returns a new text.
# - Censoring a bad word in an application or chats.
# - Masking the credit card numbers.

import re

text = "You are a bitch"
pattern = "bitch"

clean_text = re.sub(pattern, "*****",text)
print(clean_text)   # You are a *****



# Formatting a phone number to a standard format - (XXX) XXX-XXXX
text = "Call me on 9845621473 or 8746921126"
pattern = r"(\d{3})(\d{3})(\d{4})"
formatted_numbers = re.sub(pattern,r"(\1) (\2)-(\3)", text)
print(formatted_numbers)

# Call me on (984) (562)-(1473) or (874) (692)-(1126)


# Masking the Credit Card numbers
text = "My credit card numbers are 9876-5432-1010-4567 and 1234-9876-4567-8910"
pattern = r"\d{4}-\d{4}-\d{4}-\d{4}"
masked_numbers = re.sub(pattern,r"****-****-****-****", text)
print(masked_numbers)
