#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max_stack = []
        self.size = 0

    def Push(self, a):
        self.__stack.append(a)
        self.size += 1
        if self.size == 1:
            self.__max_stack.append(a)
        else:
            if self.__max_stack[-1] <= a:
                self.__max_stack.append(a)

    def Pop(self):
        assert(self.size)
        a = self.__stack.pop()
        self.size -= 1
        if a == self.__max_stack[-1]:
            self.__max_stack.pop()

    def Max(self):
        assert(self.size)
        return self.__max_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)