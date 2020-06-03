# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:52:44 2020

@author: ThinkPadUser
"""
import sys


def car_fueling(distance, tank, stops):
    if distance <= tank:
        return 0
    
    stops.insert(0, 0)
    stops.append(distance)
    curr_index, next_index = 0, 1
    numRefills = 0
    
    while stops[curr_index] < distance:
        if stops[next_index] == distance and distance - stops[curr_index] <= tank:
            return numRefills
        
        if stops[next_index + 1] - stops[curr_index] > tank:
            curr_index = next_index
            next_index += 1
            numRefills += 1
        else:
            next_index += 1
        if stops[next_index] - stops[curr_index] > tank:
            return -1
    
    
    return numRefills


if __name__ == '__main__':
    input = sys.stdin.read().split()
    d = int(input[0])
    m = int(input[1])
    stops = list(map(int, input))[3:]
    print(car_fueling(d, m, stops))