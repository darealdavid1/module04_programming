# week5_lab.py
## Author: David Leatherman
# Busniness domaain: Tech bro buy new tech yo

product_name = "Laptop"  # str
status = "Pending"  # str
quanity = 3  # int
unit_price = 450.00  # float
is_over_limit = unit_price * quanity > 1000  # bool

print(
    type(product_name),
    type(status),
    type(unit_price),
    type(quanity),
    type(is_over_limit),
)

# Step 4

subtotal = unit_price * quanity
tax = subtotal * 0.07
total = subtotal + tax
requires_approval = total > 1000

# Step 5

print("== Purchase Request Summary ==")
print(f"Product Name: {product_name}")
print(f"Qty: {quanity}")
print(f"subtotal: ${subtotal:.2f}")
print(f"tax: ${tax:.2f}")
print(f"total: ${total:.2f}")
print(f"requires_approval: {requires_approval}")

# Step 6

user_qty = int(input("Enter the quantity you want to purchase: "))  # convert str to int
new_total = unit_price * user_qty * 1.07
print(f"New total for {user_qty} units: ${new_total:.2f}")
print(f"requires_approval: {new_total > 1000}")
