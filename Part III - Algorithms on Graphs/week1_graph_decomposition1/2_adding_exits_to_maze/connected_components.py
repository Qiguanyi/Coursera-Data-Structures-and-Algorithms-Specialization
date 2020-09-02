#Uses python3

import sys


def visit(adj, x, v):
    v[x] = 1
    for y in adj[x]:
        if v[y] == 0:
            visit(adj, y, v)
    return


def number_of_components(adj):
    result = 0
    #write your code here
    visited = [0 for _ in range(len(adj))]
    
    for i in range(len(adj)):
        if visited[i] == 0:
            result += 1
            visited[i] = 1
            for node in adj[i]:
                if visited[node] == 0:
                    visit(adj, node, visited)
    
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
