#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:12:08 2019

@author: katieturnlund
"""

#Exercise 4

import ccHistStuff as cc
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def myPDF(x,y):
    return 1/7*(x+y)

def proposal(x):
    step = 0.5
    return x - step + 2*step*np.random.rand()

xstart = 0.5
n      = 100000
nBurn  = 10000

ystart = 3.

xlow = 0.
ylow = 2.
xhigh = 1.
yhigh = 4.

function = []

xlist = [xstart]
ylist = [ystart]

for i in range(n+nBurn-1):
    xp    = proposal(xlist[-1])
    yp    = proposal(ylist[-1])
    fnow  = myPDF(xlist[-1], ylist[-1])
    fnext = myPDF(xp, yp)
    if np.random.rand() < fnext/fnow and xp >= xlow and xp <= xhigh and yp >= ylow and yp <= yhigh:
        xlist.append(xp)
        ylist.append(yp)
    else:
        xlist.append(xlist[-1])
        ylist.append(ylist[-1])
        
yr = np.array( ylist[nBurn : ] )
xr = np.array( xlist[nBurn : ] )

plt.hist2d(xr,yr)
plt.show()


def g(x,y):
    return 7*(x+2*y)

for i in range(len(xr)):
    function.append(g(xr[i],yr[i]))

integral = sum(function)/len(xr)

print('The estimate of the integral is %5f' % (integral))
