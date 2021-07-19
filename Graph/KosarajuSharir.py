class DirectedGraph:
    def __init__(self) -> None:
        self.conections = {}
        self.vertices = 0
        self.edges = 0

    def addEdge(self, v, w):
        if v not in self.conections:
            self.conections[v] = []
            self.vertices += 1
        if w not in self.conections:
            self.conections[w] = []
            self.vertices += 1
        self.conections[v].append(w)
        self.edges += 1

    def adjacent(self, v):
        if v not in self.conections:
            return []
        else:
            return self.conections[v]

    def V(self):
        return self.vertices

    def E(self):
        return self.edges

    def toString(self):
        for a in self.conections:
            print(a, ':', self.conections[a])

    def reverse(self):
        reverse = DirectedGraph()
        for c in self.conections:
            for e in self.conections[c]:
                reverse.addEdge(e, c)
        return reverse


myGraph = DirectedGraph()
myGraph.addEdge(0, 1)
myGraph.addEdge(1, 2)
myGraph.addEdge(2, 0)
myGraph.addEdge(2, 3)
myGraph.addEdge(3, 4)
myGraph.addEdge(4, 7)
myGraph.addEdge(4, 5)
myGraph.addEdge(6, 4)
myGraph.addEdge(6, 7)
myGraph.addEdge(5, 6)

temp = myGraph
myGraph = myGraph.reverse()
marked = {}
reversePost = []


def dfs(graph, source):
    marked[source] = True
    for a in graph.adjacent(source):
        if a not in marked:
            marked[a] = False
        if not marked[a]:
            dfs(graph, a)
    reversePost.append(source)


for a in myGraph.conections:
    if a not in marked:
        marked[a] = False
    if not marked[a]:
        dfs(myGraph, a)


aux = reversePost[::-1]
marked = {}
id = {}
myGraph = temp
count = 0


def dfs2(graph, source, count):
    marked[source] = True
    id[source] = count
    for a in graph.adjacent(source):
        if a not in marked:
            marked[a] = False
        if not marked[a]:
            dfs2(graph, a, count)


for a in aux:
    if a not in marked:
        marked[a] = False
    if not marked[a]:
        dfs2(myGraph, a, count)
        count += 1

samegroups = {}
for i in id:
    if id[i] not in samegroups:
        samegroups[id[i]] = []
    samegroups[id[i]].append(i)
print(samegroups)
