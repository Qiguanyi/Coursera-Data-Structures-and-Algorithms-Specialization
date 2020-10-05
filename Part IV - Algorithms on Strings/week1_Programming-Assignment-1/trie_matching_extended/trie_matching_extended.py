# python3
import sys


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
                tree[parent][c] = [False, child]
                child += 1
            if i == len(pattern) - 1:
                tree[parent][c][0] = True
            parent = tree[parent][c] [1]
    return tree

def prefix_trie_matching(text, trie):
    i, v = 0, 0
    s = text[i]
    while True:
        if trie.get(v, None) == None:
            return True
        elif trie[v].get(s, None) != None:
            if trie[v][s][0]:
                return True
            i += 1
            if i >= len(text):
                return None
            v, s = trie[v][s][1], text[i]
        else:
            return None

def solve (text, n, patterns):
    result = []

	## write your code here
    tree = build_trie(patterns)    
    for i in range(len(text)):
        is_match = prefix_trie_matching(text[i:], tree)
        if is_match:
            result.append(i)
    return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
