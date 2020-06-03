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

	
def fibonacci_sum_of_squares(n):
    if n <= 1:
	    return n
	
    n, m = n % 60, (n+1) % 60
	
    return (fibonacci_last_digit(n) * fibonacci_last_digit(m)) % 10
	
	
	
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_of_squares(n))