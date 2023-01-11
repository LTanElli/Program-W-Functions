import math

items = int(input("Please enter the number of items: "))
items_per_box = int(input("Please enter the number of items per box: "))

number_of_boxes = math.ceil(items/items_per_box)

print()

print(f"for {items} items with {items_per_box} items per box, you will need {number_of_boxes} boxes.")