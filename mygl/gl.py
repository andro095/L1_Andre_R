import struct as st


# Reserva de espacio de memoria de 1 byte para un char
def glChar(ch):
    return st.pack('=c', ch.encode('ascii'))


# Reserva de espacio de memoria de 2 bytes para un word
def glWord(wd):
    return st.pack('=h', wd)


# Reserva de espacio de memoria de 4 bytes para un dword
def glDword(dwd):
    return st.pack('=h', dwd)


# Retorna el color deseado por el usuario
def glColor(r, g, b):
    return bytes([int(255 * b), int(255 * g), int(255 * r)])


WHITE = glColor(1, 1, 1)


# Clase para todas las operaciones relacionadas con el escritor de imágenes
class ImageCreator(object):
    # Constructor del objeto
    def __init__(self, w, h, initColor):
        self.glCreateWindow(self, w, h, bg=initColor)

    # Creador del framebuffer
    def glCreateWindow(self, w, h, bg=glColor(0, 0, 0)):
        self.width = w
        self.height = h
        self.bg = bg
        self.framebuffer = [[self.bg for x in range(self.width)] for y in range(self.height)]

    # def glViewPort(self, x=0, y=0, width=self.width-1):
