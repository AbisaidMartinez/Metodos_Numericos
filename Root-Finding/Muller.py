# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 02:55:26 2026

@author: qbo28
"""

import numpy as np

def f(x):
    return 16*x**4-40*x**3+5*x**2+20*x+6

def Muller(x0,x1,x2, tol=1e-6, max_iter=1000):
    error = []
    h1 = x1-x0
    h2 = x2-x1
    delta1 = (f(x1)-f(x0))/h1
    delta2 = (f(x2)-f(x1))/h2
    d = (delta2 - delta1)/(h2 + h1)
    i = 3
    
    
    while i <= max_iter:
        b = delta2 + h2*d
        D = (b**2-4*f(x2)*d)**(1/2)

        if np.abs(b-D) < np.abs(b+D):
            E = b+D
        else:
            E = b-D
            
        h =-2*f(x2)/E
        
        error.append(np.abs(h))
        
        p=x2+h
        
        if np.abs(h) < tol:
            return p, i, error
        x0 = x1
        x1 = x2
        x2 = p
        h1 = x1 - x0
        h2 = x2- x1
        delta1 = (f(x1)-f(x0))/h1
        delta2 = (f(x2)-f(x1))/h2
        d = (delta2 - delta1)/(h2 + h1)
        i +=1
    return None, i, error

res, i, error = Muller(0.5,1.0,1.5)

import matplotlib.pyplot as plt

#x = np.linspace(1, i, len(error))

plt.figure()
plt.plot(error)
plt.title("Convergencia metodo de Muller")