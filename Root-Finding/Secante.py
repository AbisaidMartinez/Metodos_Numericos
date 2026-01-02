# -*- coding: utf-8 -*-
"""
Created on Thu Jan  1 15:27:13 2026

@author: qbo28
"""

import numpy as np

def f(x):
    return x**2#x**2-6#

def secante(a,b, tol=1e-6, max_iter=1000):
    c1 = f(a)
    c2 = f(b)
    error= []
    i=2
    
    while i <= max_iter:
        p = b - c2*(b-a)/(c2-c1)
        error.append(np.abs(p-b))
        if np.abs(p-b) < tol:
            return p, i, error
        i +=1
        a = b 
        c1 = c2
        b = p
        c2 = f(p)
        
      
res, ite,  error = secante(3,2)#-5,10)        
     
import matplotlib.pyplot as plt

plt.figure()
plt.plot(error)
plt.title("Convergencia del metodo de la secante")
plt.xlabel("iteraciones")
plt.ylabel("Error absoluto")    