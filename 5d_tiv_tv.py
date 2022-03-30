# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 16:18:41 2022

@author: fuzi
"""

import numpy as np
import matplotlib.pyplot as plt


t = np.arange(-5, 20, 0.01)
u = np.heaviside(t, 0.1) - np.heaviside(t-10, 0.1) # [u(t)-u(t-10)]
x = np.cos(t)*u # input signal x(t) = cos(t)[u(t)-u(t-10)]

y = 1 - 2*x*(t-1) # system y(t) = 1-2x(t-1)

'''
x(t-t0) = cos(t-t0)[u(t-t0)-u(t-10-t0)]
time delay, t0 = 4
'''
xd = np.cos(t-4)*(np.heaviside(t-4, 0.1) - np.heaviside(t-14, 0.1))

yds = 1 - 2*xd*(t-4-1)

#
ys = 1- 2*(np.cos(t-4)*(np.heaviside(t-5, 0.1) - np.heaviside(t-15, 0.1)))*(t-5)


fig, axes = plt.subplots(3, 2, constrained_layout=True)


def input_sginal_fig():
    axes[0, 0].plot(t, x, color = 'g')
    axes[0, 0].set_title("input signal x(t)", color = 'm', fontsize=9)
    axes[0, 0].set_xlabel('t -------->', fontsize=7)
    axes[0, 0].set_ylabel('x(t)', fontsize=7)
    axes[0, 0].legend('y', fontsize=7)
    axes[0, 0].grid()

def y_fig():
    axes[0, 1].plot(t, y, color = 'g')
    axes[0, 1].set_title("y(t) = 1-2x(t-1)", color = 'm', fontsize=9)
    axes[0, 1].set_xlabel('t -------->', fontsize=7)
    axes[0, 1].set_ylabel('y(t)', fontsize=7)
    axes[0, 1].legend('y', fontsize=7)
    axes[0, 1].grid()

def ydelay_fig():
    axes[1, 0].plot(t-4, y, color = 'b')
    axes[1, 0].set_title("y(t-t0) = 1-2x(t-t0-1)", color = 'm', fontsize=9)
    axes[1, 0].set_xlabel('t -------->', fontsize=7)
    axes[1, 0].set_ylabel('y(t-t0)', fontsize=7)
    axes[1, 0].legend('y', fontsize=7)
    axes[1, 0].grid()


def xdelay_fig():
    axes[1, 1].plot(t, xd, color='r')
    axes[1, 1].set_title('x(t-t0) = cos(t-t0)[u(t-t0)-u(t-10-t0)]', color='m', fontsize=9)
    axes[1, 1].set_xlabel('t----->', fontsize=7)
    axes[1, 1].set_ylabel('x(t-t0)', fontsize=7)
    axes[1, 1].legend('x', fontsize=7)
    axes[1, 1].grid()

def yds_fig():
    axes[2, 0].plot(t, yds, color='b')
    axes[2, 0].set_title("y'(t) = 1-2x(t-t0)*(t-t0-1)", color='m', fontsize=9)
    axes[2, 0].set_xlabel('t----->', fontsize=7)
    axes[2, 0].set_ylabel('y(t)', fontsize=7)
    axes[2, 0].legend('yd', fontsize=7)
    axes[2, 0].grid()
    

def ys_fig():
    axes[2, 1].plot(t, ys, color='m')
    axes[2, 1].set_title('y(t) = 1-2x(t-t0)*(t-t0-1)', color='m', fontsize=9)
    axes[2, 1].set_xlabel('t----->', fontsize=7)
    axes[2, 1].set_ylabel('y(t)', fontsize=7)
    axes[2, 1].legend('y', fontsize=7)
    axes[2, 1].grid()

input_sginal_fig()
y_fig()
ydelay_fig()
xdelay_fig()
yds_fig()
ys_fig()


plt.suptitle("System verify: Time Inveriant/Time-veriant", color='b', fontsize=11)
plt.show()