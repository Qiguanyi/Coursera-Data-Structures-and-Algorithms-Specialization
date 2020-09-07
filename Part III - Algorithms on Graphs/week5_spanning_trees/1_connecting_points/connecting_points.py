#Uses python3
import sys
import math
import queue

def distance(x1, x2, y1, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def minimum_distance(x, y):
    result = 0.
    #write your code here
    n = len(x)
    distances = [float('inf')] * n
    distances[0] = 0
    Q = queue.PriorityQueue()
    Q.put((0, 0))
    visited = set()
    while not Q.empty():
        d, i = Q.get()
        if i not in visited:
            result += d
            visited.add(i)
            for j in range(n):
                if j not in visited:
                    dist = distance(x[i], x[j], y[i], y[j])
                    if distances[j] > dist:
                        distances[j] = dist
                        Q.put((dist, j))
    
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
