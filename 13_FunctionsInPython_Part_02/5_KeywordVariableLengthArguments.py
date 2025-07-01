# KEYWORD VARIABLE LENGTH ARGUMENTS :
#   - Use (**kwargs) for Keyword Variable-Length Arguments.
#   - Data stored in Dictionary {} in Key-Value pairs.

def display(**kwargs):
    for k,v in kwargs.items():
        print(k,'=',v)
    print(kwargs)

display(a=10,b=20,c=30)
display(a=100,b=200,c=300)


"""
CONSOLE OUTPUT:

a = 10
b = 20
c = 30
{'a': 10, 'b': 20, 'c': 30}
a = 100
b = 200
c = 300
{'a': 100, 'b': 200, 'c': 300}
"""

print("==================================================================")

def create_user_profile(name,age,**additional_info):
    profile = {
        "Name" : name,
        "Age" : age
    }

    profile.update(additional_info) # ADD ADDITIONAL INFO (location, profession, hobbies) TO THE PROFILE (Dictionary)
    # profile.update(additional_info)  # If commented, only 'name', 'age' will be displayed
    print("User Profile:",profile)

create_user_profile("Vivek","35",location="India",profession="Tester",hobbies="Reading")
create_user_profile("Deepika","29",role="Senior Associate Consultant")


"""
CONSOLE OUTPUT:

User Profile: {'Name': 'Vivek', 'Age': '35', 'location': 'India', 'profession': 'Tester', 'hobbies': 'Reading'}
User Profile: {'Name': 'Deepika', 'Age': '29', 'role': 'Senior Associate Consultant'}

If,
    # profile.update(additional_info)  is commented then output will be,
    User Profile: {'Name': 'Vivek', 'Age': '35'}
    User Profile: {'Name': 'Deepika', 'Age': '29'}
    
"""










