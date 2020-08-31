from gl import ImageCreator, glColor
from models import TextureReader
from myshad import *
from mynumpy import *
from src.myshad import myNormal

r = ImageCreator(564, 376, glColor(0, 0, 0), glColor(1, 1, 1))

# Este es solo un main de pruebas el otro máin es el real


r.glBackground('./backgrounds/living_room.bmp')


t = TextureReader('./textures/CatMac_C.bmp')

r.setNormalMap(TextureReader('./normalmaps/CatMac_N.bmp'))
#
r.setShaderFunc(myNormal)

r.glModel('./objmodels/CatMac.obj', -2.8, -1.2, -5, 3, 3, 3, 0, 45, 0, texture=t)

r.setShaderFunc(myGray)

t = TextureReader('./textures/man.bmp')

r.glModel('./objmodels/man.obj', -1.22, -1.75, -4, 0.02, 0.02, 0.02, 0, 0, 0, texture=t)

r.setShaderFunc(myInvert)

t = TextureReader('./textures/ivan.bmp')

r.glModel('./objmodels/ivan.obj', 2.6, -1.75, -4, 0.002, 0.002, 0.002, 0, -90, 0, texture=t)

r.setShaderFunc(myRainbow)

t = TextureReader('./textures/table.bmp')

r.glModel('./objmodels/table.obj', 0.5, -1.75, -4, 0.04, 0.04, 0.04, 0, 0, 0, texture=t)

r.setShaderFunc(myStatic)

t = TextureReader('./textures/table.bmp')

r.glModel('./objmodels/sphere.OBJ', 0.5, -1, -4, 0.003, 0.003, 0.003, 0, 0, 0, texture=t)


r.glFinish('./screenshots/Prueba.bmp')

