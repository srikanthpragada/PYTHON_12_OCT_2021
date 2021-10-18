# Calculate net amount based on qty and price

qty = int(input("Enter Quantity :"))
price = int(input("Enter price :"))

amount = qty * price

# calculate 10% discount
discount = amount * 10 / 100
netamount = amount - discount

print('Net amount = ', netamount)
