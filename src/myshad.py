from gl import *
import mynumpy as mn
import random


# Toon shader
def myToon(verts, bcords, tcords, normals, color, texture=None, itt=None, normMap=None):
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
def myInvert(verts, bcords, tcords, normals, color, texture=None, itt=None, normMap=None):
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
def myGray(verts, bcords, tcords, normals, color, texture=None, itt=None, normMap=None):
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
def myStatic(verts, bcords, tcords, normals, color, texture=None, itt=None, normMap=None):
    nx = normals[0][0] * bcords[0] + normals[1][0] * bcords[1] + normals[2][0] * bcords[2]
    ny = normals[0][1] * bcords[0] + normals[1][1] * bcords[1] + normals[2][1] * bcords[2]
    nz = normals[0][2] * bcords[0] + normals[1][2] * bcords[1] + normals[2][2] * bcords[2]

    norm = [nx, ny, nz]
    itt = mn.mdot(norm, itt)

    b = itt * random.randint(0, 255) / 255
    g = itt * random.randint(0, 255) / 255
    r = itt * random.randint(0, 255) / 255

    return [r, g, b] if itt > 0 else [0, 0, 0]


# Normal mapping
def myNormal(verts, bcords, tcords, normals, color, texture=None, itt=None, normMap=None):
    b = color[0] / 255
    g = color[1] / 255
    r = color[2] / 255

    tx = tcords[0][0] * bcords[0] + tcords[1][0] * bcords[1] + tcords[2][0] * bcords[2]
    ty = tcords[0][1] * bcords[0] + tcords[1][1] * bcords[1] + tcords[2][1] * bcords[2]

    if texture:
        tcolor = texture.gColor(tx, ty)

        b *= tcolor[0] / 255
        g *= tcolor[1] / 255
        r *= tcolor[2] / 255

    nx = normals[0][0] * bcords[0] + normals[1][0] * bcords[1] + normals[2][0] * bcords[2]
    ny = normals[0][1] * bcords[0] + normals[1][1] * bcords[1] + normals[2][1] * bcords[2]
    nz = normals[0][2] * bcords[0] + normals[1][2] * bcords[1] + normals[2][2] * bcords[2]

    itt = [[itt[0]], [itt[1]], [itt[2]]]
    norm = [nx, ny, nz]
    if normMap:
        tNormal = normMap.gColor(tx, ty)
        tNormal = [
            (tNormal[2] / 255) * 2 - 1,
            (tNormal[1] / 255) * 2 - 1,
            (tNormal[0] / 255) * 2 - 1
        ]
        tNormaldiv = [tNormal[x] / mn.mnorm(tNormal) for x in range(len(tNormal))]

        sb1 = mn.msubstract(verts[1], verts[0])
        sb2 = mn.msubstract(verts[2], verts[0])
        d1 = mn.msubstract(tcords[1], tcords[0])
        d2 = mn.msubstract(tcords[2], tcords[0])
        tn = [0, 0, 0]
        tn[0] = ((d2[1] * sb1[0]) - (d1[1] * sb2[0])) / ((d1[0] * d2[1]) - (d2[0] * d1[1]))
        tn[1] = ((d2[1] * sb1[1]) - (d1[1] * sb2[1])) / ((d1[0] * d2[1]) - (d2[0] * d1[1]))
        tn[2] = ((d2[1] * sb1[2]) - (d1[1] * sb2[2])) / ((d1[0] * d2[1]) - (d2[0] * d1[1]))

        tndiv = [tn[x] / mn.mnorm(tn) for x in range(len(tn))]
        tnsus = mn.msubstract(tndiv, mn.mmul(mn.mdot(tndiv, norm), norm))
        tndiv = [tnsus[x] / mn.mnorm(tnsus) for x in range(len(tnsus))]

        bitn = mn.mcross(norm, tndiv)
        bitndiv = [bitn[x] / mn.mnorm(bitn) for x in range(len(bitn))]

        tMatrix = [[tndiv[0], bitndiv[0], norm[0]],
                   [tndiv[1], bitndiv[1], norm[1]],
                   [tndiv[2], bitndiv[2], norm[2]]]

        tk = mn.mmul(tMatrix, itt)
        tk = [tk[0][0], tk[1][0], tk[2][0]]
        tkdiv = [tk[x] / mn.mnorm(tk) for x in range(len(tk))]
        itt = mn.mdot(tNormaldiv, tkdiv)
    else:
        itt = mn.mdot(norm, itt)

    b *= itt
    g *= itt
    r *= itt

    if itt > 0:
        return r, g, b
    else:
        return 0, 0, 0


# Rainbow shader
def myRainbow(verts, bcords, tcords, normals, color, texture=None, itt=None, normMap=None):
    nx = normals[0][0] * bcords[0] + normals[1][0] * bcords[1] + normals[2][0] * bcords[2]
    ny = normals[0][1] * bcords[0] + normals[1][1] * bcords[1] + normals[2][1] * bcords[2]
    nz = normals[0][2] * bcords[0] + normals[1][2] * bcords[1] + normals[2][2] * bcords[2]

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
