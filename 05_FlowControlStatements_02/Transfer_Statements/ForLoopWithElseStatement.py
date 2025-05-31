cart = [10,20,6,60,70]

for item in cart:
    if item>500:
        print("To place this order, insurance must be required")
        break
    print(item)
else:
    print("Congrats... all items are selected")

# else block executed.