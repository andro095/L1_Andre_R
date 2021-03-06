from gl import glColor, ImageCreator
from  models import TextureReader
from myshad import *

menu = "Menú:\n   1. Crear una nueva imagen\n   2. Definir un ViewPort\n   3. Borrar todo punto realizado (Clear())\n" \
       "   4. Cambiar el color del clear\n   5. Dibujar un punto\n   6. Cambiar el color de dibujado\n   7. Imprimir " \
       "la imagen\n   8. Realizar una linea\n   9. Dibujar un modelo obj\n   10. Rellenar un poligono\n   11. " \
       "Proyecto #1 (No tiene que crear imagen con este por su cuenta)\n   12. Salir del programa\nIngrese una opción: "

oplimit = 12


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
                        zScale = int(input('Ingrese la escala z con la que se dibujara el modelo: '))
                        res = ''
                        while res.lower() != 'y' and res.lower() != 'n':
                            res = input('Desea que se despliegue el wireframe (y/n):').lower()

                        isWire = True if res == 'y' else False
                        res = ''
                        while res.lower() != 'y' and res.lower() != 'n':
                            res = input('Desea que se agregue una textura? (y/n):').lower()

                        if res == 'y':
                            bandera = True
                            while bandera:
                                try:
                                    dir = input('Ingrese la dirección del archivo con su nombre y extensión: ')
                                    open(dir, 'rb')
                                    bandera = False
                                except:
                                    print('Ingrese una dirección correcta')
                        texture = TextureReader(dir)

                        print('Se desplegara con un Toon Shader')
                        img.setShaderFunc(myToon)

                        img.glModel(namefile, xStart, yStart, 0, xScale, yScale, zScale, texture=texture, isWire=isWire)
                    except:
                        print('Ingrese valores correctos')
            if op == 10:
                if img == '':
                    print("Todavia no ha creado su imagen")
                else:
                    op = ''
                    while op.lower() != 'y' and op.lower() != 'n':
                        op = input('Tiene un archivo txt con el polígono que desea agregar? (y/n): ')
                    arr = []
                    if op == 'y':
                        print('Las coordenadas deben estar ingresadas en tuplas (x,y), una por linea para funcionar. '
                              'Puede consultar a los ejemplos de formato adjuntos a este programa para más detalles')
                        namefile = input('Ingrese el nombre de su archivo con su extensión: ')
                        try:
                            f = open(namefile, 'r')
                            arr = [list(map(int, linea.replace('\n', '').replace('(', '').replace(')', '').replace(' ', '').split(','))) for linea in f.readlines()]
                        except:
                            print('Error el archivo no se encuentra o no se puede leer')
                        finally:
                            f.close()

                        if len(arr) > 2:
                            img.glPolygon(arr)
                        else:
                            print('No ingreso los suficientes vertices')

                    else:
                        print('Ingresando coordenadas manualmente.')
                        x = 0
                        y = 0
                        while x >= 0 and y >= 0:
                            try:
                                x = int(input('Ingrese la cordenada x (Ingrese numero negativo para dejar de ingresar '
                                              'coordenadas): '))
                                if x >= 0:
                                    y = int(input('Ingrese la cordenada y (Ingrese numero negativo para dejar de '
                                                  'ingresar coordenadas): '))

                                if x >= 0 and y >= 0:
                                    arr.append((x, y))

                            except:
                                print('Ingrese números correctos')
                        if len(arr) > 2:
                            img.glPolygon(arr)
                        else:
                            print('No ingreso los suficientes vertices')

            if op == 11:
                print("Creando la imagen...")
                r = ImageCreator(564, 376, glColor(0, 0, 0), glColor(1, 1, 1))
                print('Imagen Creada')
                print('Añadiendo Fondo')
                r.glBackground('./backgrounds/living_room.bmp')
                print('Fondo Añadido')
                print('Empezamos a cargar modelos')
                print('Empezamos con el Modelo del gato. Este modelo es el que contiene el mapa de normales')
                print('Cargamos la textura')
                t = TextureReader('./textures/CatMac_C.bmp')
                print('Textura Cargada')
                print('Cargando el mapa normal')
                r.setNormalMap(TextureReader('./normalmaps/CatMac_N.bmp'))
                print('Mapa normal cargado')
                print('Configurando el shadder')
                r.setShaderFunc(myNormal)
                print('Shadder Configurado')
                print('Cargamos el modelo del gato')
                r.glModel('./objmodels/CatMac.obj', -2.8, -1.2, -5, 3, 3, 3, 0, 45, 0, texture=t)
                print('Modelo cargado')
                print('Seguimos con el hombre de negocios')
                print('Cargamos su textura')
                t = TextureReader('./textures/man.bmp')
                print('Textura cargada')
                print('Configurando el shadder')
                r.setShaderFunc(myGray)
                print('Shadder configurado')
                print('Cargamos el modelo del hombre')
                r.glModel('./objmodels/man.obj', -1.22, -1.75, -4, 0.02, 0.02, 0.02, 0, 0, 0, texture=t)
                print('Modelo cargado')
                print('Seguimos con el joven')
                print('Cargamos su textura')
                t = TextureReader('./textures/ivan.bmp')
                print('Textura cargada')
                print('Configurando el shadder')
                r.setShaderFunc(myInvert)
                print('Shadder configurado')
                print('Cargamos el modelo del hombre')
                r.glModel('./objmodels/ivan.obj', 2.6, -1.75, -4, 0.002, 0.002, 0.002, 0, -90, 0, texture=t)
                print('Modelo cargado')
                print('Seguimos con la mesa')
                print('Cargamos su textura')
                t = TextureReader('./textures/table.bmp')
                print('Textura cargada')
                print('Configurando el shadder')
                r.setShaderFunc(myRainbow)
                print('Shadder configurado')
                print('Cargamos el modelo de la mesa')
                r.glModel('./objmodels/table.obj', 0.5, -1.75, -4, 0.04, 0.04, 0.04, 0, 0, 0, texture=t)
                print('Modelo cargado')
                print('Finalizamos con la esfera')
                print('Cargamos su textura')
                t = TextureReader('./textures/table.bmp')
                print('Textura cargada')
                print('Configurando el shadder')
                r.setShaderFunc(myStatic)
                print('Shadder configurado')
                print('Cargamos el modelo de la esfera')
                r.glModel('./objmodels/sphere.OBJ', 0.5, -1, -4, 0.003, 0.003, 0.003, 0, 0, 0, texture=t)
                print('Modelo cargado')
                print('Render terminado')
                print('Creando bmp con nombre Proyecto1.bmp')
                r.glFinish('./screenshots/Proyecto1.bmp')
                print('Bmp creado')
                print('Encontrará el resultado en la carpeta de screenshots.')
                print('Feliz dia')


        except:
            print("Ingrese una opción válida")
