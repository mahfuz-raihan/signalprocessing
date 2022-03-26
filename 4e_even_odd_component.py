# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 20:37:51 2022

@author: fuzi
"""

import numpy as np
import matplotlib.pyplot as plt


step = 0.01
# w = 2*np.pi/4

t = np.arange(0, 5, step)
y = t*np.cos(3*np.pi*t)
ye = 0.5*(y + y)
yo = 0.5*(y - y)
y_t = ye + yo

'''
for i in range(len(t)):
    x = t*np.exp(t[i]) # original signal
    x_t= t*np.exp(-t[i]) # reverse signal
    xe = 0.5*t*(np.exp(t[i]) - np.exp(t[i])) # even signal formula
    xo = 0.5*t*(np.exp(t[i]) + np.exp(t[i])) # odd signal formula
    
    # add the value in list
    y.append(x)
    y_t.append(x_t)
    ye.append(xe)
    yo.append(xo)

print(t)
print(y_t)
print(ye)
print(yo)
'''

fig, axs = plt.subplots(2, 2, constrained_layout=True)


def original_signal(): # display the original signal
    axs[0,0].plot(t, y, color='r')
    axs[0,0].set_xlabel("Time t-------->", fontsize=9)
    axs[0,0].set_ylabel("x(t)---->", fontsize=9)
    axs[0,0].set_title("Original signal", fontsize=10)
    axs[0,0].grid()

def even_signal():
    axs[0,1].plot(t, ye, color='b')
    axs[0,1].set_xlabel("Time t-------->", fontsize=9)
    axs[0,1].set_ylabel("xe(t)---->", fontsize=9)
    axs[0,1].set_title("Even part", fontsize=10)
    axs[0,1].grid()
    
    
def odd_signal(): # display even signal
    axs[1,0].plot(t, yo, color='b')
    axs[1,0].set_xlabel("Time t-------->", fontsize=9)
    axs[1,0].set_ylabel("xo(t)---->", fontsize=9)
    axs[1,0].set_title("Odd part", fontsize=10)
    axs[1,0].grid()


def reverse_signal(): # display odd signal
    axs[1,1].plot(t, y_t, color='b')
    axs[1,1].set_xlabel("Time t-------->", fontsize=9)
    axs[1,1].set_ylabel("xr(t)---->", fontsize=9)
    axs[1,1].set_title("summation of two part", fontsize=10)
    axs[1,1].grid()


original_signal()
reverse_signal()
even_signal()
odd_signal()

plt.suptitle("Even and Odd signal component", color='r')
plt.show() # display the figure in the section