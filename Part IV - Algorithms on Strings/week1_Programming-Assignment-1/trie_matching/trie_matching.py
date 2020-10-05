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
                tree[parent][c] = child
                child += 1
            parent = tree[parent][c]    
    return tree

def prefix_trie_matching(text, trie):
    i, v = 0, 0
    s = text[i]
    while True:
        if trie.get(v, None) == None:
            return text[:v]
        elif trie[v].get(s, None) != None:
            i += 1
            v = trie[v][s]
            if i < len(text):
                s = text[i]
            elif i > len(text):
                return None
        else:
            return None

def solve (text, n, patterns):
    result = []
    tree = build_trie(patterns)    
    for i in range(len(text)):
        pattern = prefix_trie_matching(text[i:], tree)
        if pattern != None:
            result.append(i)
    return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
