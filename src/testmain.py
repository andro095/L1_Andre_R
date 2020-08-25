from gl import ImageCreator, glColor
from models import TextureReader
from myshad import *
from mynumpy import *
import numpy as np
#import mynumpy as np

r = ImageCreator(768, 432, glColor(0, 0, 0), glColor(1, 1, 1))

# Este es solo un main de pruebas el otro máin es el real

# r.glTriangle((100, 150, 0), (200, 250, 100), (300, 350, 200))


# r.glTriangle()



t = TextureReader('model.bmp')
#
r.setShaderFunc(myToon)

mPos = [0, 0, -5]

#r.glLookAt(mPos, [0, 0, 0])
r.glLookAt(mPos, [2, 0, 0])
#
r.glModel('model.obj', mPos[0], mPos[1], mPos[2], 2, 2, 2, 0, 0, -29, texture=t)
#

r.glFinish('DutchAngleshot.bmp')
#
# r.setShaderFunc(myStatic)
#
# r.glModel('model.obj', 450, 250, 0, 200, 200, 200, texture=t)
#
# r.setShaderFunc(myRainbow)
#
# r.glModel('model.obj', 750, 250, 0, 200, 200, 200, texture=t)
#
# r.setShaderFunc(myGray)
#
# r.glModel('model.obj', 1050, 250, 0, 200, 200, 200, texture=t)
#
# r.setShaderFunc(myInvert)
#
# r.glModel('model.obj', 1350, 250, 0, 200, 200, 200, texture=t)
#
# r.glFinish('shaders.bmp')
