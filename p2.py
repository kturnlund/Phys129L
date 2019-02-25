#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:48:29 2019

@author: katieturnlund
"""

#Katherine Turnlund

#Homework #5 Exercise 2

import numpy as np
import matplotlib.pyplot as plt

#Define the coloring of the plot
thisMap = 'plasma'

#Determine size of image
xpix = 640
ypix = 400

#Determine scale of image
xmin = -1.6
xmax = 1.6
xwidth = 3.2

ymin = -1.0
ymax = 1.0
ywidth = 2.0

xc = int(xpix/2)
yc = int(ypix/2)

pixColor = np.zeros((xpix,ypix),dtype = "uint8")

c = complex(-0.76,0.51)


#Define function to create count of iterations for each pixel
for i in range(xpix):
    x = i/xpix * xwidth + xmin
    for j in range(ypix):
        y = j/ypix * ywidth + ymin
        n = 0
        z = complex(x,y)
        while abs(z) <= 2 and n < 255:
            z = z**2 + c
            n+=1
        pixColor[i][j] = n

#Flip/transpose array of n values
new_pixColor = np.flipud(pixColor.transpose())

#Plot array
f1, ax1 = plt.subplots()
picture = ax1.imshow(new_pixColor,interpolation = 'nearest', aspect = 'auto', cmap = thisMap)
ax1.axis('off')
f1.show()
