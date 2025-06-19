# Web Scrapping :-
import re

import requests

print("========== Extracting the Pin-Codes from the web page ===========")

response = requests.get("https://www.redbus.in/info/contactus")
pin_code_pattern = r"[a-zA-Z]+ - [0-9]+"
pins = re.findall(pin_code_pattern, response.text)
print(pins)

"""
CONSOLE OUTPUT
--------------

['rem - 2', 'Karnataka - 560008', 'Karnataka - 560017', 'Nadu - 641015', 'Gujarat - 380009',
 'Hyderabad - 500081', 'Nadu - 600032', 'Rajasthan - 302021', 'Delhi - 110030', 'Phase - 8']
"""

#              X---------------X---------------X---------------X---------------X

print("========== Extracting the Emails from the web page ===========")
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.]+\.[a-zA-Z]+"
emails = re.findall(email_pattern, response.text)
print(emails)

# ['press@redbus.com']

#              X---------------X---------------X---------------X---------------X

print("========== Extracting the City Names from the web page ===========")
name_Pattern = r"[A-Z]{4,12}"
names = re.findall(name_Pattern,response.text)
print(names)

"""
['DOCTYPE', 'UTCS', 'HOME', 'SEARCH', 'SEARCH', 'JSON', 'URIC', 'BANGALORE', 'BANGALORE', 'COIMBATORE', 'AHMEDABAD',
 'INDORE', 'HYDERABAD', 'KOLKATA', 'CHENNAI', 'JAIPUR', 'MUMBAI', 'PUNE', 'NECO', 'DELHI', 'CHANDIGARH', 
 'TCFTX', 'TCFTX', 'CONTEXTUAL', 'LOGIN', 'ENABLED', 'RDCH', 'SECURE', 'COOKIE', 'UZAAAAAAJP', 'PROD', 
 'DIRECT', 'JSON', 'XMLH', 'JSON', 'POST', 'XMLH', 'URIC', 'URIC', 'UTCS', 'CDATA', 'DOMC']

"""

#              X---------------X---------------X---------------X---------------X

print("========== Extracting the Link's URLs from the web page ===========")
link_pattern = r"https?://[a-zA-Z0-9./-]+"
links = re.findall(link_pattern,response.text)

# Print no of links on web page
print("No of links on Web Page:-",len(links))

# Print each link
for link in links:
    print(link)

