#---------------------------------------------------------
# CALLING THE FUNCTION WITHOUT '@decor'
#---------------------------------------------------------

print("========= Example of beauty parlour without '@decor' function =========")

def makeup(func):
    def inner(customer):
        if customer == "Neha":
            print("Hey",customer,"you are looking beautiful after make-up!")
        else:
            func(customer)
    return inner          # Inner function is also called wrapper function


def parlour(customer):
    print("Hey",customer,"you are looking normal!")


# Decorator function internally works as below
afterMakeup = makeup(parlour)

afterMakeup("Jessi")   # Hey Jessi you are looking normal!
afterMakeup("Neha")   # Hey Neha you are looking beautiful after make-up!

#===============================================================================================================

#---------------------------------------------------------
# CALLING THE FUNCTION WITH '@decor'
#---------------------------------------------------------

print("========= Using @decor function =========")

# Here makeup is the decorator function
def makeup(func):
    def inner(customer):
        if customer == "Neha":
            print("Hey",customer,"you are looking beautiful after make-up!")
        else:
            func(customer)
    return inner          # Inner function is also called wrapper function

@makeup
def parlour(customer):
    print("Hey",customer,"you are looking normal!")


parlour("Pooja")   # Hey Pooja you are looking normal!
parlour("Neha")    # Hey Neha you are looking beautiful after make-up!