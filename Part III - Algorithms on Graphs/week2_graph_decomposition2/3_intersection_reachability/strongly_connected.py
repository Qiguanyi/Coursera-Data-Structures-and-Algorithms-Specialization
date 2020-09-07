#Uses python3

import sys

sys.setrecursionlimit(200000)


def explore(adj, used, order, x):
    if used[x][0] == 0:
        used[x][0] = 1
        for i in adj[x]:
            explore(adj, used, order, i)
        used[x][1] = 1
        order.append(x)


# DFS(GR)
def ordering(adj):
    used = [[0, 0] for _ in range(len(adj))]
    order = []
    for i in range(len(adj)):
        explore(adj, used, order, i)
    return order


def connected(adj, x, v):
    for i in adj[x]:
        if v[i] == 0:
            v[i] = 1
            connected(adj, i, v)


def number_of_strongly_connected_components(adj, order):
    result = 0
    #write your code here
    visited = [0 for _ in range(len(adj))]
    for i in range(len(adj)):
        x = order.pop()
        if visited[x] == 0:
            result += 1
            visited[x] = 1
            connected(adj, x, visited)
    
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adj_reversed = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj_reversed[b-1].append(a - 1)
    order = ordering(adj_reversed)
    print(number_of_strongly_connected_components(adj, order))
