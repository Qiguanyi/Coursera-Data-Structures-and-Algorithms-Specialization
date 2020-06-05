# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:52:06 2020

@author: ThinkPadUser
"""
import numpy as np
import sys


def edit_distance(s, t):
    if s == t:
        return 0
    res = np.zeros((len(s) + 1, len(t) + 1))
    res[0] = range(len(t) + 1)
    res[:,0] = range(len(s) + 1)
    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            if s[i - 1] == t[j - 1]:
                res[i, j] = res[i-1, j-1]
            else:
                res[i, j] = 1 + min(res[i-1, j], res[i-1, j-1], res[i, j-1])
    
    return int(res[-1][-1])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(str, input.split()))
    s = data[0]
    t = data[1]
    print(edit_distance(s, t))