# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 18:49:44 2020

@author: ThinkPadUser
"""

import sys


def binary_search(a, key):
    left, right = 0, len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == key:
            return mid
        elif a[mid] < key:
            if key == a[left]:
                return left
            left = mid + 1
        else:
            right = mid - 1
        
    return -1


if __name__ == '__main__':
    input = sys.stdin.read().split()
    data = list(map(int, input))
    n = data[0]
    a = data[1:n+1]
    for _ in data[n+2:]:
        print(binary_search(a, _), end = ' ')