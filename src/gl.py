import struct as st


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


# Clase para el modelado de objetos
class Mobj(object):

    def __init__(self, fname):
        self.lines = open(fname, 'r').read().splitlines()
        self.vertex = []
        self.norms = []
        self.tcords = []
        self.faces = []
        self.load()

    def load(self):
        opt = [['v', self.vertex], ['vn', self.norms], ['vt', self.tcords]]
        for l in self.lines:
            if l:
                key, v = l.split(' ', 1)

                for op in opt:
                    if key == op[0]:
                        op[1].append(list(map(float, v.split(' '))))
                if key == 'f':
                    self.faces.append([list(map(int, vt.split('/'))) for vt in v.split(' ')])


# Clase para todas las operaciones relacionadas con el escritor de imágenes
class ImageCreator(object):
    # Constructor del objeto
    def __init__(self, w, h, bgColor, vColor):
        self.glCreateWindow(w, h, bgColor)
        self.vColor = vColor

    # Creador del framebuffer
    def glCreateWindow(self, w, h, bg):
        self.width = w
        self.height = h
        self.bgcolor = bg
        self.glClear()
        self.glViewPort(w, h, 0, 0)

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

    # Cambiar el bgcolor
    def glClearColor(self, r, g, b):
        self.bgcolor = glColor(r, g, b)

    # Cambiar vColor
    def glVertexColor(self, r, g, b):
        self.vColor = glColor(r, g, b)

    # Función para dibujar un punto
    def glVertex(self, x, y):
        if x > 1 or x < -1 or y > 1 or y < -1: return False
        try:
            self.framebuffer[NDCtoWC(self.VPheight, self.VPYstart, y)][
            NDCtoWC(self.VPwidth, self.VPXstart, x)] = self.vColor
        except:
            pass
        return True

    def glVertexWC(self, x, y):
        try:
            self.framebuffer[y][x] = self.vColor
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

    def glLine(self, xi, yi, xf, yf):
        if xi > 1 or yi > 1 or xf > 1 or yf > 1 or xi < -1 or yi < -1 or xf < -1 or yf < -1:
            return False

        xi = NDCtoWC(self.VPwidth, self.VPXstart, xi)
        xf = NDCtoWC(self.VPwidth, self.VPXstart, xf)
        yi = NDCtoWC(self.VPheight, self.VPYstart, yi)
        yf = NDCtoWC(self.VPheight, self.VPYstart, yf)

        x = abs(xf - xi)
        y = abs(yf - yi)

        comp = y > x

        print(comp)

        if y > x:
            temp = xi
            xi = yi
            yi = temp
            temp = xf
            xf = yf
            yf = temp

        print(xi)
        print(xf)
        print(yi)
        print(yf)

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
        yinc = yi

        for xc in range(xi, xf + 1):
            if comp:
                self.glVertexWC(yinc, xc)
            else:
                self.glVertexWC(xc, yinc)
            ac = ac + y / x
            if ac >= top:
                yinc = yinc - 1 if yi > yf else yinc + 1
                top = top + 1

        return True

    # Cargamos el modelo A dibujar
    def glModel(self, namefile, xSt, ySt, xSc, ySc):
        mymodel = Mobj(namefile)
        for elem in mymodel.faces:
            vCount = len(elem)
            for x in range(vCount):
                vi = mymodel.vertex[elem[x][0] - 1]
                vf = mymodel.vertex[elem[(x + 1) % vCount][0] - 1]
                xi = round((vi[0] * xSc) + xSt)
                yi = round((vi[1] * ySc) + ySt)
                xf = round((vf[0] * xSc) + xSt)
                yf = round((vf[1] * ySc) + ySt)
                self.glLineWC(xi, yi, xf, yf)

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