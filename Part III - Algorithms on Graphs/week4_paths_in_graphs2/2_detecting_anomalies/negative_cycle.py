#Uses python3

import sys


def relax(adj, dist, cost):
    relaxed = False
    for u in range(len(adj)):
        for i, v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                relaxed = True

    return relaxed


def negative_cycle(adj, cost):
    n = len(adj)
    adj.append(range(n))
    cost.append([0] * n)
    dist = [float('inf')] * (n + 1)
    dist[n] = 0
    for _ in range(n):
        if not relax(adj, dist, cost):
            return 0
        
    if relax(adj, dist, cost):
        return 1
    
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
