class Graph:
    def __init__(self):
        self.adjList = {}

    def __addSingleVertex(self, node):
        if node not in self.adjList.keys():
            self.adjList[node] = []

    def addVertices(self, nodes):
        if type(nodes) == list:
            for node in nodes:
                self.__addSingleVertex(node)
        elif type(nodes) == str:
            self.__addSingleVertex(nodes)

    def addEdge(self, node1, node2):
        if node1 in self.adjList.keys() and node2 in self.adjList.keys():
            if node1 in self.adjList[node2] or node2 in self.adjList[node1]:
                return
            else:
                self.adjList[node1].append(node2)
                self.adjList[node2].append(node1)

    def rmnode(self, node):
        pass

    def rmEdge(self, node1, node2):
        pass

    def isConnected(self):
        pass

    def shortestPath(self, node1, node2):
        pass

    def printGraph(self):
        print(self.adjList)


g = Graph()

g.addVertices(['a', 'b', 'c'])


g.addVertices('d')


g.addEdge('a', 'b')
g.addEdge('a', 'c')
g.addEdge('d', 'b')

g.printGraph()
