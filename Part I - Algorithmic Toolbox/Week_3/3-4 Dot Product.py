# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:52:44 2020

@author: ThinkPadUser
"""
import sys


def dot_product(a, b):
    a.sort()
    b.sort()
    
    res = 0
    for _ in range(len(a)):
        res += a[_] * b[_]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:n+1]
    b = data[n+1:]
    print(dot_product(a, b))