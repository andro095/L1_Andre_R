import struct as st
import mynumpy as mn
import models as md
from numpy import sin, cos, deg2rad


# Reserva de espacio de memoria de 1 byte para un char
def glChar(ch):
    return st.pack('=c', ch.encode('ascii'))


# Reserva de espacio de memoria de 2 bytes para un word
def glWord(wd):
    return st.pack('=h', wd)


# Reserva de espacio de memoria de 4 bytes para un dword
def glDword(dwd):
    return st.pack('=l', dwd)


# Retorna el color deseado por el usuario
def glColor(r, g, b):
    return bytes([int(255 * b), int(255 * g), int(255 * r)])


def NDCtoWC(size, stp, num):
    return int(((num + 1) * (size / 2)) + stp)


# Clase para todas las operaciones relacionadas con el escritor de imágenes
class ImageCreator(object):
    # Constructor del objeto
    def __init__(self, w, h, bgColor, vColor):
        self.glCreateWindow(w, h, bgColor)
        self.vColor = vColor
        self.shaderfunc = None

    def setShaderFunc(self, func):
        self.shaderfunc = func

    # Creador del framebuffer
    def glCreateWindow(self, w, h, bg):
        self.width = w
        self.height = h
        self.bgcolor = bg
        self.glClear()
        self.glViewPort(w - 1, h - 1, 0, 0)

    # Creador del viewport
    def glViewPort(self, w=0, h=0, x=0, y=0):
        # Validamos el área del viewport
        if x + w > self.width or y + h > self.height: return False
        self.VPwidth = self.width - x if w == 0 else w
        self.VPheight = self.height - y if h == 0 else h
        self.VPXstart = x
        self.VPYstart = y
        return True

    # Aclarar el background con su color
    def glClear(self):
        self.framebuffer = [[self.bgcolor for x in range(self.width)] for y in range(self.height)]
        self.dbf = [[-float('inf') for x in range(self.width)] for y in range(self.height)]

    # Cambiar el bgcolor
    def glClearColor(self, r, g, b):
        self.bgcolor = glColor(r, g, b)

    # Cambiar vColor
    def glVertexColor(self, r, g, b):
        self.vColor = glColor(r, g, b)

    # Función para dibujar un punto
    def glVertex(self, x, y, scolor=None):
        if x > 1 or x < -1 or y > 1 or y < -1: return False
        xWc = NDCtoWC(self.VPwidth, self.VPXstart, x)
        yWc = NDCtoWC(self.VPheight, self.VPYstart, y)
        self.glVertexWC(xWc, yWc, scolor)
        return True

    def glVertexWC(self, x, y, scolor=None):
        if scolor is None:
            scolor = self.vColor
        try:
            self.framebuffer[y][x] = scolor
        except:
            pass

    def glVertexTPWC(self, x, y):
        try:
            self.tempframebuffer[y][x] = self.vColor
        except:
            pass

    def glLineWC(self, xi, yi, xf, yf):
        x = abs(xf - xi)
        y = abs(yf - yi)

        comp = y > x

        if y > x:
            temp = xi
            xi = yi
            yi = temp
            temp = xf
            xf = yf
            yf = temp

        if xi > xf:
            temp = xi
            xi = xf
            xf = temp
            temp = yi
            yi = yf
            yf = temp

        x = abs(xf - xi)
        y = abs(yf - yi)

        ac = 0
        top = 0.5
        try:
            p = y / x
        except ZeroDivisionError:
            pass
        else:
            yinc = yi
            for xc in range(xi, xf + 1):
                if comp:
                    self.glVertexWC(yinc, xc)
                else:
                    self.glVertexWC(xc, yinc)
                ac = ac + p
                if ac >= top:
                    yinc = yinc - 1 if yi > yf else yinc + 1
                    top = top + 1

    def glLineTPWC(self, xi, yi, xf, yf):
        x = abs(xf - xi)
        y = abs(yf - yi)

        comp = y > x

        if y > x:
            temp = xi
            xi = yi
            yi = temp
            temp = xf
            xf = yf
            yf = temp

        if xi > xf:
            temp = xi
            xi = xf
            xf = temp
            temp = yi
            yi = yf
            yf = temp

        x = abs(xf - xi)
        y = abs(yf - yi)

        ac = 0
        top = 0.5
        try:
            p = y / x
        except ZeroDivisionError:
            pass
        else:
            yinc = yi
            for xc in range(xi, xf + 1):
                if comp:
                    self.glVertexTPWC(yinc, xc)
                else:
                    self.glVertexTPWC(xc, yinc)
                ac = ac + p
                if ac >= top:
                    yinc = yinc - 1 if yi > yf else yinc + 1
                    top = top + 1

    def glLine(self, xi, yi, xf, yf):
        if xi > 1 or yi > 1 or xf > 1 or yf > 1 or xi < -1 or yi < -1 or xf < -1 or yf < -1:
            return False

        xi = NDCtoWC(self.VPwidth, self.VPXstart, xi)
        xf = NDCtoWC(self.VPwidth, self.VPXstart, xf)
        yi = NDCtoWC(self.VPheight, self.VPYstart, yi)
        yf = NDCtoWC(self.VPheight, self.VPYstart, yf)

        self.glLineWC(xi, yi, xf, yf)

        return True

    # Creamos un poligono
    def glPolygon(self, polcords):
        # Variables para cachar el x y y mínimo y máximo
        xmin, ymin, xmax, ymax = polcords[0][0], polcords[0][1], polcords[0][0], polcords[0][1]
        # Dibujamos el contorno del polygono
        for index in range(len(polcords)):
            # Averiguamos La coordenadas mínima y máxima x y y
            xmin = polcords[index][0] if xmin > polcords[index][0] else xmin
            xmax = polcords[index][0] if xmax < polcords[index][0] else xmax
            ymin = polcords[index][1] if ymin > polcords[index][1] else ymin
            ymax = polcords[index][1] if ymax < polcords[index][1] else ymax

        polcordsmodified = []

        for x in range(len(polcords)):
            polcordsmodified.append([polcords[x][0] - xmin, polcords[x][1] - ymin])

        self.tempframebuffer = [[self.bgcolor for x in range(xmax - xmin + 1)] for y in range(ymax - ymin + 1)]

        for index in range(len(polcordsmodified)):
            xi = polcordsmodified[index][0]
            xf = polcordsmodified[(index + 1) % len(polcordsmodified)][0]
            yi = polcordsmodified[index][1]
            yf = polcordsmodified[(index + 1) % len(polcordsmodified)][1]

            self.glLineTPWC(xi, yi, xf, yf)

        height = len(self.tempframebuffer)
        width = len(self.tempframebuffer[0])

        for y in range(height):
            for x in range(width):
                if self.tempframebuffer[y][x] != self.vColor:
                    toppoint = False
                    bottompoint = False
                    leftpoint = False
                    rightpoint = False
                    count = y
                    if count != height - 1:
                        while count < height - 1 and not toppoint:
                            if self.tempframebuffer[count + 1][x] == self.vColor:
                                toppoint = True
                            else:
                                count += 1

                    count = y
                    if count != 0:
                        while count > 0 and not bottompoint:
                            if self.tempframebuffer[count - 1][x] == self.vColor:
                                bottompoint = True
                            else:
                                count -= 1

                    count = x
                    if count != width - 1:
                        while count < width - 1 and not rightpoint:
                            if self.tempframebuffer[y][count + 1] == self.vColor:
                                rightpoint = True
                            else:
                                count += 1

                    count = x
                    if count != 0:
                        while count > 0 and not leftpoint:
                            if self.tempframebuffer[y][count - 1] == self.vColor:
                                leftpoint = True
                            else:
                                count -= 1

                    if toppoint and bottompoint and rightpoint and leftpoint:
                        self.glVertexTPWC(x, y)

        for y in range(height):
            for x in range(width):
                if self.tempframebuffer[y][x] == self.vColor:
                    self.framebuffer[y + ymin][x + xmin] = self.tempframebuffer[y][x]

    # Crearemos la matrix del modelo
    def glMMatrix(self, trns, scl, rot):
        tMatrix = [[1, 0, 0, trns[0]],
                   [0, 1, 0, trns[1]],
                   [0, 0, 1, trns[2]],
                   [0, 0, 0, 1]]

        sMatrix = [[scl[0], 0, 0, 0],
                   [0, scl[1], 0, 0],
                   [0, 0, scl[2], 0],
                   [0, 0, 0, 1]]

        rMatrix = self.glRMatrix(rot)

        return mn.mmul(mn.mmul(tMatrix, rMatrix), sMatrix)

    # Crearemos la matrix de rotación
    def glRMatrix(self, rot):
        rtx = deg2rad(rot[0])
        rty = deg2rad(rot[1])
        rtz = deg2rad(rot[2])

        mRtx = [[1, 0, 0, 0],
                [0, cos(rtx), -sin(rtx), 0],
                [0, sin(rtx), cos(rtx), 0],
                [0, 0, 0, 1]]

        mRty = [[cos(rty), 0, sin(rty), 0],
                [0, 1, 0, 0],
                [-sin(rty), 0, cos(rty), 0],
                [0, 0, 0, 1]]

        mRtz = [[cos(rtz), -sin(rtz), 0, 0],
                [sin(rtz), cos(rtz), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]]

        return mn.mmul(mn.mmul(mRtx, mRty), mRtz)

    # Cargamos el modelo A dibujar
    def glModel(self, namefile, xSt, ySt, zSt, xSc, ySc, zSc, xRt, yRt, zRt, texture=None, isWire=False):
        mymodel = md.Mobj(namefile)

        mMatrix = self.glMMatrix([xSt, ySt, zSt], [xSc, ySc, zSc], [xRt, yRt, zRt])

        rMatrix = self.glRMatrix([xRt, yRt, zRt])

        print(mMatrix)

        print(rMatrix)

        exit(1)

        for elem in mymodel.faces:
            vCount = len(elem)
            if isWire:
                for x in range(vCount):
                    vi = mymodel.vertex[elem[x][0] - 1]
                    vf = mymodel.vertex[elem[(x + 1) % vCount][0] - 1]
                    xi = round((vi[0] * xSc) + xSt)
                    yi = round((vi[1] * ySc) + ySt)
                    xf = round((vf[0] * xSc) + xSt)
                    yf = round((vf[1] * ySc) + ySt)
                    self.glLineWC(xi, yi, xf, yf)
            else:
                a = mymodel.vertex[elem[0][0] - 1]
                b = mymodel.vertex[elem[1][0] - 1]
                c = mymodel.vertex[elem[2][0] - 1]

                a = [round(a[0] * xSc + xSt), round(a[1] * ySc + ySt), round(a[2] * zSc + zSt)]
                b = [round(b[0] * xSc + xSt), round(b[1] * ySc + ySt), round(b[2] * zSc + zSt)]
                c = [round(c[0] * xSc + xSt), round(c[1] * ySc + ySt), round(c[2] * zSc + zSt)]

                if vCount > 3:
                    d = mymodel.vertex[elem[3][0] - 1]
                    d = (round(d[0] * xSc + xSt), round(d[1] * ySc + ySt), round(d[2] * zSc + zSt))
                    dp = [mymodel.tcords[elem[3][1] - 1][0], mymodel.tcords[elem[3][1] - 1][1]] if texture else [0, 0]
                    dp2 = mymodel.norms[elem[3][2] - 1]

                ap = [mymodel.tcords[elem[0][1] - 1][0], mymodel.tcords[elem[0][1] - 1][1]] if texture else [0, 0]
                bp = [mymodel.tcords[elem[1][1] - 1][0], mymodel.tcords[elem[1][1] - 1][1]] if texture else [0, 0]
                cp = [mymodel.tcords[elem[2][1] - 1][0], mymodel.tcords[elem[2][1] - 1][1]] if texture else [0, 0]

                ap2 = mymodel.norms[elem[0][2] - 1]
                bp2 = mymodel.norms[elem[1][2] - 1]
                cp2 = mymodel.norms[elem[2][2] - 1]

                self.glTriangle(a, b, c, t=texture, tcords=(ap, bp, cp), norms=(ap2, bp2, cp2))
                if vCount > 3:
                    self.glTriangle(a, c, d, t=texture, tcords=(ap, cp, dp), norms=(ap2, cp2, dp2))

    # Calcular coordenadas baricentricas
    def glBcCords(self, point, v1, v2, v3):
        bcarr = []
        try:
            bcarr.append((((v2[1] - v3[1]) * (point[0] - v3[0])) + ((v3[0] - v2[0]) * (point[1] - v3[1]))) /
                         (((v2[1] - v3[1]) * (v1[0] - v3[0])) + ((v3[0] - v2[0]) * (v1[1] - v3[1]))))

            bcarr.append((((v3[1] - v1[1]) * (point[0] - v3[0])) + ((v1[0] - v3[0]) * (point[1] - v3[1]))) /
                         (((v2[1] - v3[1]) * (v1[0] - v3[0])) + ((v3[0] - v2[0]) * (v1[1] - v3[1]))))

            bcarr.append(1 - bcarr[0] - bcarr[1])
        except:
            for x in range(3):
                bcarr.append(-1)
        return bcarr

    def glTriangle(self, v1, v2, v3, color=None, t=None, tcords=(), norms=()):
        if color is None:
            color = glColor(1, 1, 1)

        xmin = min(v1[0], v2[0], v3[0])
        ymin = min(v1[1], v2[1], v3[1])
        xmax = max(v1[0], v2[0], v3[0])
        ymax = max(v1[1], v2[1], v3[1])

        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                if y < 0 or y >= self.height or x < 0 or x >= self.width:
                    continue
                bcarr = self.glBcCords((x, y), v1, v2, v3)

                if bcarr[0] >= 0 and bcarr[1] >= 0 and bcarr[2] >= 0:
                    dp = v1[2] * bcarr[0] + v2[2] * bcarr[1] + v3[2] * bcarr[2]
                    if dp > self.dbf[y][x]:
                        _color = self.shaderfunc(bcarr, tcords, norms, color, texture=t)

                        self.dbf[y][x] = dp
                        self.glVertexWC(x, y, glColor(_color[0], _color[1], _color[2]))

    # Función para hacer la image
    def glFinish(self, filename):
        file = open(filename, 'wb')

        file.write(bytes('B'.encode('ascii')))
        file.write(bytes('M'.encode('ascii')))

        file.write(glDword(14 + 40 + self.width * self.height * 3))
        file.write(glDword(0))
        file.write(glDword(14 + 40))

        file.write(glDword(40))
        file.write(glDword(self.width))
        file.write(glDword(self.height))
        file.write(glWord(1))
        file.write(glWord(24))
        file.write(glDword(0))
        file.write(glDword(self.width * self.height * 3))
        file.write(glDword(0))
        file.write(glDword(0))
        file.write(glDword(0))
        file.write(glDword(0))

        for x in range(self.height):
            for y in range(self.width):
                file.write(self.framebuffer[x][y])

        file.close()
