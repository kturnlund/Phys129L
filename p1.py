#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:47:55 2019

@author: katieturnlund
"""

#Katherine Turnlund
#
#Homework #5: Exercise 1

#Start with a Monte Carlo integration of integral, then evaluate integral @ varying alpha values.

import matplotlib.pyplot as plt
import numpy as np
import scipy.special as sp


#number of points for MC integration
N = 1000

#Given function to integrate over (given alpha, beta)

def harmOsc(alpha,beta):
    return 2 / (np.pi * (np.sqrt(1 - (np.sin(alpha / 2)) ** 2 * (np.sin(beta)) ** 2)))

#Monte Carlo integration function (given alpha)

def MonteCarlo(alpha, N):
    
    #define function values for the interval
    
    beta_set = np.linspace(0,np.pi/2,N)
    harmOsc_set = np.zeros(N)
    
    for i in range(N):
        harmOsc_set[i] = harmOsc(alpha,beta_set[i])
        
    min_HO = np.amin(harmOsc_set)
    max_HO = np.amax(harmOsc_set)
    interval_HO = max_HO - min_HO
    
    #create random vectors within respective intervals
    
    beta_random = np.random.rand(N)*np.pi/2
    harmOsc_random = min_HO + interval_HO*np.random.rand(N)
    
    count_below = []
    
    #Check if random numbers are below function value
    
    for i in range(N):
        if harmOsc_random[i] < harmOsc(alpha, beta_random[i]):
            count_below.append(harmOsc_random[i])
    
    frac_below = len(count_below)/N
    interval_area = np.pi/2 * interval_HO
    area_below = np.pi/2 * min_HO
    
    integral = interval_area * frac_below + area_below
    
    return integral

#Defining integral approximation

alpha = np.linspace(1,91,90)
T_over_T0 = np.zeros(90)

for i in range(90):
    T_over_T0[i] = MonteCarlo(alpha[i],N)

#Defining exact integral
    
m = (np.sin(alpha/2))**2
exact_T_over_T0 = sp.ellipk(m)*2/np.pi

diff_T_T0 = exact_T_over_T0-T_over_T0

#plot values

plt.plot(alpha,T_over_T0,'r-',label = 'Integral Approximation')
plt.plot(alpha, exact_T_over_T0, 'k:', label = 'Exact Integral')
plt.xlim([0,90])
plt.ylim([0,4])
plt.xlabel('Alpha (Degrees)')
plt.ylabel('T/To')
plt.title('Period of Oscillation of a Pendulum without the Small Angle Approximation')
plt.legend()

plt.show()
