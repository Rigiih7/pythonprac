lavi_edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E')]
class Mygraph():
    def __init__(self, Nodes):
      self.nodes = Nodes
      self.adj_list = {}

      for node in self.nodes:
        self.adj_list[node] = []
    def add_edges(self, u, v):
      self.adj_list[u].append(v)
      self.adj_list[v].append(u)
    def print_all(self):
      for node in self.nodes:
        print(node,'->',self.adj_list[node])
      
Nodes = ['A', 'B', 'C', 'D', 'E']
graph = Mygraph(Nodes)

for u, v in lavi_edges:
    graph.add_edges(u, v)

print(graph.print_all())

