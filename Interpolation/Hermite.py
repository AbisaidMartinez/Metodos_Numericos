# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 16:42:12 2026

@author: qbo28
"""

import numpy as np

def Hermite(x_values, y_values, x_diff, x_interp):
    n=len(x_values)
    
    z = np.zeros(2*n)
    Q = np.zeros((2*n,2*n))
    
    for i in range(n):
        z[2*i] = x_values[i]
        z[2*i+1] = x_values[i]
        Q[2*i,0] = y_values[i]
        Q[2*i+1,0] = y_values[i]
        Q[2*i+1,1] = x_diff[i]        
        
        if (i!=0):
            Q[2*i,1] = (Q[2*i,0]-Q[2*i-1,0])/(z[2*i]-z[2*i-1])
            
    for j in range(2,2*n):
        for i in range(j, 2*n):
            Q[i,j] = (Q[i,j-1]-Q[i-1,j-1])/(z[i]-z[i-j])
            
            
    a = np.diag(Q)
    
    y_interp = a[0]
    producto_z = 1.0
    for k in range(1, 2 * n):
        producto_z *= (x_interp - z[k - 1])
        y_interp += a[k] * producto_z
        
    return y_interp
    
x_data = np.array([0, 1, 2, 3])
y_data = np.array([0, 1, 4, 9]) # y = x^2
dy_data = np.array([0, 2, 4, 6], dtype=float)

# Punto a interpolar
x_p = 1.5

# Calcular interpolación
y_interpolated = Hermite(x_data, y_data, dy_data, x_p)
print(f"El valor interpolado en {x_p} es: {y_interpolated}")

    