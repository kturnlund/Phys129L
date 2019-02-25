#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:12:13 2019

@author: katieturnlund
"""

#Exercise 5

import numpy as np
import matplotlib.pyplot as plt

#Determine x values

mu = 3
sigma = 0.5
N = 5

x = np.linspace(-3,15,100)

estimate_fx = []

#set function
def g(x,y):
    return np.exp(-x-y)*(x+y)**N
 
    
#Iterate through x, calculate g(y)
for i in range(len(x)):
    y = np.random.normal(loc = 3, scale = 0.5, size = 1000)
    gy = []
    for j in range(len(y)):
        new_g = g(x[i],y[j])
        gy.append(new_g)
    estimate_fx.append(sum(gy)/len(y))

#Plot figure
fig, ax = plt.subplots()

plt.plot(x,estimate_fx)
plt.xlabel('x')
plt.xlim(-3,15)
plt.ylabel('Estimate of f(x)')
plt.title('f(x) Estimation with N=5')
plt.show()