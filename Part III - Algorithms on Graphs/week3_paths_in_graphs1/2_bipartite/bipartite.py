#Uses python3

import sys
import queue

def bipartite(adj):
    #write your code here
    visited = [ None for _ in range(len(adj)) ]
    q = queue.Queue()
    for i in range(len(adj)):
        if visited[i] is None:
            visited[i] = True
            q.put(i)
            while not q.empty():
                x = q.get()
                value = visited[x]
                for v in adj[x]:
                    if visited[v] is None:
                        q.put(v)
                        visited[v] = not value
                    elif visited[v] == value:
                        return 0    
    return 1

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
    print(bipartite(adj))
