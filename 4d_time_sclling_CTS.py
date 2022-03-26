# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 18:36:02 2022

@author: fuzi
"""

import numpy as np
import matplotlib.pyplot as plt


step = 0.2
t = np.arange(-5, 10, step)

a = float(input("Put the time : "))

x_t = np.sin(t)
y_t = np.sin(a*t) # time compression/expansion
# y_t2 = a*(np.sin(t))

def original_signal():
    plt.subplot(3,1,1)
    plt.title("Original signal")
    plt.xlabel("time t---->")
    plt.ylabel("x(t)------->")
    plt.plot(t ,x_t, color='red', marker='o')
    plt.grid()

def compression_signal():
    plt.subplot(3,1,3)
    plt.title("Compression of signal")
    plt.xlabel("time t---->")
    plt.ylabel("y(at)------->")
    plt.plot(t ,y_t, color='green', marker='x')
    plt.grid()

def expand_singnal():
    plt.subplot(3,1,3)
    plt.title("Expansion of signal")
    plt.xlabel("time t---->")
    plt.ylabel("y(at)------->")
    plt.plot(t ,y_t, color='green', marker='x')
    plt.grid()

if a > 1:
    original_signal()
    compression_signal()
elif -1 < a < 0 or 0 < a < 1:
    original_signal()
    expand_singnal()

plt.suptitle('Time scaling of CTS', color = 'blue', fontsize=12)
plt.show()