
"""
4. Do from scratch
Shop calculator
"""

total = 0
item_count = int(input("How many items: "))
while item_count < 0:
    print("invalid number of items!")
    item_count = int(input("How many items: "))
for items in range(item_count):
    item = float(input("Enter price of item: "))
    total = total + item
if total > 100:
    total *= 0.9
print(f"Total price for {item_count} items is ${total:.2f}")
