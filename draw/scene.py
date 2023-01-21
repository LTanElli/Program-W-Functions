"""
The scene must be outdoor and include part of the sky.

The sky must have clouds.

The scene must include repetitive objects, such as blades of grass, trees, leaves on a tree, birds, flowers, insects, fish, pickets in a fence, dashed lines on a road, buildings, bales of hay, snowmen, snowflakes, or icicles.

"""

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
import random
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
     # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_night_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.



# Call the main function so that
# this program will start executing.

def draw_night_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 4, scene_width, scene_height, width=0, fill="gray3")

    half_height = round(scene_height / 1)
    min_diam = 10
    max_diam = 25

    for i in range(28):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="lightYellow3")
    
def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0, scene_width, scene_height / 4, width=0, fill="tan4")

    half_height = round(scene_height / 5)
    min_diam = 8
    max_diam = 18

    for i in range(15):
        x = random.randint(0, scene_width - max_diam)
        y = random.randint(0, half_height)
        diameter = random.randint(min_diam, max_diam)
        draw_oval(canvas, x, y, x + diameter, y + diameter, fill="saddleBrown")

#for the final part id like to add the moon and a cactus
# def draw_cactus(canvas, center_x, bottom, height):
#     cactus_width = height / 3
#     cactus_height = height / 7
#     left = center_x - c
    

main()