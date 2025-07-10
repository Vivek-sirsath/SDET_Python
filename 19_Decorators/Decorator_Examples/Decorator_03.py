print("========= Normal behaviour of a function =========")

def division(a,b):
    print(a/b)

division(10,20)   # 0.5
# division(10,0)   # ZeroDivisionError: division by zero


print("========= Using decorator function '@decorator' =========")


def smart_division(func):   # Decorator function

    # wrapper() is an extra functionality modified to original function
    def wrapper(x,y):   # Instead of x,y we can use a,b
        if y == 0:
            print("Can not divide by zero")
        else:
            func(x,y)
    return wrapper

@smart_division
def division(a,b):
    print(a/b)


division(10,0)   # Can not divide by zero
division(30,50)   # 0.6