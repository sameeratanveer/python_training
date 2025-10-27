customer_name = "   alice williams   "
address = "  42, green street, london  "
phone = " +44 7900 123456 "

# Ordered Items
items = ["burger", "fries", "coke"]
quantities = (2, 1, 3)  # matching order
prices = (5.50, 2.25, 1.00)  # per item in dollars

# q1: Clean up customer_name, address, and phone using string methods.
customer_name = customer_name.strip().capitalize()
address = address.strip().title()
phone = phone.strip()


# 2. Prepare Order Summary

# 3. Create a new list items_upper with all item names in uppercase.
items_upper = []
items_upper.append(items[0].upper())
items_upper.extend(list([items[1].upper(), items[2].upper()]))


# 4. Calculate the total cost for each item using the quantity and price (indexing only).
total_cost = quantities[0] * prices[0] + quantities[1] * prices[1] + quantities[2] * prices[2]

# 5. Store the individual totals in a list totals.
totals = [quantities[0] * prices[0], quantities[1] * prices[1], quantities[2] * prices[2]]
print(totals)

# print order receipt:
print('*****')
print(f'Order Summary for {customer_name}\nDelivery Address: {address}\nContact: {phone}')
print()
print(f'Items Ordered:')
print(f'-{items_upper[0]} x {quantities[0]} = ${totals[0]:.2f}')
print(f'-{items_upper[1]} x {quantities[1]} = ${totals[1]:.2f}')
print(f'-{items_upper[2]} x {quantities[2]} = ${totals[2]:.2f}')

print()
print('Total Bill: ${}'.format(total_cost))
print('*****')

