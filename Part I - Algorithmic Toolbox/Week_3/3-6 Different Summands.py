# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:52:44 2020

@author: ThinkPadUser
"""
import sys


def different_summands(n):
    res = []
    i, sum_summand = 1, 0
    while sum_summand <= n:
        if (sum_summand + i) <= n:
            res.append(i)
            sum_summand += i
        else:
            res[-1] += n - sum_summand
            break
        i += 1
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = different_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end = ' ')