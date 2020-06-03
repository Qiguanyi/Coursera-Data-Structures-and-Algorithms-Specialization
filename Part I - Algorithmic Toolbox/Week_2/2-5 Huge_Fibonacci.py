# -*- coding: utf-8 -*-
"""
Created on Sun May 31 23:34:01 2020

@author: ThinkPadUser
"""
import sys


def fibonacci_period(m):
    result = 2;
    fn2 = 1
    fn1 = 2%m
    fn = 3%m
    while fn1 != 1 or fn != 1:
        result += 1
        fn2 = fn1
        fn1 = fn
        fn = (fn1 + fn2)%m
    return result


def fibonacci(n):
    if n <= 1:
        return n
    res = [0, 1]
	
    for i in range(2, n + 1):
	    res.append(res[i-1] + res[i-2])
    
    return res[n]


def huge_fibonacci(n, m):
    if n > 4:
        period = fibonacci_period(m)
        return fibonacci(n % period) % m
    
    return fibonacci(n) % m


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(huge_fibonacci(n, m))