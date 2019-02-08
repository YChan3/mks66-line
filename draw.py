from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    pass
    A = y1 - y0
    B = -1 * (x1 - x0)

    slope = float(A) / (-1 * B)
    print(slope)

    if slope > 0:
        if slope <= 1:

            d = A + A + B

            x = x0
            y = y0

            while x <= x1:
                plot(screen, color, x, y)
                if d>0:
                    y += 1
                    d += 2 * B
                x += 1
                d += 2 * A
        else:
            d = A + B + B

            x = x0
            y = y0

            while y <= y1:
                plot(screen, color, x, y)
                if d<0:
                    x += 1
                    d += 2 * A
                y += 1
                d += 2 * B
    else:
        if (-1 * slope) <= 1:

            d = A + A + B

            x = x0
            y = y0

            while x <= x1:
                print(d)
                plot(screen, color, x, y)
                if d>0:
                    y += -1
                    d += -2 * B
                x += 1
                d += 2 * A
