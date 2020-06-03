# -*- coding: utf-8 -*-
"""
Created on Sun May 31 23:34:01 2020

@author: ThinkPadUser
"""
import sys


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))