"""

LOCAL VARIABLE vs GLOBAL VARIABLE

# TYPES OF VARIABLES:
---------------------------------
1) Global Variable :
   - declared outside of function and accessible within all function in a same module.
   - Global variable can be accessible within all the functions in the same package.
   - Global variables are class/module level variables. But we can make any variable
     as global variable inside a method by using 'global' keyword in front of it.

2) Local Variable :
   declared inside of function and accessible only within that funct ion.

"""

company_name = "Microsoft"  # Global Variable

def employee_details():
    global location   #  We can make any local variable as Global by using 'global' keyword.
    employee_name = "John Legend"  # Local  Variable
    location = "Pune"  # Local variable
    print(f"Employee: {employee_name}, Location: {location}, Company: {company_name}")

def company_info():
    print(f"Welcome to, {company_name}")

def company_address():
    print(f"Address: {company_name} , {location}")  # Here we've made 'location' as global variable.

employee_details()  # Employee: John Legend, Location: Pune, Company: Microsoft
company_info()  # Welcome to, Microsoft
company_address()  # Address: Microsoft , Pune















