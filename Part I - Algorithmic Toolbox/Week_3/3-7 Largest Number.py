# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:52:44 2020

@author: ThinkPadUser
"""
import sys


def is_greater(digit, max_digit):
    '''
    digit: string
    max_digit: string
    '''
    return digit + max_digit > max_digit + digit


def largest_number(digits):
    '''
    digits: list(string)
    '''
    res = ''
    while len(digits) != 0:
        max_digit = '0'
        for d in digits:
            if is_greater(d, max_digit):
                max_digit = d
        res += max_digit
        digits.remove(max_digit)
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    digits = data[1:]
    print(largest_number(digits))
    