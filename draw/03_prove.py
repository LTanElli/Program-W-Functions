# Import the functions from the Draw 2-D library
# so that they can be used in this program.
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

    # draw_line(canvas, 10, 10, 200, 200, width=10)
    for i in range(0, 200, 10):
        draw_line(canvas, 10, 10, i, 200 - i)

    # x = 100
    # y = 200
    # width = 100

    # draw_line(canvas, x, y, x, y + width)
    # draw_line(canvas, x, y, x + width, y + width)
    # draw_line(canvas, x, y, x, y + width)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_something(canvas, x, y, width):
    
    x = 100
    y = 200
    width = 100

    draw_line(canvas, x, y, x, y + width)
    draw_line(canvas, x, y, x + width, y + width)
    draw_line(canvas, x, y, x, y + width)


# Call the main function so that
# this program will start executing.
main()