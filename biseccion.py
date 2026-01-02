# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 17:31:48 2025

@author: qbo28
"""

import numpy as np

#Definir la funcion a encontrar sus raices
def function(x):
    return np.cos(x)

#Metodo de bisección
def biseccion(a,b, tol=1e-6, iteraciones=1000):
    i=1
    error = []
    fa = function(a)
    while i<=iteraciones:
        p=a+(b-a)/2
        fp = function(p)
        
        if(fp == 0) or (b-a)/2<tol:
            return p, i, error
        else:
            error.append((b-a)/2)
        i +=1
        if(fa*fp > 0):
            a = p
        else:
            b = p

    
p0, N, error = biseccion(-3,3)

import matplotlib.pyplot as plt

plt.figure()
plt.plot(error)
plt.title("convergencia de error en metodo de bisección")