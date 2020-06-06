# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:55:27 2020

@author: GY
"""

import sys
from math import inf

def evalt(a, b, operators):
    if operators == '+':
        return a + b
    elif operators == '-':
        return a - b
    elif operators == '*':
        return a * b
    else:
        assert False


def min_and_max(mins, maxs, operators, i, j):
    tmp_min = inf
    tmp_max = -inf

    for k in range(i, j):
        a = evalt(maxs[i][k], mins[k + 1][j], operators[k])
        b = evalt(mins[i][k], mins[k + 1][j], operators[k])
        c = evalt(maxs[i][k], maxs[k + 1][j], operators[k])
        d = evalt(mins[i][k], maxs[k + 1][j], operators[k])

        tmp_min = min(tmp_min, a, b, c, d)
        tmp_max = max(tmp_max, a, b, c, d)

    return tmp_min, tmp_max



def parentheses(numbers, operators):
    n = len(numbers)
    min_values = [[0] * n for _ in range(n)]
    max_values = [[0] * n for _ in range(n)]
    
    for i in range(n):
        min_values[i][i] = int(numbers[i])
        max_values[i][i] = int(numbers[i])
    
    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            min_values[i][j], max_values[i][j] = min_and_max(min_values, max_values, operators, i, j)
    
    return int(max_values[0][n - 1])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(input)
    operators = data[1::2]
    numbers = data[::2]
    print(parentheses(numbers, operators))