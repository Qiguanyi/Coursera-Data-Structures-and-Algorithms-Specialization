# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:55:27 2020

@author: GY
"""

import sys


def knapsack(capacity, weight):
    res = [[0] * (capacity + 1) for _ in range(len(weight) + 1)]
    
    for i in range(1, len(weight) + 1):
        for j in range(1, capacity + 1):
            if weight[i-1] > j:
                res[i][j] = res[i-1][j]
            else:
                res[i][j] = max(weight[i-1] + res[i-1][j-weight[i-1]], res[i-1][j])
    
    return int(res[len(weight)][capacity])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    capacity = data[0]
    n = data[1]
    weight = data[2:]
    print(knapsack(capacity, weight))