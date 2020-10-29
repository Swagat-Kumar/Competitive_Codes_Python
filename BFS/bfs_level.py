class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def adjacent(self, vertex):
        return list(self.adj[vertex])

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)


class BFSLevel:
    def __init__(self, myGraph):
        self.level = [-1 for i in range(myGraph.V)]
        self.visited = [False]*myGraph.V
        queue = []
        queue.append(0)
        self.level[0] = 1
        self.visited[0] = True
        while len(queue) > 0:
            vertex = queue.pop(0)
            for ends in myGraph.adjacent(vertex):
                if(not self.visited[ends]):
                    queue.append(ends)
                    self.visited[ends] = True
                    self.level[ends] = self.level[vertex]+1

    def returnNumberLevel(self, number):
        count = 0
        for i in self.level:
            if(number == i):
                count += 1
        return count


nodes = int(input())
myGraph = Graph(nodes)
for i in range(nodes-1):
    a, b = map(int, input().split())
    myGraph.addEdge(a-1, b-1)
bf = BFSLevel(myGraph)
x = int(input())
print(bf.returnNumberLevel(x))
