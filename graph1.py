her_edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E')]
class Graph():
    def __init__(self, Nodes):
        self.nodes = Nodes
        self.adj_list = {}
        
        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def list_list(self):
        for node in self.nodes:
         print(node,'->',self.adj_list[node])
Nodes = ['A', 'B', 'C', 'D', 'E']
graph = Graph(Nodes)

for u, v in her_edges:
    graph.add_edge(u, v)

print(graph.list_list())
