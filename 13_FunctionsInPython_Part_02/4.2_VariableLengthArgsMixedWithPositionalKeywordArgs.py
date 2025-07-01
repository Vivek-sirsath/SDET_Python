def sum(n1,*n):
    print(n)

sum(10)  # ()
sum(100)  # ()
sum(10,20)  # (20,)
sum(10,20,30,40,50)  # (20, 30, 40, 50)


print("===================== IF USE POSITIONAL ARGUMENT AFTER VARIABLE LENGTH ARGUMENT =======================")


def sum(*n,n1):
    print(n)

# sum(10,20,30)  # TypeError: sum() missing 1 required keyword-only argument: 'n1'
# It will take all the values as 'Variable Length Argument'

# WILL SHOW ERROR :
# TypeError: sum() missing 1 required keyword-only argument: 'n1'

print("===================== TO RESOLVE THE ERROR, USE KEYWORD 'n1' WITH POSITIONAL ARGUMENTS =======================")

def sum(*n,n1):
    print(n)

sum(10,20, n1=30)  # (10,20)





