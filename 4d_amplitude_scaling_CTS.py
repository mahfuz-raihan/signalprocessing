# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 19:53:43 2022

@author: fuzi
"""

import numpy as np
import matplotlib.pyplot as plt

step = 0.2
t = np.arange(-5, 10, step)

a = float(input("Put the scale: "))

x_t = np.sin(t)
y_t = a*(np.sin(t)) # amplitude scaling

'''
print(t)
print(x_t)
print(y_t)
'''
def original_signal():
    plt.subplot(3,1,1)
    plt.title("Original signal")
    plt.xlabel("time t---->")
    plt.ylabel("x(t)------->")
    plt.plot(t ,x_t, color='red', marker='o')
    plt.grid()

def amplification_signal():
    plt.subplot(3,1,3)
    plt.title("amplification of signal")
    plt.xlabel("time t---->")
    plt.ylabel("y(at)------->")
    plt.plot(t ,y_t, color='green', marker='x')
    plt.grid()

def reduction_singnal():
    plt.subplot(3,1,3)
    plt.title("reduction of signal")
    plt.xlabel("time t---->")
    plt.ylabel("y(at)------->")
    plt.plot(t ,y_t, color='green', marker='x')
    plt.grid()

if a > 1:
    original_signal()
    amplification_signal()
elif -1 < a < 0 or 0 < a < 1:
    original_signal()
    reduction_singnal()

plt.suptitle('Amplitude scaling of CTS', color = 'm', fontsize=12)
plt.show()
