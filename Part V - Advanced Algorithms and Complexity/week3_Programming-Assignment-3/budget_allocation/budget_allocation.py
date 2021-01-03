# python3
from sys import stdin


n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
  A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.


def EquisatisfiableSatFormula(A, b):
    clauses = []
    
    for i, coef in enumerate(A):
        coef_clean = [(j, coef[j]) for j in range(m) if 0 != coef[j]]
        l = len(coef_clean)
        
        for x in range(2 ** l):
            currSet = [coef_clean[j] for j in range(l) if 1 == ((x/2**j)%2)//1]
            currSum = 0
            for coeff in currSet:
                currSum += coeff[1]
            if currSum > b[i]:
                clauses.append([-(coeff[0]+1) for coeff in currSet] + [coeff[0]+1 for coeff in coef_clean if not coeff in currSet])
    return clauses

def printEquisatisfiableSatFormula(n, m, A, b):
    clauses = EquisatisfiableSatFormula(A, b)
    
    if len(clauses) == 0:
        clauses.append([1, -1])
        m = 1
        
    print(len(clauses), m)
    for cc in clauses:
        cc.append(0)
        print(' '.join(map(str, cc)))

printEquisatisfiableSatFormula(n, m, A, b)
