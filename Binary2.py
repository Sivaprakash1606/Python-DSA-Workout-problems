class Graph:
    def __init__(self):
        self.graph={}
    def AddVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
    def AddEdge(self,vertex1,vertex2,isDirected=False):
        self.AddVertex(vertex1)
        self.AddVertex(vertex2)
        self.graph[vertex1].append(vertex2)
        if not isDirected:
            self.graph[vertex2].append(vertex1)
    def GetVertex(self):
        for i in self.graph:
            print(i)
    def display(self):
        for key,value in self.graph.items():
            print(f"{key}=>{value}")












graph1=Graph()
graph1.AddEdge('A','B')
graph1.AddEdge('B','C')
graph1.AddEdge('D','B')
graph1.AddEdge('C','D')
graph1.GetVertex()
graph1.display()







