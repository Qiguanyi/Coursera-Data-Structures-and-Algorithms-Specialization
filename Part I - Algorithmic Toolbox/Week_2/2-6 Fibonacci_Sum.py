# -*- coding: utf-8 -*-
"""
Created on Sun May 31 23:34:01 2020

@author: ThinkPadUser
"""
import sys


def fibonacci_last_digit(n):
    if n <= 1:
        return n
    
    n0 = 0
    n1 = 1
    
    for _ in range(n - 1):
        n0, n1 = n1 % 10, (n0 + n1) % 10
    
    return n1


def fibonacci_sum_last_digit(n):
    n = (n+2) % 60
    res = fibonacci_last_digit(n)
    if res == 0:
        return 9
	
    return res - 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_last_digit(n))