# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:52:06 2020

@author: ThinkPadUser
"""
import numpy as np
import sys


def lcs2(a, b):
    res = np.zeros((len(a) + 1, len(b) + 1))
    
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                res[i, j] = res[i-1, j-1] + 1
            else:
                res[i, j] = max(res[i-1][j-1], res[i-1][j], res[i][j-1])
    
    return int(res[len(a)][len(b)])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:n+1]
    
    m = data[n+1]
    b = data[-m:]
    print(lcs2(a, b))