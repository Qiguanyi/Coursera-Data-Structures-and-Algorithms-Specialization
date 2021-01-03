# python3
import collections
import sys
import threading


sys.setrecursionlimit(10 ** 6)
threading.stack_size(2 ** 26)

# This solution tries all possible 2^n variable assignments.
# It is too slow to pass the problem.
# Implement a more efficient algorithm here.


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

def isSatisfiable(n, m, clauses):
    edges, implication_g, reversed_imp_g, node_map, var_map = build_implication_graph(n, clauses)

    ccs = analyse_connected_components(n, implication_g, reversed_imp_g, var_map)

    result = collections.defaultdict(lambda: None)
    for cc in ccs:
        cc_vars = set([])
        for node in cc:
            lit = var_map[node]
            if abs(lit) in cc_vars:
                return None
            else:
                cc_vars.add(abs(lit))

            if result[abs(lit)] is None:
                if lit < 0:
                    result[abs(lit)] = 0
                else:
                    result[abs(lit)] = 1

    return result

def print_isSatisfiable():
    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]
    
    result = isSatisfiable(n, m, clauses)
    
    if result is None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE");
        print(" ".join(str(i+1 if result[i+1] else -i-1) for i in range(n)))


if __name__ == '__main__':
    threading.Thread(target = print_isSatisfiable).start()