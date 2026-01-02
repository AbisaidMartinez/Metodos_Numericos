# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 03:45:55 2026

@author: qbo28
"""

import numpy as np

def Neville(x_values, y_values, x_interp):
    n = len(x_values)
    Q = np.zeros((n,n))
    
    for i in range(n):
        Q[i, 0] = y_values[i]
    
    for j in range(1,n):
        for i in range(n-j):
            Q[i,j] = ((x_interp - x_values[i+j]) * Q[i, j-1] - 
                       (x_interp - x_values[i]) * Q[i+1, j-1]) / (x_values[i] - x_values[i+j])
            
    return Q[0, n-1]

x_data = np.array([0, 1, 2, 3])
y_data = np.array([0, 1, 4, 9]) # y = x^2

# Punto a interpolar
x_p = 1.5

# Calcular interpolación
y_interpolated = Neville(x_data, y_data, x_p)
print(f"El valor interpolado en {x_p} es: {y_interpolated}")

import matplotlib.pyplot as plt

x_plot = np.linspace(min(x_data), max(x_data), 100)
y_plot = [Neville(x_data, y_data, x) for x in x_plot]

plt.plot(x_data, y_data, 'o', label='Puntos originales')
plt.plot(x_plot, y_plot, '-', label='Polinomio de Neville')
plt.plot(x_p, y_interpolated)
plt.title("Comparativa entre puntos y polinomio de Neville")
plt.legend()