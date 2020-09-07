#Uses python3

import sys


def explore(adj, x, v):
    if v[x][0] == 1:
        if v[x][1] == 0:
            return 1
    else:
        v[x][0] = 1
        for i in adj[x]:
            if explore(adj, i, v) == 1:
                return 1
        v[x][1] = 1
    return 0

def acyclic(adj):
    visited = [[0, 0] for _ in range(len(adj))]
    for i in range(len(adj)):
        if visited[i][0] == 0:
            visited[i][0] = 1
            for j in adj[i]:
                if explore(adj, j, visited) == 1:
                    return 1
            visited[i][1] = 1
    
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
