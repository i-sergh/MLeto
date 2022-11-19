#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np

rnd = np.random.randint


# In[2]:


class Ball:
    def __init__(self, cnv, cords, radius, color ):
        self.x = cords[0]
        self.y = cords[1]
        self.cnv =cnv
        self.radius = radius
        self.color = color
        
        self.dx = 0 * rnd(-1, 1)
        self.dy = 0 * rnd(-1, 1)
        
    def draw(self):
        cv2.circle(self.cnv, (self.x, self.y), self.radius, self.color, -1)
        
    def destroy(self):
        cv2.circle(self.cnv, (self.x, self.y), self.radius, (0, 0, 0), -1)
        
    def update(self):
        self.x += self.dx
        if self.x + self.dx + self.radius >= self.cnv.shape[1] or self.x + self.dx - self.radius <= 0:
            self.dx *= -1
            self.slow_dx()
            
        self.y += self.dy
        
        if self.y + self.dy + self.radius >= self.cnv.shape[0] or self.y + self.dy - self.radius <= 0:
            self.dy *= -1
            self.slow_dy()
            
        self.draw()
        
    def add_dx(self, dx_):
        self.dx += dx_
        
    def add_dy(self, dy_):
        self.dy += dy_
        
    def slow_dx(self):
        if self.dx > 1 and np.abs( int(self.dx/ 2) ) > 0:
            self.dx = 1 and np.abs( int(self.dx/ 2) )
            
    def slow_dy(self):
        if self.dy > 1 and np.abs( int(self.dy/ 2) ) > 0:
            self.dy = 1 and np.abs( int(self.dy/ 2) )
    def stop(self):
        self.dy = 0
        self.dx = 0
    def blast(self):
        self.dy = rnd(1,2) * rnd(-1,2)
        self.dx = rnd(1,2) * rnd(-1,2)


# In[3]:


cnv = np.zeros( (600, 600, 3), dtype=np.uint8() )
#mrB = Ball(cnv, (150, 200), 75, (240, 230, 150))
mrB = []
for i in range(1000):
     
    coords = (rnd(0,600), rnd(0,600))
    radius = rnd(1, 5)
    #print(radius, end='  ')
    if coords[0] - radius <= 0:
        radius = radius + coords[0] - radius
    if coords[1] - radius <= 0:
        radius = radius + coords[1] - radius
    if coords[0] + radius > cnv.shape[1]:
        radius = radius - (coords[0] + radius - cnv.shape[1])
    if coords[1] + radius > cnv.shape[0]:
        radius = radius - (coords[1] + radius - cnv.shape[0])
    #print(radius)
    
    mrB.append( Ball(cnv,  coords, radius, (rnd(0,255), rnd(0,255), rnd(0,255))) )


while True:
    for i in range(1000):
        mrB[i].destroy()
        mrB[i].update()
        mrB[i].draw()
    
    cv2.imshow('privet', cnv)

   
    key = cv2.waitKey(1) # ожидание нажатия на клавишу
    if key == 27:
        break
    
        
    if key ==ord('w'):
        for i in range(1000):
            mrB[i].add_dy(-1)
    if key ==ord('a'):
        for i in range(1000):
            mrB[i].add_dx(-1)
    if key ==ord('s'):
        for i in range(1000):
            mrB[i].add_dy(1)
    if key ==ord('d'):
        for i in range(1000):
            mrB[i].add_dx(1)
    if key ==32:
        for i in range(1000):
            mrB[i].stop()
    if key ==113:
        for i in range(1000):
            mrB[i].blast()
    if key == 13:
        mrB = []
        cnv = np.zeros( (600, 600, 3), dtype=np.uint8() )
    
        for i in range(1000):
            radius = rnd(1, 5)
            coords = (rnd(0+radius,600-radius), rnd(0+radius,600-radius))
            
            mrB.append( Ball(cnv,  coords, radius, (rnd(0,255), rnd(0,255), rnd(0,255))) )
            mrB[-1].draw()

cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




