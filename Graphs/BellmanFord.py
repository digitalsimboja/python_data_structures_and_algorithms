# Uses the graph datastructure

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
    
    def add_edge(self, start, destination, weight):
        self.graph.append([start, destination, weight])

    def addNode(self, value):
        self.nodes.append(value)
    
    def print_solution(self, distance):
        print("Vertex distance from source")
        for key, value in distance.items():
            print(' ' + key, ' : ', value)
    
    def bellmanFord(self, src):
        dist = {i: float("inf") for i in self.nodes}
        dist[src] = 0

        for _ in range(self.V -1):
            for s, d, w in self.graph:
                if dist[s] != float("inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
        
        for s, d, w in self.graph:
            if dist[s] != float("inf") and dist[s] + w < dist[d]:
                print("The graph contains negative cycle")
                return
        
        self.print_solution(dist)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", 6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
g.bellmanFord("E")
