'''
Create a new CSV file sales.csv with columns:
Product,Quantity,Price
Take input from the user for 5 products
Write them into the file using csv.writer
Then open it again and print the total sales (Quantity × Price)
'''
import csv
try:
    with open('sales.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Product', 'Quantity', 'Price'])
except Exception as e:
    print(e)

user_inp = []
for i in range(5):
    product = input("Enter the product: ")
    quantity = int(input("Enter the quantity: "))
    price = int(input("Enter the price of the product: "))
    user_inp.append([product, quantity, price])

# write to file:
try:
    with open('sales.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(user_inp)
except Exception as e:
    print(e)

# read sales.
try:
    with open('sales.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)
except Exception as e:
    print(e)

# print the total sales (Quantity × Price)
total_sales = 0
try:
    with open('sales.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                total_sales += int(row[1]) * int(row[2])
            except ValueError:
                print("Not a number")

except Exception as e:
    print(e)

print(total_sales)