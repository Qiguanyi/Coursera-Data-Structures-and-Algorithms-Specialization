# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 18:49:44 2020

@author: ThinkPadUser
"""
import sys
from itertools import chain

def points_and_segments(starts, ends, points):
    res = [0] * len(points)
    
    starts = zip(starts, [float('-inf')]*len(starts))
    ends = zip(ends, [float('inf')]*len(ends))
    points = zip(points, range(len(points)))
    
    sorted_list = sorted(chain(starts, ends, points), key = lambda x: (x[0], x[1]))
    stack = []
    
    for i, j in sorted_list:
        # start point
        if j == float('-inf'):
            stack.append(j)
        # end point
        elif j == float('inf'):
            stack.pop()
        # point
        else:
            res[j] = len(stack)
    
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    s, p = data[0], data[1]
    segments_start = data[2:-p:2]
    segments_end = data[3:-p:2]
    points = data[-p:]
    res = points_and_segments(segments_start, segments_end, points)
    for _ in res:
        print(_, end = ' ')