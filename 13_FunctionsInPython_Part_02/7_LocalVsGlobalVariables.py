# LOCAL VARIABLE vs GLOBAL VARIABLE

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

employee_details()  # Employee: John Legend, Company: Microsoft
company_info()  # Welcome to, Microsoft
company_address()  # Address: Microsoft , Pune















