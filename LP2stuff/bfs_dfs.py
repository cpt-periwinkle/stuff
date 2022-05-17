graph = {
  '1' : ['2','3'],
  '2' : ['4', '5'],
  '3' : ['6'],
  '4' : [],
  '5' : ['6'],
  '6' : []
}

visited = []  # List for visited nodes.
queue = []
visited2 = set()

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    print (m, end = " ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

def dfs(visited2, graph, node):
    if node not in visited2:
        print (node, end = " ")
        visited2.add(node)
        for neighbour in graph[node]:
            dfs(visited2, graph, neighbour)

def searchElement(self):
    element = int(input("Search element: "))
    start = 1
    print("Searching: ", end="")
    found = self.dfs(visited2, start, element)
    print()
    for node in self.nodes:
        node.visited = False
    if found == True:
        print("Vertex Found")
    else:
        print("Vertex Not Found")

while True:
    print(
        "\nSelect Choice\n",
        "1) BFS\n",
        "2) DFS\n",
        "3)Exit"
    )
    choice = int(input("Enter choice:"))
    if choice == 1:
        print("\nBreadth-First Search:")
        bfs(visited, graph, '1')
    elif choice == 2:
        print("\nDepth-First Search:")
        dfs(visited2, graph, '1')
    else:
        break

"""
Graph:
        1
       / \
      2   3
     / \   \
    4   5 - 6

OUTPUT:
Breadth-First Search: 
1 2 3 4 5 6 

Depth-First Search:
1 2 4 5 6 3 

"""
