# python3
import sys

def InverseBWT(bwt):
    # write your code here
    result = [''] * len(bwt)
    count = dict()
    start = {}
    shortcut = []
    for i in range(len(bwt)):
        currPosition = count.get(bwt[i], 0)
        shortcut.append(currPosition)
        count[bwt[i]] = currPosition + 1

    currPosition = 0
    first_col = []
    for char, n in sorted(count.items(), key = lambda x: x[0]):
        first_col += [char] * n
        start[char] = currPosition
        currPosition += n
    
    currPosition = 0
    for i in range(len(bwt)):
        result[len(bwt) - i - 1] = first_col[currPosition]
        currPosition = start[bwt[currPosition]] + shortcut[currPosition]
    
    return "".join(result)


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
