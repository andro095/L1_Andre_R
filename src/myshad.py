from gl import *
import mynumpy as mn


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

        for x in range(7):
            if 0.15 * (x + 1) <= itt <= 0.15 * (x + 2):
                itt = 0.15 * (x + 1)

        b *= itt
        g *= itt
        r *= itt

        return [r, g, b] if itt > 0 else [0, 0, 0]
