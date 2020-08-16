from gl import *
import mynumpy as mn
import random


# Toon shader
def myToon(bcords, tcords, normals, color, texture=None, itt=None):
    if itt is None:
        itt = [0, 0, 1]
    b = color[0] / 255
    g = color[1] / 255
    r = color[2] / 255

    if texture:
        tx = tcords[0][0] * bcords[0] + tcords[1][0] * bcords[1] + tcords[2][0] * bcords[2]
        ty = tcords[0][1] * bcords[0] + tcords[1][1] * bcords[1] + tcords[2][1] * bcords[2]

        tcolor = texture.gColor(tx, ty)

        b *= tcolor[0] / 255
        g *= tcolor[1] / 255
        r *= tcolor[2] / 255

    nx = normals[0][0] * bcords[0] + normals[1][0] * bcords[1] + normals[2][0] * bcords[2]
    ny = normals[0][1] * bcords[0] + normals[1][1] * bcords[1] + normals[2][1] * bcords[2]
    nz = normals[0][2] * bcords[0] + normals[1][2] * bcords[1] + normals[2][2] * bcords[2]

    norm = [nx, ny, nz]
    itt = mn.mdot(norm, itt)

    divisions = 7

    for x in range(divisions):
        if 1 / divisions * (x + 1) <= itt <= 1 / divisions * (x + 2):
            itt = 1 / divisions * (x + 1)

    b *= itt
    g *= itt
    r *= itt

    return [r, g, b] if itt > 0 else [0, 0, 0]

# Toon shader
def myInvert(bcords, tcords, normals, color, texture=None, itt=None):
    if itt is None:
        itt = [0, 0, 1]
    b = color[0] / 255
    g = color[1] / 255
    r = color[2] / 255

    if texture:
        tx = tcords[0][0] * bcords[0] + tcords[1][0] * bcords[1] + tcords[2][0] * bcords[2]
        ty = tcords[0][1] * bcords[0] + tcords[1][1] * bcords[1] + tcords[2][1] * bcords[2]

        tcolor = texture.gColor(tx, ty)

        b *= tcolor[0] / 255
        g *= tcolor[1] / 255
        r *= tcolor[2] / 255

    nx = normals[0][0] * bcords[0] + normals[1][0] * bcords[1] + normals[2][0] * bcords[2]
    ny = normals[0][1] * bcords[0] + normals[1][1] * bcords[1] + normals[2][1] * bcords[2]
    nz = normals[0][2] * bcords[0] + normals[1][2] * bcords[1] + normals[2][2] * bcords[2]

    norm = [nx, ny, nz]
    itt = mn.mdot(norm, itt)

    b *= itt
    g *= itt
    r *= itt

    b = 1 - b
    g = 1 - g
    r = 1 - r

    return [r, g, b] if itt > 0 else [0, 0, 0]


# Gray shader
def myGray(bcords, tcords, normals, color, texture=None, itt=None):
    if itt is None:
        itt = [0, 0, 1]
    b = color[0] / 255
    g = color[1] / 255
    r = color[2] / 255

    if texture:
        tx = tcords[0][0] * bcords[0] + tcords[1][0] * bcords[1] + tcords[2][0] * bcords[2]
        ty = tcords[0][1] * bcords[0] + tcords[1][1] * bcords[1] + tcords[2][1] * bcords[2]

        tcolor = texture.gColor(tx, ty)

        b *= tcolor[0] / 255
        g *= tcolor[1] / 255
        r *= tcolor[2] / 255

    nx = normals[0][0] * bcords[0] + normals[1][0] * bcords[1] + normals[2][0] * bcords[2]
    ny = normals[0][1] * bcords[0] + normals[1][1] * bcords[1] + normals[2][1] * bcords[2]
    nz = normals[0][2] * bcords[0] + normals[1][2] * bcords[1] + normals[2][2] * bcords[2]

    norm = [nx, ny, nz]
    itt = mn.mdot(norm, itt)

    b *= itt
    g *= itt
    r *= itt

    gsc = 0.299 * r + 0.587 * g + 0.114 * b

    return [gsc, gsc, gsc] if itt > 0 else [0, 0, 0]


# static shader
def myStatic(bcords, tcords, normals, color, texture=None):
    nx = normals[0][0] * bcords[0] + normals[1][0] * bcords[1] + normals[2][0] * bcords[2]
    ny = normals[0][1] * bcords[0] + normals[1][1] * bcords[1] + normals[2][1] * bcords[2]
    nz = normals[0][2] * bcords[0] + normals[1][2] * bcords[1] + normals[2][2] * bcords[2]

    itt = [0, 0, 1]
    norm = [nx, ny, nz]
    itt = mn.mdot(norm, itt)

    b = itt * random.randint(0, 255) / 255
    g = itt * random.randint(0, 255) / 255
    r = itt * random.randint(0, 255) / 255

    return [r, g, b] if itt > 0 else [0, 0, 0]


def myRainbow(bcords, tcords, normals, color, texture=None):
    nx = normals[0][0] * bcords[0] + normals[1][0] * bcords[1] + normals[2][0] * bcords[2]
    ny = normals[0][1] * bcords[0] + normals[1][1] * bcords[1] + normals[2][1] * bcords[2]
    nz = normals[0][2] * bcords[0] + normals[1][2] * bcords[1] + normals[2][2] * bcords[2]

    itt = [0, 0, 1]
    norm = [nx, ny, nz]
    itt = mn.mdot(norm, itt)

    divisions = 12
    colors = [
        [26, 19, 52],
        [38, 41, 74],
        [1, 84, 90],
        [1, 115, 81],
        [3, 195, 131],
        [170, 217, 98],
        [251, 191, 69],
        [239, 106, 50],
        [237, 3, 69],
        [161, 42, 94],
        [113, 1, 98],
        [2, 44, 125]
    ]
    r = 1
    g = 1
    b = 1
    for x in range(divisions):
        if 1 / divisions * (x + 1) <= itt <= 1 / divisions * (x + 2):
            itt = 1 / divisions * (x + 1)
            r = colors[x][0] / 255 * itt
            g = colors[x][1] / 255 * itt
            b = colors[x][2] / 255 * itt

    return [r, g, b] if itt > 0 else [0, 0, 0]
