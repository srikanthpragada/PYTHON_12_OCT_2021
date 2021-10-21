# Calculate net amount based on qty and price

qty = int(input("Enter Quantity :"))
price = int(input("Enter price :"))

amount = qty * price

# calculate 10% discount
discount = amount * 10 / 100
netamount = amount - discount

print(f"Amount        : {amount:10.2f}")
print(f"- Discount    : {discount:10.2f}")
print(f"                 ----------")
print(f"Net amount    : {netamount:10.2f}")

