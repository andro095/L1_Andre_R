from gl import ImageCreator, glColor

r = ImageCreator(800,600,glColor(0,0,0),glColor(1,0,0))

r.glModel('bears.obj', 400,200 , 15,15 )





r.glFinish('output.bmp')
