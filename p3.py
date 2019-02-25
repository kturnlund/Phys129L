#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 15:45:18 2019

@author: katieturnlund
"""

#Katherine Turnlund

#Homework #5 Exercise 3

import numpy as np
import matplotlib.pyplot as plt
import ccHistStuff as cc

#use np.loadtxt in place of np.load

x = np.loadtxt('mass.txt')

x_list = list(set(np.around(x)))
bin_count = len(x_list)

#Make histogram

fig, ax = plt.subplots()
plt.hist(x, bins = bin_count)
contents, binEdges, _ = ax.hist(x, bin_count, histtype='step', log=False, color='blue')
plt.yscale('log')
cc.statBox(ax, x, binEdges)
plt.title('Distribution of the Data loaded from mass.txt')
plt.ylabel('Count of invariant mass')
plt.xlabel('Invariant mass (GeV/c^2)')
plt.xlim(100,200)
plt.show()