from gl import glColor, ImageCreator, Mobj
menu = "Menú:\n   1. Crear una nueva imagen\n   2. Definir un ViewPort\n   3. Borrar todo punto realizado (Clear())\n" \
       "   4. Cambiar el color del clear\n   5. Dibujar un punto\n   6. Cambiar el color de dibujado\n   7. Imprimir " \
       "la imagen\n   8. Realizar una linea\n   9. Dibujar un modelo obj\n   10. Salir del programa\nIngrese una " \
       "opción: "

oplimit = 10

def create_image():
    try:
        print("Dimensiones: ")
        w = int(input("   Ingrese el ancho de su imagen: "))
        h = int(input("   Ingrese el alto de su imagen: "))
        print("Colores: ")
        print("Ingrese el color de fondo en formato rgb")
        r = int(input("r: ")) / 255
        g = int(input("g: ")) / 255
        b = int(input("b: ")) / 255
        bgColor = glColor(r, g, b)
        print("Ingrese el color de dibujado en formato rgb")
        r = int(input("r: ")) / 255
        g = int(input("g: ")) / 255
        b = int(input("b: ")) / 255
        vColor = glColor(r, g, b)
        image = ImageCreator(w, h, bgColor, vColor)
        return image
    except:
        return False


# Creador de viewport
def create_viewport(img):
    try:
        print("Coordenadas de Inicio: ")
        xStart = int(input("Ingrese el punto x de inicio: "))
        yStart = int(input("Ingrese el punto y de inicio: "))
        width = int(
            input("Ingrese el ancho de su viewport (no debe sobrepasar el el ancho más su punto x de inicio): "))
        height = int(input("Ingrese el alto de su viewport (no debe sobrepasar el el alto más su punto y de inicio): "))
    except:
        return False
    finally:
        img.glViewPort(width, height, xStart, yStart)
        return True


# Aquí el main
if __name__ == '__main__':
    print("Bienvenido al programa. Iniciemos creando una imagen")
    bandera = False
    img = ''
    mobj = ''
    op = 0
    while op != oplimit:
        try:
            op = int(input(menu))
            if op < 1 or op > oplimit:
                raise Exception()
            if op == 1:
                while not bandera:
                    img = create_image()
                    if img:
                        print("Framebuffer creado con exito")
                        bandera = True
                    else:
                        print('Ingrese los datos correctos')

            if op == 2:
                if img == '':
                    print("Todavia no ha creado su imagen")
                else:
                    bandera2 = False
                    while not bandera2:
                        res2 = create_viewport(img)
                        if res2:
                            bandera2 = True
                        else:
                            print('Ingrese valores correctos')
            if op == 3:
                if img == '':
                    print("Todavia no ha creado su imagen")
                else:
                    img.glClear()

            if op == 4:
                if img == '':
                    print("Todavia no ha creado su imagen")
                else:
                    print("Ingrese el color de fondo en formato rgb")
                    r = int(input("r: ")) / 255
                    g = int(input("g: ")) / 255
                    b = int(input("b: ")) / 255
                    img.glClearColor(r, g, b)

            if op == 5:
                if img == '':
                    print("Todavia no ha creado su imagen")
                else:
                    try:
                        x = float(input('Ingrese una coordenada x del -1 al 1: '))
                        y = float(input('Ingrese una coordenada y del -1 al 1: '))
                        img.glVertex(x, y)
                    except:
                        print("Ingrese datos completos")

            if op == 6:
                if img == '':
                    print("Todavia no ha creado su imagen")
                else:
                    print("Ingrese el color de dibujado en formato rgb")
                    r = int(input("r: ")) / 255
                    g = int(input("g: ")) / 255
                    b = int(input("b: ")) / 255
                    img.glVertexColor(r, g, b)

            if op == 7:
                if img == '':
                    print("Todavia no ha creado su imagen")
                else:
                    namefile = input("Ingrese el nombre del archivo sin su extensión: ") + '.bmp'
                    img.glFinish(namefile)

            if op == 8:
                if img == '':
                    print("Todavia no ha creado su imagen")
                else:
                    try:
                        print('Ingrese las coordenadas de -1 a 1')
                        xi = float(input("Ingrese la coordenada x inicial"))
                        yi = float(input("Ingrese la coordenada y inicial"))
                        xf = float(input("Ingrese la coordenada x final"))
                        yf = float(input("Ingrese la coordenada y final"))
                        if not img.glLine(xi, yi, xf, yf):
                            raise Exception
                    except:
                        print('Ingrese números válidos')

            if op == 9:
                if img == '':
                    print("Todavia no ha creado su imagen")
                else:
                    try:
                        namefile = input("ingrese el nombre del archivo, con su extensión y ubicación: ")
                        xStart = int(input('Ingrese la coordenada x desde donde se dibujara el modelo: '))
                        yStart = int(input('Ingrese la coordenada y desde donde se dibujara el modelo: '))
                        xScale = int(input('Ingrese la escala x con la que se dibujara el modelo: '))
                        yScale = int(input('Ingrese la escala y con la que se dibujara el modelo: '))
                        img.glModel(namefile, xStart, yStart, xScale, yScale)
                    except:
                        print('Ingrese valores correctos')

        except:
            print("Ingrese una opción válida")
