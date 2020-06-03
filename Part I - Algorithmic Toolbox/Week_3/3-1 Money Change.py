# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:52:44 2020

@author: ThinkPadUser
"""
import sys

def money_change(m):
    return (m // 10) + ((m % 10) // 5) + (m % 10 % 5)

if __name__ == '__main__':
    input = sys.stdin.read()
    m = int(input)
    print(money_change(m))