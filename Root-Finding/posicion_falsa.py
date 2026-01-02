# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 00:42:06 2026

@author: qbo28
"""

import numpy as np

def f(x):
    return x**2-6

def false_pos(p0,p1, tol=1e-6, max_iter=1000):
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    error = []
    while i <= max_iter:
        p = p1-q1*(p1-p0)/(q1-q0)
        
        error.append(np.abs(p-p1))
        
        if np.abs(p-p1) < tol:
            return p, i, error
        
        i +=1
        q = f(p)
        if q*q1 < 0 :
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q
    return None, i, error

res, i, error = false_pos(2,3)

import matplotlib.pyplot as plt

plt.figure()
plt.plot(error)
plt.title("Convergencia metodo posicion falsa")