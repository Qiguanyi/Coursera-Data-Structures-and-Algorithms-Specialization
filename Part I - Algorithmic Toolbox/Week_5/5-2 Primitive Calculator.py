# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:52:06 2020

@author: ThinkPadUser
"""

import sys


def primitive_calculator(n):
    res = []
    temp = [0] * (n + 1)
    
    for i in range(1, n+1):
        temp[i] = temp[i-1] + 1
        if i % 2 == 0:
            temp[i] = min(temp[i // 2] + 1, temp[i])
        if i % 3 == 0:
            temp[i] = min(temp[i // 3] + 1, temp[i])
    
    while n >= 1:
        res.append(n)
        if temp[n] == temp[n-1] + 1:
            n -= 1
        elif n % 2 == 0 and temp[n // 2] == temp[n] - 1:
            n //= 2
        elif n % 3 == 0 and temp[n // 3] == temp[n] - 1:
            n //= 3
    
    return list(reversed(res))


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    res = primitive_calculator(n)
    print(len(res) - 1)
    for _ in res:
        print(_, end = ' ')