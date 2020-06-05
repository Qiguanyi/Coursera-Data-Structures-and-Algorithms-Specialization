# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 18:49:44 2020

@author: ThinkPadUser
"""

import sys


def merge(a, b, left, mid, right):
    inversions_count = 0
    
    i, j, k = left, mid, left
    
    while i <= mid - 1 and j <= right:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
        else:
            b[k] = a[j]
            j += 1
            inversions_count += mid - i
        k += 1
    
    while i <= mid - 1:
        b[k] = a[i]
        i += 1
        k += 1
        
    while j <= right:
        b[k] = a[j]
        j += 1
        k += 1
    
    for i in range(left, right + 1):
        a[i] = b[i]
    
    return inversions_count


def inversions(a, b, left, right):
    inversions_count = 0
    if right > left:
        mid = (left + right) // 2
        inversions_count += inversions(a, b, left, mid)
        inversions_count += inversions(a, b, mid + 1, right)
        inversions_count += merge(a, b, left, mid + 1, right)
    
    return inversions_count


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = [0] * n
    print(inversions(a, b, 0, n - 1))