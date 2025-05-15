inventory_items = ['pen', 'pencil', 'eraser']
item_input = input("Enter product name: ")
if item_input in inventory_items:
    print("Product available")
else:
    print("Product not available")