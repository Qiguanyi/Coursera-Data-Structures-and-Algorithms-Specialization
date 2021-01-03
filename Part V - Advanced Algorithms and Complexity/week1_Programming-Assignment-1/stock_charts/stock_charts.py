# python3
import queue


class StockCharts:
    def read_data(self):
        n, k = map(int, input().split())
        stock_data = [list(map(int, input().split())) for i in range(n)]
        return stock_data

    def write_response(self, result):
        print(result)

    def min_charts(self, stock_data):
        # Replace this incorrect greedy algorithm with an
        # algorithm that correctly finds the minimum number
        # of charts on which we can put all the stock data
        # without intersections of graphs on one chart.
        n = len(stock_data)
        k = len(stock_data[0])
        adj_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if all([x < y for x, y in zip(stock_data[i], stock_data[j])]):
                    adj_matrix[i][j] = 1
        matching = [-1] * n
        busy_right = [False] * n
    
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
                            parent[(2, i)] = currNode
                            q.put((2, i))
                elif currNode[0] == 2:
                    i = currNode[1]
                    for j in range(n):
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
        
        return len([0 for i in matching if -1 == i])

    
    def solve(self):
        stock_data = self.read_data()
        result = self.min_charts(stock_data)
        self.write_response(result)

if __name__ == '__main__':
    stock_charts = StockCharts()
    stock_charts.solve()
