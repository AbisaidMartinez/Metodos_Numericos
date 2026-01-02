# -*- coding: utf-8 -*-
"""
Created on Wed Dec 31 18:19:40 2025

@author: qbo28
"""
import numpy as np

def fixed_point(x0, tol=1e-6, max_iter=1000):
    """
    Implementa el método de punto fijo para cos(x) = x
    Retorna:
        x_final
    historial de errores
    """
    i = 1
    error = []
    while i<= max_iter:
        gx = np.cos(x0)
        error.append(np.abs(gx-x0))
        if np.abs(gx-x0) < tol:
            return gx, error
        i += 1
        x0 = gx
        
x, error = fixed_point(1)

import matplotlib.pyplot as plt

plt.figure()
plt.plot(error)
plt.title("convergencia de error en metodo de punto fijo")
        
        