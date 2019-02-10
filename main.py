from display import *
from draw import *
import random
import math

screen = new_screen()
color = [ 255, 0, 0 ]
val = 0.0
cycle = 0

INCREMENT = 255/333.33

# draw_line(250, 250, 500, 350, screen, color)
# draw_line(250, 250, 350, 500, screen, color)
# draw_line(250, 250, 500, 150, screen, color)
# draw_line(250, 250, 350, 0, screen, color)
# draw_line(250, 250, 150, 500, screen, [ 255, 0, 0 ])
# draw_line(250, 250, 0, 350, screen, [ 255, 0, 0 ])
# draw_line(250, 250, 0, 150, screen, [ 255, 0, 0 ])
# draw_line(250, 250, 150, 0, screen, [ 255, 0, 0 ])

# draw_line(250, 250, 0, 250, screen, [ 255, 0, 0 ])
# draw_line(250, 250, 250, 500, screen, [ 255, 0, 0 ])
# draw_line(250, 250, 500, 250, screen, [ 255, 0, 0 ])
# draw_line(250, 250, 250, 0, screen, [ 255, 0, 0 ])

# draw_line(250, 250, 500, 249, screen, [ 255, 0, 0 ])

# draw_line(250, 250, 249, 0, screen, [ 255, 0, 0 ])

# draw_line(250, 250, 499, 0, screen, [ 255, 0, 0 ])
# draw_line(250, 250, 500, 0, screen, [ 255, 0, 0 ])
# draw_line(250, 250, 500, 1, screen, [ 255, 0, 0 ])
# draw_line(250, 250, 498, 0, screen, [ 255, 0, 0 ])

# draw_line(250, 250, 500, 500, screen, [ 255, 255, 0 ])


def color_change(color):
    global cycle
    global val
    if cycle == 0:
        val += INCREMENT
        color[2] = math.floor(val)
        if color[2] == 255:
            cycle += 1
            val = 255.0
    elif cycle == 1:
        val -= INCREMENT
        color[0] = math.ceil(val)
        if color[0] == 0:
            cycle += 1
            val = 0.0
    elif cycle == 2:
        val += INCREMENT
        color[1] = math.ceil(val)
        if color[1] == 255:
            cycle += 1
            val = 255.0
    elif cycle == 3:
        val -= INCREMENT
        color[2] = math.ceil(val)
        if color[2] == 0:
            cycle += 1
            val = 0.0
    elif cycle == 4:
        val += INCREMENT
        color[0] = math.ceil(val)
        if color[0] == 255:
            cycle += 1
            val = 255.0
    elif cycle == 5:
        val -= INCREMENT
        color[1] = math.ceil(val)

# ex = 0
# ey = 500
#
# while ex <= 500:
#     draw_line(500, 0, ex, ey, screen, color)
#     ex += 1
#     color_change(color)
#
# ex = 500
# while ey >= 0:
#     draw_line(500, 0, ex, ey, screen, color)
#     ey += -1
#     color_change(color)
#
# ey = 0
# while ex >= 0:
#     draw_line(500, 0, ex, ey, screen, color)
#     ex += -1
#     color_change(color)
#
# ex = 0
# while ey <= 500:
#     draw_line(500, 0, ex, ey, screen, color)
#     ey += 1
#     color_change(color)

ex = 0
ey = 500

while ex <= 500:
    draw_line(100, 100, ex, ey, screen, color)
    ex += 1
    color_change(color)

ex = 500
while ey >= 0:
    draw_line(100, 100, ex, ey, screen, color)
    ey += -1
    color_change(color)

ey = 0
while ex >= 0:
    draw_line(100, 100, ex, ey, screen, color)
    ex += -1
    color_change(color)

ex = 0
while ey <= 500:
    draw_line(100, 100, ex, ey, screen, color)
    ey += 1
    color_change(color)

display(screen)
save_extension(screen, 'img.png')
