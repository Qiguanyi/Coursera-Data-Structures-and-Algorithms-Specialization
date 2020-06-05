# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 18:49:44 2020

@author: ThinkPadUser
"""
import random
import sys


def partition_3(a, left, right):
    x = a[left]
    i, j = left, left + 1
    while j <= right:
        if a[j] == x:
            j += 1
        elif a[j] < x:
            a[i], a[j] = a[j], a[i]
            i += 1
            j += 1
        else:
            a[j], a[right] = a[right], a[j]
            right -= 1
    
    return i, right
    
    
def sorting(a, left, right):
    if left >= right:
        return
    k = random.randint(left, right)
    a[left], a[k] = a[k], a[left]
    lower, upper = partition_3(a, left, right)
    sorting(a, left, lower - 1)
    sorting(a, upper + 1, right)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    sorting(a, 0, n - 1)
    for _ in a:
        print(_, end = ' ')