# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:52:06 2020

@author: ThinkPadUser
"""

import sys


def lcs3(a, b, c):
    n = len(a) + 1
    m = len(b) + 1
    l = len(c) + 1
    
    res = [[[0] * l for _ in range(m)] for x in range(n)]
    
    for i in range(1, n):
        for j in range(1, m):
            for k in range(1, l):
                if a[i-1] == b[j-1] and a[i-1] == c[k-1]:
                    res[i][j][k] = 1 + res[i-1][j-1][k-1]
                else:
                    res[i][j][k] = max(max(max(max(max(res[i-1][j][k], res[i][j-1][k]), 
                       res[i][j][k-1]), res[i-1][j-1][k]), res[i-1][j][k-1]), res[i][j-1][k-1])

    return int(res[n-1][m-1][l-1])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1: n + 1]
    
    m = data[n + 1]
    b = data[n + 2: n + m + 2]
    
    l = data[n + m + 2]
    c = data[-l:]
    
    print(lcs3(a, b, c))