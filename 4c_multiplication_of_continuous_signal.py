# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 16:44:38 2022

@author: fuzi
"""

import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.gridspec as gdp


t = np.arange(0, 6*np.pi,0.1)
x1 = [] # first signal
x2 = [] # second signal
x3 = [] # final signal

for i in range(len(t)):
    count = np.sin(3*t[i])
    count1 = np.cos(t[i])
    x1.append(count)
    x2.append(count1)

for i in range(len(t)):
    signal_value = x1[i] * x2[i]
    x3.append(signal_value)

'''
print(t)
print(x1)
print(x2)
print(x3)
'''

fig, axs = plt.subplots(2, 2, constrained_layout=True)


# first figure
def sin_fig():
    axs[0,0].plot(t, x1, color='red', marker='.')
    axs[0,0].set_xlabel("Time t-------->", fontsize=9)
    axs[0,0].set_ylabel("x1 = sin(3t)", fontsize=9)
    axs[0,0].set_title("Sin signal", fontsize=10)
    axs[0,0].grid()

# second figure
def cos_fig():
    axs[0,1].plot(t, x2, color='blue', marker='.')
    axs[0,1].set_xlabel("Time t-------->", fontsize=9)
    axs[0,1].set_ylabel("x2 = cos(t)", fontsize=9)
    axs[0,1].set_title("Cosine signal", fontsize=10)
    axs[0,1].grid()

# third figure
def signal_multiplication():
    axs[1, 0].set_title("multiplication of the signal", fontsize=10)
    axs[1, 0].set_xlabel("time t----->", fontsize=9)
    axs[1, 0].set_ylabel("x3(t)=x1 x x2", fontsize=9)
    axs[1, 0].plot(t, x3, color='green', marker='.')
    axs[1, 0].grid()
    
fig.suptitle("Multiplication of two continuous time signal") # title of the whole figure

sin_fig()
cos_fig()
signal_multiplication()

plt.show() # display the graph in a figure