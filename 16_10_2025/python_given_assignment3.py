# online shopping system
# 1. Create a dictionary of items with prices (e.g., "Laptop": 55000, "Mouse": 700, ...).
items = {
    'laptop': 55000,
    'mouse': 700,
    'keyboard':500,
    'pen':10,
    'bottle':200,
    'mobile':40000
}
cart = {}
continuing = True
while continuing:
    item = input(f"Enter the item to purchase. Options are: \n{items.keys()}: ").lower()
    quantity = int(input("Enter the quantity: "))
    while quantity < 0:
        quantity = int(input("Please give valid quantity: Quantity must be > 0: "))
    cart[item] = [quantity, quantity*items[item]]
    cont = input("To continue shopping enter y/Y else n/N: ").lower()
    if cont == 'n':
        continuing = False

total_amount = 0
for key,value in cart.items():
    total_amount += cart[key][1]
print(total_amount)

discount = total_amount * 0.15 if total_amount > 50000 else total_amount * 0.10 if total_amount > 25000 else 0
final_bill = (total_amount - discount) + (1 + 0.05) # add 5% gst

print("---------- BILL ----------")
# Display the bill.
for key, value in cart.items():
    print(f'{key} : {cart[key][0]} * {items[key]} => {cart[key][1]}')
print("---------------------------------")
print(f"Total Before Discount: {total_amount}")
print(f'Discount: ', end=' ')
print("15%") if total_amount > 50000 else print("10%") if total_amount > 25000 else print("No Discount")
print("GST: 5%")
print(f"Final Amount: {final_bill}")
print("--------------------------------------")
print("Thank you for shopping!")


