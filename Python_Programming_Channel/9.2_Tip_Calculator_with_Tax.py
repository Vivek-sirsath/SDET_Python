def calculate_total(bill, tip_percent=10, tax_percent=5):
    tip = bill * (tip_percent / 100)
    tax = bill * (tax_percent / 100)
    return bill + tip + tax

amount = float(input("Enter bill amount: "))
total_amount = calculate_total(amount, tip_percent=15)
print(f"Total Amount to Pay: ₹{total_amount:.2f}")