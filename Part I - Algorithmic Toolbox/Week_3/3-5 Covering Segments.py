# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:52:44 2020

@author: ThinkPadUser
"""
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def covering_segments(segments):
    segments.sort(key = lambda x: x.end, reverse = True)
    res = []
    
    point = 0
    
    while len(segments) != 0:
        base_segment = segments.pop()
        point = base_segment.end
        while (len(segments) != 0) and (segments[-1].start <= point):
            segments.pop()
        if point not in res:
            res.append(point)
    
    res.sort()
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = covering_segments(segments)
    print(len(points))
    for point in points:
        print(point, end = ' ')