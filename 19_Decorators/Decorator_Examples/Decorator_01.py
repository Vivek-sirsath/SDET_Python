print("========= Normal behaviour of a function =========")

def praise(name):
    print("Hey",name,"you are so clever!")

praise("Deepika")   # Hey Deepika you are so clever!
praise("Vivek")   # Hey Vivek you are so clever!


#---------------------------------------------------------
# CALLING THE ORIGINAL FUNCTION WITHOUT '@decor'
#---------------------------------------------------------
print("========= Decorator function with original function =========")

def decor(func):
    # Wrapper function / modified function
    def inner(name):
        if name == "Pooja":
            print("Hello",name,"good evening!")
        else:
            func(name)
    return inner        # Inner function is also called wrapper function

# Original function
def greet(name):
    print("Hello",name,"good morning!")


# Decorator function internally works as below
decoratorFunction = decor(greet)

decoratorFunction("Alisha")   # Hello Alisha good morning!
decoratorFunction("Pooja")    # Hello Pooja good evening!

#===============================================================================================================

#---------------------------------------------------------
# CALLING THE ORIGINAL FUNCTION WITH '@decor'
#---------------------------------------------------------
print("========= Using @decor function =========")

# Here decor is the decorator function
def decor(func):
    def inner(name):
        if name == "Pooja":
            print("Hello",name,"good evening!")
        else:
            func(name)
    return inner        # Inner function is also called wrapper function

@decor
def greet(name):
    print("Hello",name,"good morning!")


greet("Tanya")   # Hello Tanya good morning!
greet("Pooja")   # Hello Pooja good evening!
