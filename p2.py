# Exercise 2


#Katherine Turnlund
#Last Edited: 2-15-2019
#Exercise 2: Poisson Distribution

#genPoisson.py code
#######################
import argparse
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import ccHistStuff as cc

# Define the arguments
parser =  argparse.ArgumentParser(description="Generate and plot Poisson variable. Calculate pvalue of observed")
parser.add_argument('-m','--mean', help='Mean of the Poisson', required=True, type=float)
parser.add_argument('-n', '--nev', help='No. to generate. Default=10K', required=False, type=int, default=10000)
parser.add_argument('-L', '--Low', help='Minimum for plot', required=False, type=int)
parser.add_argument('-H', '--High', help='Maximum for plot', required=False, type=int)
parser.add_argument('-s', '--seed', help='Random seed. Default=10', required=False, type=int, default=1)
parser.add_argument('-o', '--obs',  help='Number of observed events', required=True, type=int)
parser.add_argument('-u', '--unc', help='Uncertainty of the Poisson', required=True, type = float)
parser.add_argument('-g', '--gauss', help='Toggle Gaussian for mean (enter 1). Default = 0', required=False, type = int, default = 0)

# This is a dictionary containing the arguments
args = vars(parser.parse_args())

# Extract the arguments
mean   = args['mean']  # mean
nev    = args['nev']   # number of events to generate
seed   = args['seed']
obs    = args['obs']
unc    = args['unc']
gauss  = args['gauss']

nsigma = 5.             # plot to \pm 5 sigma if not specified 
if args['Low'] == None:
    nMin = int(max(0., mean-nsigma*math.sqrt(mean)))
else:
    nMin = args['Low']
if args['High'] == None:
    nMax = int(max(0., mean+nsigma*math.sqrt(mean)))
else:
    nMax = args['High']

# Make sure we dont have to low a maximum
if nMax < 6: nMax=6
if nMax < 1.2*obs: nMax=1.2*obs

#Determine N for number of trials on Poisson Distribution
N = 100

#create means for multiple poission distributions and check for gauss/lognormal
stored_means = []
if gauss != 0:
    while len(stored_means) < N:
        x = np.random.normal(loc = mean, scale = unc)
        if x >= 0:
            stored_means.append(x)
else:
    while len(stored_means) < N:
        x = np.random.lognormal(mean = mean, sigma = unc)
        x = np.log(x)
        if x >= 0:
            stored_means.append(x)


fig, ax = plt.subplots(1,1)

#plot all "uncertain" poissons
for i in range(N):
    entries = np.random.poisson(stored_means[i], nev)
    contents, binEdges, _ = ax.hist(entries, np.linspace(nMin-0.5, nMax+0.5, nMax-nMin+2), histtype='step', log=False, color='cyan')

# Initialize the random seed
np.random.seed(seed)

# Generate a bunch of poisson
entries = np.random.poisson(mean, nev)

# Calculate the pvalue
boolArray = entries >= obs   # an array of True/False
nTail = boolArray.sum()      # the number of trues in the array
print("-------------------------------")
if nTail == 0:
    print("Not a single try with at least %d entries" %obs)
    print("Cannot calculate very small pvalue")
else:
    pvalue = nTail/nev
    nsigma = stats.norm.ppf(1-pvalue)
    print("pvalue        = ", pvalue)
    print("which corresponds to")
    print("No. of sigmas = ", nsigma)
    print("This number of sigma (n) is from the tail integral of a gaussian distribution.")
    print("In other words, for a gaussian of mean=0 and sigma=1, the integral from")
    print("n to infinity would be equal to ", pvalue)
print("-------------------------------")
    
# Define 1x1 figure

# the histogram
contents, binEdges, _ = ax.hist(entries, np.linspace(nMin-0.5, nMax+0.5, nMax-nMin+2), histtype='step', log=False, color='black')
cc.statBox(ax, entries, binEdges)
ax.set_xlim(binEdges[0], binEdges[-1])
ax.set_title('Poisson Distribution including Uncertainty (Cyan)')
ax.set_xlabel('x')
ax.set_ylabel('Count of x')
ax.tick_params("both", direction='in', length=10, right=True)

# show the figure
fig.show()
# plt.show()  (this would pause automatically)
input("Press any key to continue")
##################################
#My code:




