def div(i,j):
    print(i/j)

div(10,20)  # 0.5
div(20,10)  # 2.0   # Result changed due to changing the position of arguments.


# Errors may come if we change the number of arguments.

# div(20)   # TypeError: div() missing 1 required positional argument: 'j'

div(20,10,30)   # TypeError: div() takes 2 positional arguments but 3 were given

