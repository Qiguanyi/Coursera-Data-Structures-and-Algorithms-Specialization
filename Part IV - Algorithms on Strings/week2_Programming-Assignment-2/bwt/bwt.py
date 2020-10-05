# python3
import sys

def BWT(text):
    matrix = sorted(text[i:]+text[:i] for i in range(len(text)))
    return "".join(row[-1] for row in matrix)

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
