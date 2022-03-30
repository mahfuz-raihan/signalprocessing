# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:07:12 2022

@author: fuzi
"""

import numpy as np
import matplotlib.pyplot as plt


t = np.arange(-3,3, 0.01)
x1 = np.heaviside(t, 0.5) - np.heaviside(t-1, 0.5) # x1(t) = u(t) - u(t-1)
x2 = np.heaviside(t, 0.5) - np.heaviside(t-2, 0.5) # x2(t) = u(t) - u(t-2)
a1, a2 = 2, 3

z = a1*x1 + a2*x2 # S{a1*x1(t) + a2*x2(t)}
y = 2*z # y(t) = 2*z(t)

z1 = 2*x1 # S{x1(t)}
z2 = 2*x2 # S{x2(t)}
y1 = a1*z1 + a2*z2 # a1S{x1(t)} + a2S{x2(t)}


# examin the y(t) = x^2(t)
y3 = z**2 # y(t) = [a1*x1 + a2*x2]^2(t)

z3 = x1**2 # y(t) = x1^2(t)
z4 = x2**2 # x2^2(t)
y4 = a1*z3 + a2*z4 # a1S{x1(t)} + a2S{x2(t)}

fig, axes = plt.subplots(2, 2, constrained_layout=True)

def y_fig():
    axes[0, 0].plot(t, y, color = 'g')
    axes[0, 0].set_title("For y(t)= 2*x(t)", color = 'm', fontsize=9)
    axes[0, 0].set_xlabel('t -------->', fontsize=7)
    axes[0, 0].set_ylabel('y(t)=2*(a1*x1 + a2*x2)', fontsize=7)
    axes[0, 0].legend('y', fontsize=7)
    axes[0, 0].grid()

def y1_fig():
    axes[0, 1].plot(t, y1, color = 'r')
    axes[0, 1].set_title("For y(t)= 2*x(t) y1", color = 'm', fontsize=9)
    axes[0, 1].set_xlabel('t -------->', fontsize=7)
    axes[0, 1].set_ylabel('y(t)= a1S{x1(t)} + a2S{x2(t)}', fontsize=7)
    axes[0, 1].legend('y', fontsize=7)
    axes[0, 1].grid()

def y3_fig():
    axes[1, 0].plot(t, y3, color = 'r')
    axes[1, 0].set_title("y(t) = x^2(t) system graph", color = 'm', fontsize=9)
    axes[1, 0].set_xlabel('t -------->', fontsize=7)
    axes[1, 0].set_ylabel('y(t)=2*(a1*x1 + a2*x2)', fontsize=7)
    axes[1, 0].legend('y1', fontsize=7)
    axes[1, 0].grid()

def y4_fig():
    axes[1, 1].plot(t, y4, color = 'g')
    axes[1, 1].set_title("y(t) = x^2(t) system graph", color = 'm', fontsize=9)
    axes[1, 1].set_xlabel('t -------->', fontsize=7)
    axes[1, 1].set_ylabel('y(t)= a1S{x1(t)} + a2S{x2(t)}', fontsize=7)
    axes[1, 1].legend('r', fontsize=7)
    axes[1, 1].grid()

plt.suptitle('Verification of the system(Linear/Non-linear)',color = 'b', fontsize=11)

y_fig()
y1_fig()
y3_fig()
y4_fig()

plt.show()