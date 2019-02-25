#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:18:47 2019

@author: katieturnlund
"""

#Katherine Turnlund

#Homework #5 Exercise 4

#Prompt user for  number: 16-bit integer most likely?

userInput = input('Enter a 16-bit integer: ')

listedInput = list(userInput) #separates all digits of inputted binary number

#1st four digits go to channel number reading
bitChannel = listedInput[0] + listedInput[1] + listedInput[2] + listedInput[3]

#2nd four digits go to time reading
bitTime = listedInput[4] + listedInput[5] + listedInput[6] + listedInput[7]

#remaining digits go to pulse height reading
bitPulseHeight = ''
for i in range(8):
    n = i + 8
    bitPulseHeight = bitPulseHeight + listedInput[n]
    
#change strings into integers with binary reading
numChannel = int(bitChannel,2)
numTime = int(bitTime,2)
numPulseHeight = int(bitPulseHeight,2)

#print values obtained. Would prefer to use units accompanying but no units were specified.
print('Channel Number: %d' % (numChannel))
print('Time: %d' % (numTime))
print('Pulse Height: %d' % (numPulseHeight))
