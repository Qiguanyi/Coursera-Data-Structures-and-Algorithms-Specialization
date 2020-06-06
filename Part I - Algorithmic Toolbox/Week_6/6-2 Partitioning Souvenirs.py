# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:55:27 2020

@author: GY
"""
import numpy as np
import sys


def partition3(W, n, weights):
    count = 0
    value = np.zeros((W+1, n+1))
    
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if weights[j-1] <= i:
                temp = value[i-weights[j-1]][j-1] + weights[j-1]
                value[i][j] = max(value[i][j], temp)
            if value[i][j] == W:
                count += 1
    
    return 0 if count < 3 else 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    v = data[1:]
    total_weight = sum(v)
    if n < 3:
        print(0)
    elif total_weight % 3 != 0:
        print(0)
    else:
        print(partition3(total_weight // 3, n, v))