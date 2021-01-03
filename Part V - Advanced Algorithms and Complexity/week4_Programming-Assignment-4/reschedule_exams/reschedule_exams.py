# python3

from enum import Enum
import collections
import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 26)  # new thread will get stack of such size


# Arguments:
#   * `n` - the number of vertices.
#   * `edges` - list of edges, each edge is a tuple (u, v), 1 <= u, v <= n.
#   * `colors` - list consisting of `n` characters, each belonging to the set {'R', 'G', 'B'}.
# Return value: 
#   * If there exists a proper recoloring, return value is a list containing new colors, similar to the `colors` argument.
#   * Otherwise, return value is None.

class Ordered_Set(collections.MutableSet):

    def __init__(self, iterable = None):
        self.end = end = []
        end += [None, end, end]         # sentinel node for doubly linked list
        self.map = {}                   # key --> [key, prev, next]
        if iterable is not None:
            self |= iterable

    def __len__(self):
        return len(self.map)

    def __contains__(self, key):
        return key in self.map

    def add(self, key):
        if key not in self.map:
            end = self.end
            current = end[1]
            current[2] = end[1] = self.map[key] = [key, current, end]

    def discard(self, key):
        if key in self.map:
            key, prev, next = self.map.pop(key)
            prev[2] = next
            next[1] = prev

    def __iter__(self):
        end = self.end
        current = end[2]
        while current is not end:
            yield current[0]
            current = current[2]

    def __reversed__(self):
        end = self.end
        current = end[1]
        while current is not end:
            yield current[0]
            current = current[1]

    def pop(self, last=True):
        if not self:
            raise KeyError('set is empty')
        key = self.end[1][0] if last else self.end[2][0]
        self.discard(key)
        return key

    def __repr__(self):
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self))

    def __eq__(self, other):
        if isinstance(other, Ordered_Set):
            return len(self) == len(other) and list(self) == list(other)
        return set(self) == set(other)


def post_orders(adjacents):

    def dfs(node, order, traversed):
        traversed.add(node)
        for adj in adjacents[node]:
            if adj in traversed:
                continue
            dfs(adj, order, traversed)
        if node in vertices:
            vertices.remove(node)
        order.add(node)

    post_order = Ordered_Set([])
    traversed = set([])
    vertices = set([node for node in range(len(adjacents))])

    while True:
        dfs(vertices.pop(), post_order, traversed)
        if len(post_order) == len(adjacents):
            break

    assert len(post_order) == len(adjacents)

    return list(post_order)

def connected_component(adjacents, node, found):

    connected = set([])
    def dfs(node, connected):
        connected.add(node)
        found.add(node)
        found.add(node)
        for adj in adjacents[node]:
            if adj in found or adj in connected:
                continue
            dfs(adj, connected)

    dfs(node, connected)
    return connected

def analyse_connected_components(n, adjacents, reverse, var_map):

    order = post_orders(reverse)
    order_pointer = len(order) - 1
    found = set([])
    ccs = []
    while order_pointer >= 0:
        if order[order_pointer] in found:
            order_pointer -= 1
            continue

        ccs.append(connected_component(adjacents, order[order_pointer], found))

    assert len(found) == len(adjacents), 'found {0} nodes, but {1} were specified'.format(len(found), n)
    return ccs
    
def build_implication_graph(n, clauses):

    edges = []
    var_dict =  {}
    node_dict = {}
    node_num = 0
    adjacents = [[] for _ in range(2*n)]
    reversed_adjs = [[] for _ in range(2*n)]

    for clause in clauses:
        left = clause[0]
        right = clause[1]
        for term in [left, right]:
            if not term in node_dict:
                var_dict[node_num] = term
                node_dict[term] = node_num
                node_num += 1
            if not -term in node_dict:
                var_dict[node_num] = -term
                node_dict[-term] = node_num
                node_num += 1

        adjacents[node_dict[-left]].append(node_dict[right])
        reversed_adjs[node_dict[right]].append(node_dict[-left])

        adjacents[node_dict[-right]].append(node_dict[left])
        reversed_adjs[node_dict[left]].append(node_dict[-right])


    return edges, adjacents[:node_num], reversed_adjs[:node_num], node_dict, var_dict

class Color(Enum):
    R = 0
    G = 1
    B = 2

def get_node_color( var ):
    node = (var - 1) // 3
    c = var % 3
    if c == 0:
        return node, Color(2)
    elif c == 2:
        return node, Color(1)
    else:
        return node, Color(0)

def generate_2sat_clauses( n, edges, colors ):
    """
    If C is the set of colours (R, G, B), the colour c of each node must change to one of the
    colours in the set: C difference (c).
    It must also be the case that the colour c of any two adjacent nodes is not the same.
    """

    red = Color(0)
    green = Color(1)
    blue = Color(2)
    rgb = set([red, green, blue])

    clauses = []

    for node_ in range(1, n + 1):
        node = node_ * 3 - 2
        c1 = Color[colors[node_ - 1]]
        others = rgb.difference(set([c1]))
        c2 = others.pop()
        c3 = others.pop()
        c1_var = node + c1.value
        c2_var = node + c2.value
        c3_var = node + c3.value
        clauses += [[c2_var, c3_var], [-c2_var, -c3_var], [-c1_var, -c1_var]]

    for edge in edges:
        # Add adjacency conditions.
        left = edge[0] * 3 - 2
        right = edge[1] * 3 - 2
        clauses += [[-left, -right], [-(left + 1), -(right + 1)], [-(left + 2), -(right + 2)]]

    return clauses

def assign_new_colors(n, edges, colors):
    # Insert your code here.
    num_vars = n * 3
    clauses = generate_2sat_clauses(n, edges, colors[0])
    edges, implication_g, reversed_imp_g, node_map, var_map = build_implication_graph(num_vars, clauses)

    ccs = analyse_connected_components(num_vars, implication_g, reversed_imp_g, var_map)

    result = collections.defaultdict(lambda: None)

    for cc in ccs:
        cc_vars = set([])
        for node in cc:

            # Check valid solution.
            litteral = var_map[node]
            if abs(litteral) in cc_vars:
                return None
            else:
                cc_vars.add(abs(litteral))

            if result[abs(litteral)] is None:
                if litteral < 0:
                    result[abs(litteral)] = 0
                else:
                    result[abs(litteral)] = 1

    result_colors = []
    for key in sorted(result.keys()):
        if result[key] == 1:
            node, color = get_node_color(key)
            result_colors.append(color.name)
    return result_colors
    
def main():
    n, m = map(int, input().split())
    colors = input().split()
    edges = []
    for i in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    new_colors = assign_new_colors(n, edges, colors)
    if new_colors is None:
        print("Impossible")
    else:
        print(''.join(new_colors))

main()
