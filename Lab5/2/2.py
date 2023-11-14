from Structures.Graph import Graph

g = Graph()
for i in range(4):
    g.addVertex(i)

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(2, 1)

for vert in g:
    for neighbor in vert.getConnections():
        print("( %s, %s, %s )" % (vert.getId(), neighbor.getId(), vert.getWeight(neighbor)))

reversedGraph = g.reverse()

for vert in reversedGraph:
    for neighbor in vert.getConnections():
        print("( %s, %s, %s )" % (vert.getId(), neighbor.getId(), vert.getWeight(neighbor)))