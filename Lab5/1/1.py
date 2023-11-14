from collections import deque
from Structures.Graph import Graph


def person_is_seller(vertex):
    return vertex.getId()[0] == 'a'


def search(graph, name):
    search_queue = deque()
    search_queue += graph.getVertex(name).getConnections()
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person.getId() + " is a mango seller!")
                return True
            else:
                search_queue += graph.getVertex(person).getConnections()
                searched.add(person)
    return False


g = Graph()

g.addVertex("you")
g.addVertex("bob")
g.addVertex("alice")
g.addVertex("claire")
g.addVertex("anuj")
g.addVertex("peggy")
g.addVertex("thom")
g.addVertex("jonny")

g.addEdge("you", "alice")
g.addEdge("you", "bob")
g.addEdge("you", "claire")
g.addEdge("bob", "anuj")
g.addEdge("bob", "peggy")
g.addEdge("alice", "peggy")
g.addEdge("claire", "thom")
g.addEdge("claire", "jonny")

for vert in g:
    for neighbor in vert.getConnections():
        print("( %s, %s, %s )" % (vert.getId(), neighbor.getId(), vert.getWeight(neighbor)))

print("\n")
search(g, "you")
