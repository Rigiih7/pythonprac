mygirl_edges = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('D', 'E'), ('D', 'F'), ('E', 'F'), ('E', 'G'), ('F', 'H'), ('G', 'H') ]
class Rvggraph():
    def __init__(self, Nodes):
        self.nodes = Nodes
        self.adj_list = {}

        for node in self.nodes:
            self.adj_list[node] = []
    def muthoni_edges(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
    def print_lv(self):
        for node in self.nodes:
            print(node, ':', self.adj_list[node])

Nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
graph = Rvggraph(Nodes)

for u, v in mygirl_edges:
    graph.muthoni_edges(u, v)

print(graph.print_lv())