class Solution:
    def validPath(self, n, edge, source, destination) :
        self.graph = {}
        for i in edges:
            if i[0] not in self.graph:
                self.graph[i[0]] = set()
            if i[1] not in self.graph:
                self.graph[i[1]] = set()
            self.graph[i[0]].add(i[1])
            self.graph[i[1]].add(i[0])
        print("Graph:", self.graph)
        return self.dfs(source, destination, set())

    def dfs(self, source, destination, alreadyvisited):
        print("Visiting node:", source)
        if source == destination:
            print("Reached destination")
            return True
        if source not in alreadyvisited:
            alreadyvisited.add(source)
            for child in self.graph.get(source, []):
                print("Checking child:", child)
                if self.dfs(child, destination, alreadyvisited):
                    return True
        print("Backtracking from node:", source)
        return False

    # Test the code


sol = Solution()
n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
print("Output:", sol.validPath(n, edges, source, destination))
