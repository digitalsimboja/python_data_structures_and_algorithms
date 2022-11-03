from collections import defaultDict
# IMplemented wih the stack data structure

class Graph:
    def __init__(self, numberOfVertices):
        self.graph = defaultDict(list)
        self.numberOfVertices = numberOfVertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)
    
    def topologicalSortUtil(self, vertex, visited, stack):
        visited.append(vertex)

        for i in self.graph[vertex]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        
        stack.insert(0, vertex)

    
    def topologicalSort(self):

        visited = []
        stack = []

        for k in list(self.grap):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)
        
        print(stack)
            
       