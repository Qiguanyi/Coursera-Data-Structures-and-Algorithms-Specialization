# python3
import sys


class SuffixTreeNode:
    def __init__(self, children, parent, stringDepth, edgeStart, edgeEnd):
        self.children = children
        self.parent = parent
        self.stringDepth = stringDepth
        self.edgeStart = edgeStart
        self.edgeEnd = edgeEnd

def createNewLeaf(node, text, suffix):
    leaf = SuffixTreeNode(dict(), node, len(text)-suffix, suffix+node.stringDepth, len(text)-1)
    node.children[text[leaf.edgeStart]] = leaf
    #print(node.id, node.edgeStart, S[node.edgeStart], node.children.items())
    return leaf

def breakEdge(node, text, start, offset):
    startChar = text[start]
    midChar = text[start + offset]
    
    midNode = SuffixTreeNode(dict(), node, node.stringDepth + offset, start, start + offset - 1)
    midNode.children[midChar] = node.children[startChar]
    node.children[startChar].parent = midNode
    node.children[startChar] = midNode
    midNode.children[midChar].edgeStart += offset
    return midNode


def suffix_array_to_suffix_tree(sa, lcp, text):
    """
    Build suffix tree of the string text given its suffix array suffix_array
    and LCP array lcp_array. Return the tree as a mapping from a node ID
    to the list of all outgoing edges of the corresponding node. The edges in the
    list must be sorted in the ascending order by the first character of the edge label.
    Root must have node ID = 0, and all other node IDs must be different
    nonnegative integers. Each edge must be represented by a tuple (node, start, end), where
        * node is the node ID of the ending node of the edge
        * start is the starting position (0-based) of the substring of text corresponding to the edge label
        * end is the first position (0-based) after the end of the substring corresponding to the edge label

    For example, if text = "ACACAA$", an edge with label "$" from root to a node with ID 1
    must be represented by a tuple (1, 6, 7). This edge must be present in the list tree[0]
    (corresponding to the root node), and it should be the first edge in the list (because
    it has the smallest first character of all edges outgoing from the root).
    """
    root = SuffixTreeNode(children = dict(), parent = None, stringDepth = 0, edgeStart = -1, edgeEnd = -1)
    lcpPrev = 0
    currNode = root
    for i in range(len(text)):
        #print(i)
        suffix = sa[i]
        while currNode.stringDepth > lcpPrev:
            currNode = currNode.parent
        if currNode.stringDepth == lcpPrev:
            leaf = createNewLeaf(currNode, text, suffix)
        else:
            edgeStart = sa[i-1] + currNode.stringDepth
            offset = lcpPrev - currNode.stringDepth
            midNode = breakEdge(currNode, text, edgeStart, offset)
            leaf = createNewLeaf(midNode, text, suffix)
        currNode = leaf
        if i < len(text) - 1:
            lcpPrev = lcp[i]
    return root


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    sa = list(map(int, sys.stdin.readline().strip().split()))
    lcp = list(map(int, sys.stdin.readline().strip().split()))
    print(text)
    # Build the suffix tree and get a mapping from 
    # suffix tree node ID to the list of outgoing Edges.
    tree = suffix_array_to_suffix_tree(sa, lcp, text)
    """
    Output the edges of the suffix tree in the required order.
    Note that we use here the contract that the root of the tree
    will have node ID = 0 and that each vector of outgoing edges
    will be sorted by the first character of the corresponding edge label.
    
    The following code avoids recursion to avoid stack overflow issues.
    It uses two stacks to convert recursive function to a while loop.
    This code is an equivalent of 
    
        OutputEdges(tree, 0);
    
    for the following _recursive_ function OutputEdges:
    
    def OutputEdges(tree, node_id):
        edges = tree[node_id]
        for edge in edges:
            print("%d %d" % (edge[1], edge[2]))
            OutputEdges(tree, edge[0]);
    
    """
    stack = [(tree, 0)]
    result_edges = []
    while len(stack) > 0:
      (node, edge_index) = stack[-1]
      stack.pop()
      if len(node.children) == 0:
        continue
      edges = sorted(node.children.keys())
      if edge_index + 1 < len(edges):
        stack.append((node, edge_index + 1))
      print("%d %d" % (node.children[edges[edge_index]].edgeStart, node.children[edges[edge_index]].edgeEnd + 1))
      stack.append((node.children[edges[edge_index]], 0))
