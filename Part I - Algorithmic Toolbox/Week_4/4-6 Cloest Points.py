# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 18:49:44 2020

@author: ThinkPadUser
"""
import math
import sys


def distance(point1, point2):
    '''
    point1 = [x1, y1]
    point2 = [x2, y2]
    '''
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def closest(points, start, end):
    if end - start == 1:
        return distance(points[start], points[end])
    if end - start == 2:
        return min(distance(points[start], points[start + 1]), distance(points[start], points[end]), distance(points[start + 1], points[end]))
    
    mid = (start + end) // 2
    d_lower = closest(points, start, mid + 1)
    d_upper = closest(points, mid + 1, end)
    d_min = min(d_lower, d_upper)
    
    tempPoints = sorted(points[start:end+1], key= lambda x: x[1])
    for i in range(len(tempPoints)):
        points[start+i] = tempPoints[i]
        
    line = points[mid + 1][0]
    
    strip = []
    
    for p in points[start:end+1]:
        if abs(line - p[0]) > d_min: continue
        strip.append(p)
    for i in range(len(strip)):
        point = strip[i]
        for j in range(1, 4):
            if i + j >= len(strip): break
            d_min = min(d_min, distance(point, strip[i + j]))
        
    return d_min


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = list(zip(x, y))
    points.sort()
    print('%.8f' % closest(points, 0, n - 1))