# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 22:02:11 2022

@author: fuzi
"""

import numpy as np
import matplotlib.pyplot as plt


t = np.arange(-7,7, 0.1)
x = np.heaviside(t, 0.5) - np.heaviside(t-1, 0.5)
y = 3*x
y1 = x*(t-1)

#print(x)

fig, axes = plt.subplots(2, 2, constrained_layout=True)

def x_fig():
    axes[0, 0].plot(t, x, color = 'g')
    axes[0, 0].set_title("The signal in a system 'X'", color = 'm', fontsize=9)
    axes[0, 0].set_xlabel('t -------->', fontsize=7)
    axes[0, 0].set_ylabel('x(t)=u(t)-u(t-1)', fontsize=7)
    axes[0, 0].legend('x(t)', fontsize=7)
    axes[0, 0].grid()

def y_fig():
    axes[0, 1].plot(t, y, color = 'r')
    axes[0, 1].set_title("Static system graph y", color = 'm', fontsize=9)
    axes[0, 1].set_xlabel('t -------->', fontsize=7)
    axes[0, 1].set_ylabel('y(t) = 3x(t)', fontsize=7)
    axes[0, 1].legend('y', fontsize=7)
    axes[0, 1].grid()

def y1_fig():
    axes[1, 0].plot(t, y1, color = 'r')
    axes[1, 0].set_title("Dynamic system graph y1", color = 'm', fontsize=9)
    axes[1, 0].set_xlabel('t -------->', fontsize=7)
    axes[1, 0].set_ylabel('y1(t) = x*(t-1)', fontsize=7)
    axes[1, 0].legend('y1', fontsize=7)
    axes[1, 0].grid()


plt.suptitle('Verification of the system(Static/Dynamic)',color = 'r', fontsize=11)
x_fig()
y_fig()
y1_fig()
plt.show()