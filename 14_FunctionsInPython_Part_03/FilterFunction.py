# filter()

l = [5,10,15,20,25,30]

# Normal for loop
for x in l:
    if x%2==0:
        print(x)  # 10 20 30
    else:
        pass


# Using filter function

def isEven(l):
    if l%2==0:
        return True
    else:
        return False

print(list(filter(isEven,l)))  # [10, 20, 30]

print("=================== Using Lambda Function ====================")

# Filter function with Lambda Function.

print(list(filter(lambda x:x%2==0,l)))  # [10, 20, 30]
print(list(filter(lambda x:x%2!=0,l)))  # [5, 15, 25]


print("=================== Filter Salary Using Lambda Function ====================")

# Filter employees with salary > 50000
employees = [{'name':'Leonardo','salary':40000},{'name':'Stacy','salary':80000},{'name':'Larry','salary':60000}]
print(list(filter(lambda emp:emp['salary']>50000, employees)))  # Example of Data Mining




