import struct as st


def glColor(r, g, b):
    return bytes([int(255 * b), int(255 * g), int(255 * r)])


# Clase para el modelado de objetos
class Mobj(object):

    def __init__(self, fname):
        with open(fname, 'r') as file:
            self.lines = file.read().splitlines()
        self.vertex = []
        self.norms = []
        self.tcords = []
        self.faces = []
        self.load()

    def load(self):
        opt = [['v', self.vertex], ['vn', self.norms], ['vt', self.tcords]]
        for l in self.lines:
            if l:
                try:
                    key, v = l.split(' ', 1)
                    v = v.rstrip()
                    v = v.lstrip()
                    for op in opt:
                        if key == op[0]:
                            op[1].append(list(map(float, v.split(' '))))
                    if key == 'f':
                        self.faces.append([list(map(int, vt.split('/'))) for vt in v.split(' ')])
                except:
                    continue


# Clase para leer las texturas
class TextureReader(object):
    def __init__(self, filename):
        self.framebuffer = []
        self.reader(filename)

    def reader(self, filename):
        texture = open(filename, 'rb')
        texture.seek(10)
        tamah = st.unpack('=l', texture.read(4))[0]
        texture.seek(18)
        self.w = st.unpack('=l', texture.read(4))[0]
        self.h = st.unpack('=l', texture.read(4))[0]
        texture.seek(tamah)

        for x in range(self.h):
            colorarr = []
            for y in range(self.w):
                b = ord(texture.read(1)) / 255
                g = ord(texture.read(1)) / 255
                r = ord(texture.read(1)) / 255
                colorarr.append(glColor(r, g, b))
            self.framebuffer.append(colorarr)

        texture.close()

    # Función que devuelve el color
    def gColor(self, vx, vy):
            return self.framebuffer[int(self.h * vy)][int(self.w * vx)] if 0 <= vx <= 1 and 0 <= vy <= 1 else glColor(0, 0, 0)
