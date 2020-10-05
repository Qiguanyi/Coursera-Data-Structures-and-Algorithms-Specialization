# python3
import sys


nodes = []

class Node(object):
  
    def __init__(self, label):
        self.label = label
        self.out = {}

def suffix_tree(text):
    root = Node(None)
    root.out[text[0]] = Node(text)
    if root.out[text[0]] not in nodes:
        nodes.append(root.out[text[0]])
    for i in range(1, len(text)):
        currNode = root
        j = i
        while j < len(text):
            if text[j] in currNode.out:
                child = currNode.out[text[j]]
                label = child.label
                k = j + 1
                while k - j < len(label) and text[k] == label[k - j]:
                    k += 1
                if k - j == len(label):
                    currNode = child
                    j = k
                else:
                    currSymbol, newSymbol = label[k - j], text[k]
                    mid = Node(label[:k - j])
                    if mid not in nodes:
                        nodes.append(mid)
                        mid.out[newSymbol] = Node(text[k:])
                    if mid.out[newSymbol] not in nodes:
                        nodes.append(mid.out[newSymbol])
                    mid.out[currSymbol] = child
                    child.label = label[k-j:]
                    currNode.out[text[j]] = mid
                    break
            else:
                currNode.out[text[j]] = Node(text[j:])
                if currNode.out[text[j]] not in nodes:
                    nodes.append(currNode.out[text[j]])
    return nodes

def build_suffix_tree(text):
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
  result = []
  # Implement this function yourself
  tree = suffix_tree(text)
  for s in tree:
      result.append(s.label)
  
  return result


if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))