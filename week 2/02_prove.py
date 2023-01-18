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
