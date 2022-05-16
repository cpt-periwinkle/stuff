class Node:
    def __init__(self, data, level, fval):
        self.data = data
        self.level = level
        self.fval = fval

    def create_states(self):  # Create child states by moving blank space #4
        a, b = self.find(self.data, "_")

        val_list = [[a, b - 1], [a, b + 1], [a - 1, b], [a + 1, b]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data, a, b, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):  # 3
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            tmp = []
            tmp = self.copy(puz)
            tmp2 = tmp[x2][y2]
            tmp[x2][y2] = tmp[x1][y1]
            tmp[x1][y1] = tmp2
            return tmp
        else:
            return None

    def copy(self, root):  # Copy matrix #2
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, puz, x):  # Find blank space #1
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j


class Puzzle:
    def __init__(self, size):  # Initialize puzzle size
        self.n = size
        # Open list, Closed list
        self.open = []
        self.closed = []

    def accept(self):  # Get puzzle input
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def f(self, start, goal):  # Function to calculate heuristic value
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != "_":
                    temp += 1
        return temp

    def process(self):
        print("\nEnter Start State: \n")
        start = self.accept()
        print("\nEnter Goal State: \n")
        goal = self.accept()

        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)

        self.open.append(start)
        print("\n")
        while True:
            cur = self.open[0]
            print("")

            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")

            if self.h(cur.data, goal) == 0:  # Reached goal state
                break
            for i in cur.create_states():
                i.fval = self.f(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

            self.open.sort(key=lambda x: x.fval, reverse=False)  # Sort by f value


print("\n---- 8-Puzzle using A* Algorithm ----")
x = Puzzle(3)
x.process()

"""
SAMPLE CASE:

 START STATE    GOAL STATE
    1 2 3         1 2 3
    _ 4 6         4 5 6
    7 5 8         7 8 _
"""
