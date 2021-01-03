# python3
import itertools


n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.

positions = range(1, n + 1) # 3 different colors
clauses = []

def convert(i, j):
    return n * i + j

def exactly_one_of(literals):
    """
    returns exactly one of iterable in CNF form as a list of strings.
    """
    clauses.append([l for l in literals])
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

def get_adjacent(n, edges):
    adj = [[] for _ in range(n)]
    for i, j in edges:
        adj[i - 1].append(j - 1)
        adj[j - 1].append(i - 1)
    return adj

def printEquisatisfiableSatFormula():
    adj = get_adjacent(n, edges)
    
    for i in range(1, n):
        exactly_one_of([convert(i, j) for j in positions])
    
    for j in positions:
        exactly_one_of([convert(i, j) for i in range(n)])
    
    for j in positions[:-1]:
        for i, nodes in enumerate(adj):
            clauses.append([-convert(i, j)] + [convert(n, j + 1) for n in nodes])

    print(len(clauses), n * n)
    for c in clauses:
        c.append(0)
        print(' '.join(map(str, c)))

printEquisatisfiableSatFormula()
