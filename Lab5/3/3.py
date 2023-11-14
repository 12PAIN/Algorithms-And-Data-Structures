from Structures.Graph import Graph

visited = []


def dfs(current, visited, stack):
    visited.add(current)
    for neighbor in current.getConnections():
        if neighbor not in visited:
            dfs(neighbor, visited, stack)
    stack.append(current)


def topological_sort(graph):
    visited = set()
    stack = []
    for vert in graph:
        if vert not in visited:
            dfs(vert, visited, stack)
    return stack[::-1]


g = Graph()

g.addVertex("3/4 cup milk")
g.addVertex("1 egg")
g.addVertex("1 Tbl oil")

g.addVertex("1 cup mix")
g.addVertex("heat syrup")

g.addVertex("heat griddle")
g.addVertex("pour 1/4 cup")
g.addVertex("turn when bubbly")
g.addVertex("eat")

g.addEdge("3/4 cup milk", "1 cup mix")
g.addEdge("1 egg", "1 cup mix")
g.addEdge("1 Tbl oil", "1 cup mix")

g.addEdge("1 cup mix", "heat syrup")
g.addEdge("1 cup mix", "pour 1/4 cup")

g.addEdge("heat griddle", "pour 1/4 cup")
g.addEdge("pour 1/4 cup", "turn when bubbly")
g.addEdge("turn when bubbly", "eat")
g.addEdge("heat syrup", "eat")


for vertex in g:
    print(f"Original Graph: {vertex}")

result = topological_sort(g)

print()
print('Граф после топологической сортировки:')
for v in result:
    print(v)


