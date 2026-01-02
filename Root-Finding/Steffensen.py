# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 01:50:31 2026

@author: qbo28
"""

import numpy as np

def g(x):
    return np.sqrt(10/(x+4))

def Steffensen(p0, tol=1e-6, max_iter=1000):
    i = 1
    error = []
    while i <= max_iter:
        p1 = g(p0)
        p2 = g(p1)
        p = p0 - (p1-p0)**2/(p2-2*p1+p0)
        error.append(np.abs(p-p0))
        if np.abs(p-p0) < tol:
            return p, i, error
        i+=1
        p0 = p
    return None, i, error

res, i, error = Steffensen(1.5)

import matplotlib.pyplot as plt

x = np.linspace(1, 3, len(error))

plt.figure()
plt.plot(x,error)
plt.title("Convergencia metodo de Steffensen")