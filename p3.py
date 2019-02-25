#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 15:11:58 2019

@author: katieturnlund
"""
#Katherine Turnlund
#Last Edited: 2-14-2019
#Exercise 3: Monte Carlo Integration of a Given Function

import numpy as np


#Defines the function we will be integrating over
def f(x,y):
   z = (x+2*y)*(x+y)
   return z

#Define the integration bounds
min_x = 0.0
max_x = 1.0
interval_x = max_x - min_x
min_y = 2.0
max_y = 4.0
interval_y = max_y - min_y

#Processing function values
n = 1000 
x = np.linspace(min_x,max_x,n)
y = np.linspace(min_y,max_y,n)
function = np.zeros((n,n))

#Turn zeros of function array into values
for i in range(n):
    for j in range(n):
        function[i][j] = f(x[i],y[j])
        
min_f = np.amin(function)
max_f = np.amax(function)
interval_f = max_f - min_f

#Monte Carlo integration
number = 100000
x_random = min_x + interval_x*np.random.random(number)
y_random = min_y + interval_y*np.random.random(number)
f_random = min_f + interval_f*np.random.random(number)

count_above = []
count_below = []

#Determine whether f_random is within the volume of integration
for i in range(number):
    if f_random[i] < f(x_random[i],y_random[i]):
        count_below.append(f_random[i])
    else:
        count_above.append(f_random[i])

percent_below = len(count_below)/number


volume_in_interval = interval_x*interval_y*interval_f
vol_below = interval_x*interval_y*min_f

integral = volume_in_interval * percent_below + vol_below

print('The fraction of random points within the interval below the curve: %5f' % (percent_below))
print('The value of the integral is %5f' % (integral))


