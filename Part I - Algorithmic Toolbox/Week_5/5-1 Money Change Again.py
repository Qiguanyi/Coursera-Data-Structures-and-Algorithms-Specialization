# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 17:52:06 2020

@author: ThinkPadUser
"""

import sys


def change_dp(money):
    denominations = [1, 3, 4]
    
    res = [0] + [float('inf')] * money
    for m in range(1, money + 1):
        for coin in denominations:
            if m >= coin:
                temp = res[m - coin] + 1
                if temp < res[m]:
                    res[m] = temp

    return res[money]


if __name__ == '__main__':
    input = sys.stdin.read()
    money = int(input)
    print(change_dp(money))