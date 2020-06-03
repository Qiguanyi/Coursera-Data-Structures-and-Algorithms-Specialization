# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:52:44 2020

@author: ThinkPadUser
"""
import sys


def fractional_knapsack(capacity, weights, values):
    value = 0.
    ratio = [float(v) / float(w) for v, w in zip(values, weights)]
    for _ in range(len(weights) + 1):
        if capacity == 0:
            return value
        max_weight = max(ratio)
        index = ratio.index(max_weight)
        ratio[index] = -1
        add_capacity = min(capacity, weights[index])
        value += add_capacity * max_weight
        weights[index] -= add_capacity
        capacity -= add_capacity
        
    return value


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[:2]
    values = data[2:(2*n+2):2]
    weights = data[3:(2*n+2):2]
    print('%.10f' % fractional_knapsack(capacity, weights, values))