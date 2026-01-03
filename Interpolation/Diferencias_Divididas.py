# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 16:40:42 2026

@author: qbo28
"""

import numpy as np

def dif_div(x_values, y_values, x_interp):
    n = len(x_values)
    
    F = np.zeros((n,n))
    A = []
    F[:, 0] = y_values
    
    for j in range(1,n):
        for i in range(j, n):
            F[i,j] = (F[i,j-1]-F[i-1,j-1])/(x_values[i]-x_values[i-j])
    
    a = np.diag(F)
    
    y_interp = a[0]
    producto_x = 1.0
    for k in range(1, n):
        producto_x *= (x_interp - x_values[k-1])
        y_interp += a[k] * producto_x
        
    return y_interp

x_data = np.array([0, 1, 2, 3])
y_data = np.array([0, 1, 4, 9]) # y = x^2

# Punto a interpolar
x_p = 1.5

# Calcular interpolación
y_interpolated = dif_div(x_data, y_data, x_p)
print(f"El valor interpolado en {x_p} es: {y_interpolated}")

import matplotlib.pyplot as plt

x_plot = np.linspace(min(x_data), max(x_data), 100)
y_plot = [dif_div(x_data, y_data, x) for x in x_plot]

plt.plot(x_data, y_data, 'o', label='Puntos originales')
plt.plot(x_plot, y_plot, '-', label='Diferencias divididas')
plt.plot(x_p, y_interpolated)
plt.title("Comparativa entre puntos y polinomio obtenido mediante Diferencias Divididas")
plt.legend()