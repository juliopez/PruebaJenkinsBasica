# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dCC_I5Uv0dZI5e6K-nBZuwWbGhc3aTLw
"""
print ("Hola")
def sum(a, b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
    return a + b