# python3
from collections import deque


def max_sliding_window_fast(sequence, m):
#    maximums = []
#    for i in range(len(sequence) - m + 1):
#        maximums.append(max(sequence[i:i + m]))
    dq = deque()
    
    for i in range(m):
        while dq and sequence[i] >= sequence[dq[-1]]:
            dq.pop()
        dq.append(i)
    for i in range(m, n):
        print(sequence[dq[0]], end = " ")
        while dq and dq[0] <= i - m:
            dq.popleft()
        while dq and sequence[i] >= sequence[dq[-1]]:
            dq.pop()
        dq.append(i)
    print(sequence[dq[0]])

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    max_sliding_window_fast(input_sequence, window_size)

