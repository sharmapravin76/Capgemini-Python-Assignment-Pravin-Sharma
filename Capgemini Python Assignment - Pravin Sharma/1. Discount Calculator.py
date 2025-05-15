bill_amount = float(input("Enter total bill amount: "))
if bill_amount > 1000:
    discount = 0.2 * bill_amount
elif bill_amount > 500:
    discount = 0.1 * bill_amount
else:
    discount = 0
final_amount = bill_amount - discount
print("Discount applied: ₹", round(discount, 2))
print("Final amount after discount: ₹", final_amount)
