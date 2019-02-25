# Exercise 1
import ccHistStuff as cc
import numpy as np
import matplotlib.pyplot as plt


#Load the .npy array, store it into x

x = np.load('dataSet.npy')

#Determine number of bins: integer values of set of data

x_list = list(set(np.around(x)))
bin_count = len(x_list)

#Make histogram

fig, ax = plt.subplots()
plt.hist(x, bins = bin_count)
contents, binEdges, _ = ax.hist(x, bin_count, histtype='step', log=False, color='blue')
plt.yscale('log')
cc.statBox(ax, x, binEdges)
plt.title('Distribution of the Data loaded from dataSet.npy')
plt.ylabel('Count of x value')
plt.xlabel('x value')
plt.show()

