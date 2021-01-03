# python3
import queue


class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        matching = [-1] * n
        busy_right = [False] * m
        
        def bfs():
            visited = set()
            q = queue.Queue()
            q.put((1, None))
            visited.add((1, None))
            
            path = []
            parent = dict()
            
            while not q.empty():
                currNode = q.get()
                
                if currNode[0] == 1:
                    for i in range(n):
                        if matching[i] == -1:
                            visited.add((2, i))
                            parent[(2, i)] = (1, None)
                            q.put((2, i))
                elif currNode[0] == 2:
                    i = currNode[1]
                    for j in range(m):
                        if adj_matrix[i][j] == 1 and matching[i] != j and not (3, j) in visited:
                            visited.add((3, j))
                            parent[(3, j)] = currNode
                            q.put((3, j))
                elif currNode[0] == 3:
                    j = currNode[1]
                    if not busy_right[j]:
                        prevNode = currNode
                        currNode = (4, j)
                        while True:
                            path.insert(0, (prevNode, currNode))
                            if prevNode[0] == 1:
                                break
                            currNode = prevNode
                            prevNode = parent[currNode]
                        for p in path:
                            if p[0][0] == 2:
                                matching[p[0][1]] = p[1][1]
                            elif p[0][0] == 3 and p[1][0] == 4:
                                busy_right[p[1][1]] = True
        
                        return True
                    else:
                        for i in range(n):
                            if matching[i] == j and not (2, i) in visited:
                                visited.add((2, i))
                                parent[(2, i)] = currNode
                                q.put((2, i))
            return False
        
        while bfs():
            continue
        
        return matching

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
