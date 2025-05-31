day = input("Enter day of the week - ")

if day == "Saturday" or day == "Sunday":
    print(day, "-", "50 % discount on all items...")
elif day == "Monday" :
    print(day, "-", "30 % discount on all items...")
elif day == "Wednesday" :
    print(day, "-", "20 % discount on all items...")
elif day == "Friday" :
    print (day, "-", "10 % discount on all items...")
else :
    print(day, "-", "No Discount")

