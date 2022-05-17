Assignment 1
Implement Depth First Search algorithm and Breadth First Search algorithm. Use an undirected graph
and develop a recursive algorithm for searching all the vertices of a graph or tree data structure.
'''

class Node:
    def __init__(self, i):
        self.l = None
        self.r = None
        self.i = i

# -------------------------------------------------------
    
class Tree:
    def __init__(self, rX):
        self.root = rX

    # Get input function
    def getInput(self):
        q = [self.root]
        print("\nEnter data or -1 for no data\n")
        while q:
            tmp = q.pop()
            if(tmp!=None):
                lC = int(input("Enter left child of {}: ".format(tmp.i)))
                if lC!=-1:
                    tmp.l = Node(lC)
                    q.append(tmp.l)
                else:
                    tmp.l=None

                rC = int(input("Enter right child of {}: ".format(tmp.i)))
                if rC!=-1:
                    tmp.r = Node(rC)
                    q.append(tmp.r)
                else:
                    tmp.r=None

    # Recursive DFS function
    def dfs(self, x):
        print(x.i, end = ' ')
        if x.l:
            self.dfs(x.l)
        if x.r:
            self.dfs(x.r)

    # Recursive BFS function
    def bfs(self, x):
        queue = []
        queue.append(x)

        while(len(queue)>0):
            print(queue[0].i, end=' ')
            tmp = queue.pop(0)

            if tmp.l is not None:
                queue.append(tmp.l)
            if tmp.r is not None:
                queue.append(tmp.r)
    
# -------------------------------------------------------

# Menu
while(True):
    print("\n------------------------")
    print("BFS and DFS traversal")
    print("1. Enter data")
    print("2. BFS traversal")
    print("3. DFS traversal")
    print("4. Exit\n")

    c = int(input("Enter choice: "))
    if c==1:
        # Create a tree
        r = int(input("Enter the root node: "))
        ROOT = Node(r)
        t = Tree(ROOT)
        t.getInput()

    elif c==2:
        print("\n-- BFS Traversal --")
        t.bfs(ROOT)
        print("")

    elif c==3:
        print("\n-- DFS Traversal --")
        t.dfs(ROOT)
        print("")

    elif c==4:
        break

    else:
        print("Invalid Input")

'''
          20
        /    \
       7     23 
      / \    / \
     3   8  15  27

    BFS:    20 7 23 3 8 15 27
    DFS:    20 7 3 8 23 15 27

          10
        /    \
       2     12
      / \
     1   3

    BFS:    10 2 12 1 3
    DFS:    10 2 1 3 12
'''
