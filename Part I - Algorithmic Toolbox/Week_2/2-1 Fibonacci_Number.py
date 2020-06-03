# -*- coding: utf-8 -*-
"""
Created on Sun May 31 23:34:01 2020

@author: ThinkPadUser
"""

def Fibonacci(n):
    if n <= 1:
        return n
    
    n0 = 0
    n1 = 1
    
    for _ in range(n-1):
        n0, n1 = n1, n0 + n1
    return n1

n = int(input())
print(Fibonacci(n))