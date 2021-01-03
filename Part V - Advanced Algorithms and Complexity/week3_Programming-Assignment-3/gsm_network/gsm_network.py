# python3
import itertools


n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.

colors = range(1, 4) # 3 different colors
clauses = []

def convert(i, k):
    return 3*(i-1) + k

def exactly_one_of(iterable):
    """
    returns exactly one of iterable in CNF form as a list of strings.
    """
    literals = [convert(iterable, k) for k in colors]
    clauses.append([l for l in literals])
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

def get_adjacent(i, j):
    for k in colors:
        clauses.append([-convert(i, k), -convert(j, k)])

def printEquisatisfiableSatFormula():
    for i in range(1, n + 1):
        exactly_one_of(i)
    
    for i, j in edges:
        get_adjacent(i, j)
    
    print(len(clauses), n*3)
    for c in clauses:
        c.append(0)
        print(' '.join(map(str, c)))


printEquisatisfiableSatFormula()
