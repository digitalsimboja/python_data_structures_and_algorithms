# Undirected Graph
# Directed Graph
# Cyclic 
# Acyclic
# Tree or Directed Acyclic

class Graph:
    def __init__(self):
        self.adjancency_list = {}

    def addVertex(self, vertex):
        if vertex not in self.adjancency_list.keys():
            self.adjancency_list[vertex] = []
            return True
        return False
    
    def printGraph(self):
        for v in self.adjancency_list:
            print(v, ":", self.adjancency_list[v])
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjancency_list.keys() and vertex2 in self.adjancency_list.keys():
            self.adjancency_list[vertex1].append(vertex2)
            self.adjancency_list[vertex2].append(vertex1)
            return True
        else:
            return False
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjancency_list.keys() and vertex2 in self.adjancency_list.keys():
            try:
                self.adjancency_list[vertex1].remove(vertex2)
                self.adjancency_list[vertex2].remove(vertex1)
            
                return True
            except ValueError:
                print("Value error occurred")
        else:
            return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adjancency_list.keys():
            for other_vertex in self.adjancency_list.keys():
                self.adjancency_list[other_vertex].remove(vertex)
            del self.adjancency_list[vertex]
            return True
        else:
            return False
    



graph = Graph()
graph.addVertex('A')
graph.addVertex('B')
graph.addVertex('D')
graph.addVertex('C')
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "C")

# graph.printGraph()
graph.remove_edge("A", "D")
graph.printGraph()