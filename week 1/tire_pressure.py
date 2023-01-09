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

