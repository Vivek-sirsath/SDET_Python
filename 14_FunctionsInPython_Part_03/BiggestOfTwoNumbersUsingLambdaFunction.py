# Find biggest of 2 numbers using Lambda Function

# Normal Function

def findBiggest(a,b):
    if a>b:
        print(a)
    else:
        print(b)


findBiggest(45,20)
findBiggest(20,50)


# Lambda Function

s = lambda a,b: a if a>b else b  # Ternary Operator
print(s(300,20))
print(s(60,120))




























