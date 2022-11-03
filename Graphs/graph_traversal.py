class  Graph:
    def __init__(self, gDict=None):
        if gDict is None:
            gDict = {}
        self.gDict = gDict
    
    def addEdge(self, vertex, edge):
        self.gDict[vertex].append(edge)
    
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            dequeuedVertex = queue.pop(0)
            print(dequeuedVertex)
            for adjVertex in self.gDict[dequeuedVertex]:
                if adjVertex not in visited:
                    visited.append(adjVertex)
                    queue.append(adjVertex)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popped = stack.pop()
            print(popped)
            for adjVertex in self.gDict[popped]:
                if adjVertex not in visited:
                    visited.append(adjVertex)
                    stack.append(adjVertex)
                    


customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f"],
    "f": ["d", "e"]
}

graph = Graph(customDict)

graph.dfs("a")