# python3
import sys

def solve (p, q):
    p_len = len(p)
    q_len = len(q)
    for i in range(min(p_len, q_len)):
        for j in range(p_len - i):
            substring = p[j: j+i+1]
            if substring not in q:
                return substring
    return


p = sys.stdin.readline ().strip ()
q = sys.stdin.readline ().strip ()

ans = solve (p, q)

sys.stdout.write (ans + '\n')
