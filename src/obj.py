# Carga un archivo OBJ

import struct


def color(r, g, b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])


class Obj(object):
    def __init__(self, filename):
        with open(filename, 'r') as file:
            self.lines = file.read().splitlines()

        self.vertex = []
        self.normals = []
        self.texcoords = []
        self.faces = []

        self.read()

    def read(self):
        for line in self.lines:
            if line:
                prefix, value = line.split(' ', 1)

                if prefix == 'v':  # vertices
                    self.vertex.append(list(map(float, value.split(' '))))
                elif prefix == 'vn':
                    self.normals.append(list(map(float, value.split(' '))))
                elif prefix == 'vt':
                    self.texcoords.append(list(map(float, value.split(' '))))
                elif prefix == 'f':
                    self.faces.append([list(map(int, vert.split('/'))) for vert in value.split(' ')])


class Texture(object):
    def __init__(self, path):
        self.pixels = []
        self.read(path)

    def read(self, path):
        image = open(path, 'rb')
        image.seek(10)
        headerSize = struct.unpack('=l', image.read(4))[0]

        image.seek(18)
        self.width = struct.unpack('=l', image.read(4))[0]
        self.height = struct.unpack('=l', image.read(4))[0]
        image.seek(headerSize)

        for y in range(self.height):
            colorarr = []
            for x in range(self.width):
                b = ord(image.read(1)) / 255
                g = ord(image.read(1)) / 255
                r = ord(image.read(1)) / 255
                colorarr.append(color(r, g, b))
            self.pixels.append(colorarr)

        image.close()

    def getColor(self, tx, ty):
        if 0 <= tx <= 1 and 0 <= ty <= 1:
            y = int(self.height * ty)
            x = int(self.width * tx)

            return self.pixels[y][x]
        else:
            return color(0, 0, 0)
