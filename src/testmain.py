from gl import ImageCreator, glColor
from models import TextureReader
from myshad import *
import mynumpy as np

r = ImageCreator(1500, 1000, glColor(0, 0, 0), glColor(1, 1, 1))

# Este es solo un main de pruebas el otro máin es el real

#r.glTriangle((100, 150, 0), (200, 250, 100), (300, 350, 200))



#r.glTriangle()



#print(np.mcross(arr, arr2)/np.mnorm([-4, -3, -2, -1, 0, 1, 2, 3, 4]))

t = TextureReader('model.bmp')

r.setShaderFunc(myToon)

r.glModel('model.obj', 250, 500, 0, 300, 300, 300, texture=t)

#r.glFinish('shadderToon.bmp')

r.setShaderFunc(myStatic)

r.glModel('model.obj', 750, 500, 0, 300, 300, 300, texture=t)

r.setShaderFunc(myRainbow)

r.glModel('model.obj', 1250, 500, 0, 300, 300, 300, texture=t)

r.glFinish('shaders.bmp')
