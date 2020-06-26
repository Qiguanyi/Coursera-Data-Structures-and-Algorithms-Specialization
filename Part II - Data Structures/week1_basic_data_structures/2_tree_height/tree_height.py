# python3

import sys
import threading
from collections import defaultdict, deque


def compute_height(n, parents):
    # Replace this code with a faster implementation
#    max_height = 0
#    for vertex in range(n):
#        height = 0
#        current = vertex
#        while current != -1:
#            height += 1
#            current = parents[current]
#        max_height = max(max_height, height)
#    return max_height
    tree = defaultdict(list)
    for node, parent in enumerate(parents):
        tree[parent].append(node)
    stack = deque()
    stack.append((tree[-1][0], 1))
    max_level = 0
    while len(stack) > 0:
        node, level = stack.popleft()
        max_level = max(level, max_level)
        for child in tree[node]:
            stack.append((child, level + 1))
    
    return max_level


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
