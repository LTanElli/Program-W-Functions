<<<<<<< HEAD
"""python tire_volume.py
Enter the width of the tire in mm (ex 205): 185
Enter the aspect ratio of the tire (ex 60): 50
Enter the diameter of the wheel in inches (ex 15): 14

The approximate volume is 24.09 liters

> python tire_volume.py
Enter the width of the tire in mm (ex 205): 205
Enter the aspect ratio of the tire (ex 60): 60
Enter the diameter of the wheel in inches (ex 15): 15

The approximate volume is 39.92 liters

v = 
π w2 a (w a + 2,540)d
10,000,000,000"""


import math
from datetime import datetime


with open("volume.txt", mode="wt") as volumes:

    current_date = datetime.now()

    print(f"{current_date:%Y-%m-%d-%A}")

    print("Formula for the Volume of a Tire")
    print()
    print()

    width = float(input("Enter the width (W) of the tire in mm: "))
    print()

    aspect_ratio = float(input("Enter the aspect ratio (a) of the tire: "))
    print()

    diameter = float(input("Enter the diameter (d) of the wheel in inches: "))
    print()

    volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
    print(f"{volume:.2f} liters/tire")

    # print(f"The approximate volume is {volume:.2f} liters.")

    print(f"{current_date:%Y-%m-%d-%A}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file = volumes)

    tire_purchase = input("Would you like to purchase this tire? ")

    if tire_purchase.lower() == "yes":
        print("Please enter your cell phone number.")
        print()
        phone = input(">>> ")
        print()
        print(f"Customer phone number: {phone}", file = volumes)
        print("Have a nice day.")
    elif tire_purchase.lower() == "no":
        print("We will contact you with more information. Have a nice day.")

    
#an attempt to do prices is below

# with open("volume.txt", mode="rt") as volumes:

#     current_date = datetime.now()

#     print(f"{current_date:%Y-%m-%d-%A}")
#     print()

#     purchase_price = input("Would you like to purchase this tire? ")
#     print()

# #Randome cost of tires at 24 liters and 39 liters were used for price examples. simple above or below option added from the average of those two numbers for simply two possible options.
#     # while purchase_price == "yes" or "no":
#     if purchase_price == "yes":

#         if volume >= 31.5:
#             print("Alright, your total is $200.00 per tire")
#             quit()
#         else:
#             print("Alright, your total is $95.00 per tire.")
#             quit()

#     elif purchase_price == "no":
#         print("Alright, have a nice day.")

=======
import math
import datetime

print("Formula for the Volume of a Tire")
print()
print()

width = float(input("Enter the width (W) of the tire in mm: "))
print()

aspect_ratio = float(input("Enter the aspect ratio (a) of the tire: "))
print()

diameter = float(input("Enter the diameter (d) of the wheel in inches: "))
print()

volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
print()

print(f"The approximate volume is {volume:.2f} liters.")

dt = datetime.now()
# day = dt.weekday()
print(f"{dt:%Y-%B-%d, %A}")

open(volume.txt, mode = "rt")
>>>>>>> 2a2f4d7bbe6e29d286de6db47288087036c939d5
