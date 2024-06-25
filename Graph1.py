# Graph
class Graph:
    def __init__(self):
        self.graph={}
    def AddVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]
        # else:
        #     print("Already exist")
    def AddEdge(self,vertex1,vertex2,isDirected=False):
        self.AddVertex(vertex1)
        self.AddVertex(vertex2)
        self.graph[vertex1].append(vertex2)
        if not isDirected:
            self.graph[vertex2].append(vertex1)
    def display(self):
        for key,value in self.graph.items():
            print(f"{key}=>{value}")

    def GetVertices(self):
        for i in self.graph:
            print(i)

    def GetEdge(self):
        for key,value in self.graph.items():
            for vertex in value:
                print(f"({key},{vertex})")

    def RemoveVertex(self,vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for key,value in self.graph.items():
                if vertex in value:
                    value.remove(vertex)
                # for i in value:
                #     if i == vertex:
                #         value.remove(i)

    def IsEdge(self,vertex1,vertex2):
        return vertex1 in self.graph[vertex2] or vertex2 in  self.graph[vertex1]

    def RemoveEdge(self,vertex1,vertex2):
        if self.IsEdge(vertex1,vertex2):
            self.graph[vertex1].remove(vertex2)
            self.graph[vertex2].remove(vertex1)

    def Dfs_traversal(self,start,AlreadyVisited):
        if start not in AlreadyVisited:
            AlreadyVisited.add(start)
            print (start,end=" ")
            for child in self.graph[start]:
                self.Dfs_traversal(child,AlreadyVisited)
    def Dfs_traversal1(self, start, AlreadyVisited=None):
        if AlreadyVisited is None:
            AlreadyVisited = []
        if start not in AlreadyVisited:
            AlreadyVisited.append(start)
            print(start, end=" ")
            for child in self.graph[start]:
                self.Dfs_traversal1(child, AlreadyVisited)
    def Bfs_traversal(self,start):
        AlreadyVisited={start}
        Queue=[start]
        while len(Queue)>0:
            current=Queue.pop(0)
            print(current,end=" ")
            for child in self.graph[current]:
                if child not in AlreadyVisited:
                    Queue.append(child)
                    AlreadyVisited.add(child)


    def Shortest_path(self,start,end):
        AlreadyVisited={start}
        Queue=[(start,[start])]
        while len(Queue)>0:
            current,path=Queue.pop(0)
            for child in self.graph[current]:
                if child==end:
                    return path+[child]
                if child not in AlreadyVisited:
                    Queue.append((child,path+[child]))
                    AlreadyVisited.add(child)

graph1=Graph()
# graph1.AddVertex('A')
# graph1.AddVertex('B')
graph1.AddEdge('A','B')
graph1.AddEdge('B','E')
graph1.AddEdge('B','C')
graph1.AddEdge('C','D')
graph1.AddEdge('B','D')
# print(graph1.graph)
# print(graph1.graph.items())
# graph1.display()
# graph1.GetVertices()
# graph1.GetEdge()
# graph1.RemoveVertex('C')
# graph1.RemoveEdge('A','C')
graph1.display()
graph1.Dfs_traversal('A',set())
graph1.Dfs_traversal1('A')
graph1.Bfs_traversal('A')
print(graph1.Shortest_path('A','D'))
