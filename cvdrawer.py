import cv2
import numpy as np

# массив итогового  изо 28 x 28


X_in = np.zeros((28,28), dtype=np.float32() )
bcolor = np.array([255, 0, 0], dtype=np.uint8())
cnv = np.ones((560, 560, 3), dtype=np.uint8()) * bcolor 

cv2.namedWindow('canvas')


def grid(cnv, xstep, ystep, color = (0,255,0) ):
    cnv[:, ::xstep] = color
    cnv[::ystep, :] = color

grid(cnv, 20, 20, color = (10,10,10) )





def draw(event, x,y, flags, param):
    print('event=',event,'x=', x,'y=', y,'flags=', flags,'param=', param)

    power = 80
    # добавляем 1, чтобы не закрашивать сетку (мы сдвинули на 1)
    y = y - y%20+1
    x = x - x%20+1

    # left click
    if flags == 1:
        # добавляем 19, чтобы не закрашивать сетку, но с другой стороны (мы уже добавили 1)
        #B
        if cnv[y, x, 0 ] - power > 0:
            cnv[y: y+19, x:x+19, 0 ] -= power 
        else:
            cnv[y: y+19, x:x+19, 0 ] = 0  
        #G
        if cnv[y, x, 1 ] + power < 255:
            cnv[y: y+19, x:x+19, 1 ] += power
        else:
            cnv[y: y+19, x:x+19, 1 ] = 255
        #R
        if cnv[y, x, 2 ] + power < 255:
            cnv[y: y+19, x:x+19, 2 ] += power 
        else:
            cnv[y: y+19, x:x+19, 2 ] = 255
        
    # right click
    elif flags == 2:
        #B
        if cnv[y, x, 0 ] + power < 255:
            cnv[y: y+19, x:x+19, 0 ] += power
        else:
            cnv[y: y+19, x:x+19, 0 ] = 255
        #G
        if cnv[y, x, 1 ] - power > 0:
            cnv[y: y+19, x:x+19, 1 ] -= power
        else:
            cnv[y: y+19, x:x+19, 1 ] = 0
        #R
        if cnv[y, x, 2 ] - power > 0:
            cnv[y: y+19, x:x+19, 2 ] -= power 
        else:
            cnv[y: y+19, x:x+19, 2 ] = 0
cv2.setMouseCallback('canvas', draw)
while True:
    
    cv2. imshow('canvas',cnv)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()