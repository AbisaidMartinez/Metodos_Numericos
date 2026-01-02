# -*- coding: utf-8 -*-
"""
Created on Thu Jan  1 01:29:09 2026

@author: qbo28
"""
import sympy as sp
import numpy as np

def f(x):
    return x**2

def df_numerica(func, x, h=1e-6):
    '''
    Parameters
    ----------
    func : Derivada numerica centrada.
    x : Variable.
    h : Infinitesimal 1e-6.

    Returns Derivada de la funcion

    '''
    return (func(x + h) - func(x - h)) / (2 * h)


def Newton(x0, tol=1e-6, max_iter=1000):
    i=1
    error = []
    while i<= max_iter:
        dfx = df_numerica(f, x0) # Usando derivada numérica
        p = x0 - f(x0)/dfx
        error.append(np.abs(p-x0))
        if np.abs(p-x0) < tol:
            return p, error
        i+= 1
        x0 = p
        
x, error = Newton(-5)
import matplotlib.pyplot as plt

plt.figure()
plt.plot(error)
plt.title("Convergencia metodo de Newton")
