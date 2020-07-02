# python3

import sys


#class Database:
#    def __init__(self, row_counts):
#        self.row_counts = row_counts
#        self.max_row_count = max(row_counts)
#        n_tables = len(row_counts)
#        self.ranks = [1] * n_tables
#        self.parents = list(range(n_tables))
#
#    def merge(self, src, dst):
#        src_parent = self.get_parent(src)
#        dst_parent = self.get_parent(dst)
#
#        if src_parent == dst_parent:
#            return False
#
#        # merge two components
#        # use union by rank heuristic
#        # update max_row_count with the new maximum table size
#        return True
#
#    def get_parent(self, table):
#        # find parent and compress path
#        return self.parents[table]


n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = [max(lines)]
act = {}

def getParent(table):
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]


def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)
    lineRoot = 0

    if realDestination == realSource:
        return False

    if rank[realDestination] > rank[realSource]:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        lineRoot = lines[realDestination]
        lines[realSource] = 0

    elif rank[realDestination] == rank[realSource]:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        lineRoot = lines[realDestination]
        lines[realSource] = 0
        rank[realDestination] += 1

    else:
        parent[realDestination] = realSource
        lines[realSource] += lines[realDestination]
        lineRoot = lines[realSource]
        lines[realDestination] = 0

    if lineRoot > ans[0]:
        ans[0] = lineRoot

    return True


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans[0])
