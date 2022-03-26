# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 16:37:31 2022

@author: fuzi
"""

import numpy as np
import matplotlib.pyplot as plt



fig, axs = plt.subplots(2, 2, constrained_layout=True)


# first figure
def first_signal():
    # first signal
    t1 = np.arange(0, 10, 0.01)
    y1 = np.cos(t1)
    
    # plot the figure
    axs[0,0].plot(t1, y1, color='red')
    axs[0,0].set_xlabel("Time t-------->", fontsize=7)
    axs[0,0].set_ylabel("y(t) = cos(t)", fontsize=7)
    axs[0,0].set_title("continuous signal(0 =< t =< 10)", fontsize=9)
    axs[0,0].grid()

# second figure
def second_signal():
    # second signal
    pi = np.pi
    t2 = np.arange(1,4*pi, 0.01)
    y2 = 3*(np.cos(3*pi*t2+pi/3))
    
    # plot the figure
    axs[0,1].plot(t2, y2, color='blue')
    axs[0,1].set_xlabel("Time t-------->", fontsize=7)
    axs[0,1].set_ylabel("y(t) = 3cos(wt+pi/4)", fontsize=7)
    axs[0,1].set_title("Continuous signal", fontsize=9)
    axs[0,1].grid()

# third figure
def third_signal():
    # third signal
    step = 0.1
    t3 = np.arange(-2, 7, step)
    y3 = 2*(np.exp(-0.9*t3))
    
    # plot the figure
    axs[1, 0].set_title("addition of the signal", fontsize=9)
    axs[1, 0].set_xlabel("time t----->", fontsize=7)
    axs[1, 0].set_ylabel("y(t) = 2e-0.9t", fontsize=7)
    axs[1, 0].plot(t3, y3, color='green')
    axs[1, 0].grid()
    
fig.suptitle("Ploting signal in a single figure") # title of the whole figure

first_signal()
second_signal()
third_signal()

plt.show() # display the graph in a figure