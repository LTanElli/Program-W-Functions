import math

can_volumes = []
can_surface_areas = []
radii = []
heights = []

radius = float(input("Enter the radius of the can in inches: "))
height = float(input("Enter the height of the can in inches: "))

radii.append(radius)
heights.append(height)


def volume(radius, height):
    #volume = π radius2 height
    # radius = float(input("Enter the radius of the can: "))
    # height = float(input("Enter the height of the can: "))
    
    can_volume = math.pi * radius * radius * height
    can_volumes.append(can_volume)
    print(f"Volume: {can_volume:.2f}")
    return can_volume


def surface_area(radius, height):
    #surface_area = 2π radius (radius + height)
    # radius = float(input("enter the radius of the can: "))
    # height = float(input("Enter the height of the can: "))

    can_surface_area = 2 * math.pi * radius * (radius + height)
    can_surface_areas.append(can_surface_area)
    print(f"Surface Area: {can_surface_area:.2f}")
    return can_surface_area


def main(radius, height):
    storage_efficiency = volume(radius, height) / surface_area(radius, height)
    print(f"Storage Efficiency: {storage_efficiency:.2f}")
    

main(radius, height)