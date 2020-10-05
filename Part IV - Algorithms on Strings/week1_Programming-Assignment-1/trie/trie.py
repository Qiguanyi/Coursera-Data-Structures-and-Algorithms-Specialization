#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    # write your code here
    child = 1
    for pattern in patterns:
        parent = 0
        for i in range(len(pattern)):
            c = pattern[i]
            if tree.get(parent, None) == None:
                tree[parent] = {}
            if tree[parent].get(c, None) == None:
                tree[parent][c] = child
                child += 1
            parent = tree[parent][c]    
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
