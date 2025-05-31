cart = [10,20,600,60,70]

for item in cart:
    if item>500:
        print("To place this order, insurance must be required")
        break
    print(item)