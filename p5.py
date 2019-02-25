#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:20:31 2019

@author: katieturnlund
"""


#Katherine Turnlund

#Homework #5 Exercise 5

import numpy as np

#define the function we're trying to find the root of: xcos(x)-1/2=0
def xcosx(x):
    return x * np.cos(x) - 0.5

#Define beginning parameters
a = 0.6
b = 0.8
c = 0.7
f_a = xcosx(a)
f_b = xcosx(b)
f_c = 1

#Bisection method while loop to get f(c) within error margin
while abs(f_c) >= 0.00001:
    c = (a+b)/2
    f_c = xcosx(c)
    if f_c < 0:
        a = c
    elif f_c > 0:
        b = c

print("The solution to xcos(x) = 1/2 is %.4f with an error margin of 0.0001" % (c))
        