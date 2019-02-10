from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x0 > x1:
        store = x1
        x1 = x0
        x0 = store
        store = y1
        y1 = y0
        y0 = store

    # print("x0: {}".format(x0))
    # print("y0: {}".format(y0))
    # print("x1: {}".format(x1))
    # print("y1: {}".format(y1))

    A = y1 - y0
    B = -1 * (x1 - x0)

    if B == 0:
        if y0 > y1:
            while y0 > y1:
                plot(screen, color, x0, y0)
                y0 -= 1
        else:
            while y0 < y1:
                plot(screen, color, x0, y0)
                y0 += 1
    elif A == 0:
        while x0 < x1:
            plot(screen, color, x0, y0)
            x0 += 1

    else:
        slope = float(A) / (-1 * B)
        if slope > 0:
            if slope <= 1:

                d = A + A + B

                x = x0
                y = y0

                # print("1st octant")
                
                # print(A)
                # print(B)

                while x <= x1:
                    # print(d)
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

                d = B - A - A

                x = x0
                y = y0


                while x <= x1:
                    # print(d)
                    plot(screen, color, x, y)
                    if d > 0:
                        y += -1
                        d += 2 * B
                    x += 1
                    d += -2 * A
            else:
                d = A - B - B

                x = x0
                y = y0

                # print("----------")
                #
                # print(A)
                # print(B)

                while y >= y1:
                    # print(d)
                    plot(screen, color, x, y)
                    if d>0:
                        x += 1
                        d += 2 * A
                    y += -1
                    d += -2 * B
