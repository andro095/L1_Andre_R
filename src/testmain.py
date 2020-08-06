from gl import ImageCreator, glColor
import mynumpy as np
r = ImageCreator(1000, 1000, glColor(0, 0, 0), glColor(1, 1, 1))

# Este es solo un main de pruebas el otro máin es el real

#r.glTriangle((100, 150, 0), (200, 250, 100), (300, 350, 200))

r.glModel('model.obj', 500, 500, 0, 300, 300, 300)

#r.glTriangle()



#print(np.mcross(arr, arr2)/np.mnorm([-4, -3, -2, -1, 0, 1, 2, 3, 4]))



r.glFinish('hosli.bmp')
