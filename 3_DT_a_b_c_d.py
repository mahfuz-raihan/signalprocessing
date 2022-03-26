# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 20:16:01 2022

@author: fuzi
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as ss
%matplotlib inline



fig, axs = plt.subplots(2, 2, constrained_layout=True)


# first figure
def first_signal():
    # first signal
    alpha = 1
    t1 = np.arange(-5, 10, alpha)
    y1 = []
    for i in range(len(t1)):
        count = (1 if t1[i] >=0 else 0)
        y1.append(count)
    
    # plot the figure
    axs[0,0].stem(t1, y1)
    axs[0,0].set_xlabel("Time t-------->", fontsize=7)
    axs[0,0].set_ylabel("u(t)----->", fontsize=7)
    axs[0,0].set_title("unit step signal", fontsize=9)
    axs[0,0].grid()

# second figure
def second_signal():
    # second signal
    alpha = 1
    t2 = np.arange(-10, 11, alpha)
    y2 = []
   
    for i in range(len(t2)):
        count = (1 if t2[i]== 0 else 0)
        y2.append(count)
    
    #print(t2)
    #print(y2)
    
    axs[0,1].stem(t2, y2)
    axs[0,1].set_xlabel('time t ----->', fontsize=7)
    axs[0,1].set_ylabel('d(t)---->', fontsize=7)
    axs[0,1].set_title('unit impulse signal', fontsize=9)
    
    


# third figure
def third_signal():
    # third signal
    t3 = np.arange(-10,11)
    c = 0
    #m = np.tan(45)
    y3 = []
    
    for i in range(len(t3)):
        count = 0 if t3[i]<0 else t3[i]
        y3.append(count)
        
    # plot the figure
    axs[1, 0].set_title("Ramp signal", fontsize=9)
    axs[1, 0].set_xlabel("time t----->", fontsize=7)
    axs[1, 0].set_ylabel("y(t)---->", fontsize=7)
    axs[1, 0].stem(t3, y3)
    axs[1, 0].grid()
    
# fourth figure
def fourth_signal():
    # fourth signal
    step = 1
    pi = np.pi
    t4 = np.arange(-10, 11, step) # time
    A = 3 # amplitude
    T = 5
    f = 1/T # frequency
    w0 = 2*pi*f # omega w = 2pif

    y0 = A*(np.sin(w0*t4)) # y = A*sin(wt), sinusoidal signal
    y4 = ss.square(y0, duty= 0.7)
    
    
    # plot the figure
    axs[1, 1].set_title("Sinusodial periodic signal", fontsize=9)
    axs[1, 1].set_xlabel("time t----->", fontsize=7)
    axs[1, 1].set_ylabel("y(t) = sqr(Asin(wt))", fontsize=7)
    axs[1, 1].stem(t4, y4)
    # axs[1, 1].ylim(-2, 2)
    axs[1, 1].grid()

fig.suptitle("Discreate time signal generator") # title of the whole figure

first_signal()
second_signal()
third_signal()
fourth_signal()


plt.show() # display the graph in a figure