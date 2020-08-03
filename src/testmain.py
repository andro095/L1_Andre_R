from gl import ImageCreator, glColor

r = ImageCreator(800, 600, glColor(0, 0, 0), glColor(1, 0, 0))

#r.glPolygon([(165, 380), (185, 360), (180, 330), (207, 345), (233, 330), (230, 360), (250, 380), (220, 385), (205, 410),
 #            (193, 383)])
#r.glVertexColor(0,1,0)
#r.glPolygon([(321, 335), (288, 286), (339, 251), (374, 302)])

#r.glVertexColor(0,1,1)
#r.glPolygon([(377, 249), (411, 197), (436, 249)])

#r.glVertexColor(0,0,1)
#r.glPolygon([(413, 177), (448, 159), (502, 88), (553, 53), (535, 36), (676, 37), (660, 52),
#(750, 145), (761, 179), (672, 192), (659, 214), (615, 214), (632, 230), (580, 230),
#(597, 215), (552, 214), (517, 144), (466, 180)])

#r.glVertexColor(1,1,0)
#r.glPolygon([(682, 175), (708, 120), (735, 148), (739, 170)])


arr = []

try:
    f = open('polygon.txt', 'r')
    arr = [list(map(int, linea.replace('\n', '').replace('(', '').replace(')', '').replace(' ', '').split(','))) for linea in f.readlines()]
except:
    print('Error')
finally:
    f.close()

#r.glFinish('holi.bmp')
