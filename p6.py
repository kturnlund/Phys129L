#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 15:38:35 2019

@author: katieturnlund
"""

#Katherine Turnlund

#Homework #5 Exercise 6: Runge-Kutta Method

import numpy as np
import matplotlib.pyplot as plt

#Define V_in function:
def V_in(x):
    z = 0
    if x % 2 <= 1:
        z = 1.0
    elif 1 < x % 2 < 2:
        z = -1.0
    return z

#take input from keyboard for tau
tau = input('Enter a value for tau: ')

tau  =  float(tau)

#Define differential equation 
def diffV_out(Vin, Vout, tau):
    dVout_dt = 1/tau*(Vin - Vout)
    return dVout_dt

#Runge-Kutta iterative method for this function

n = 10000 #number of iterations
interval = 100 #interval of plotting
h = interval/n #step size for iteration

#Create Vout vector for storage of values
t = np.zeros(n)
Vout = np.zeros(n)

#Runge-Kutta method creation of values
for i in range(1,n):
    k_1 = h * diffV_out(V_in(t[i-1]), Vout[i-1], tau)
    k_2 = h * diffV_out(V_in(t[i-1]+h/2), Vout[i-1]+k_1/2, tau)
    k_3 = h * diffV_out(V_in(t[i-1]+h/2), Vout[i-1]+k_2/2, tau)
    k_4 = h * diffV_out(V_in(t[i-1]+h/2), Vout[i-1]+k_3, tau)
    t[i] = t[i-1] + h
    Vout[i] = Vout[i-1] + 1/6*(k_1 + 2*k_2 + 2*k_3 + k_4)

#Splitting vectors to separate out for two plots
Vout1, Vout2, Vout3 = np.split(Vout,[int(0.1*n),int(0.9*n - 1)])
t1, t2, t3 = np.split(t,[int(0.1*n),int(0.9*n - 1)])

#1st plot: 0 < t < 10
plt.plot(t1, Vout1, 'b-')
plt.xlabel('Time (us)')
plt.xlim([0,10])
plt.ylabel('V_out (V)')
plt.title('V_out for 0 < t < 10 us')
plt.show()

#2nd plot: 90 < t < 100
plt.plot(t3, Vout3, 'b-')
plt.xlabel('Time (us)')
plt.xlim([90,100])
plt.ylabel('V_out (V)')
plt.title('V_out for 90 < t < 100 us')
plt.show()



