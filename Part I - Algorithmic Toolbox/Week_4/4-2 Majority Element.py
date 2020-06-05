# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 18:49:44 2020

@author: ThinkPadUser
"""

import sys


def majority_element(a):
    min_count = int(len(a) / 2)
    dict = {}
    
    for _ in a:
        if _ in dict:
            dict[_] += 1
        else:
            dict[_] = 1
    for key in dict.keys():
        if dict[key] > min_count:
            return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(majority_element(a))