# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 02:07:05 2026

@author: qbo28
"""

def Horner(n, elementos, x0):
    y = elementos[-1]
    
    for j in range(n-2,-1,-1): #recorrer hacia atras
        y = elementos[j] + x0*y
        
    return y

coef = [2, 3, 1]
valor = Horner(len(coef), coef, 5)


