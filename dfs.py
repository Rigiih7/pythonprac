adj_list = {
    "A" : ["B", "C"],
    "B" : ["D", "E"],
    "C" : ["B", "F"],
    "D" : [],
    "E" : ["F"],
    "F" : []
}

color = {}
parent = {}
trav_time = {}
dfs_travesal_output = []

for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1, -1]


time = 0
def discover_node(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_travesal_output.append(u)
    time+=1

    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            discover_node(v)
    
    color[u] = "B"
    trav_time[u][1] = time
    time+=1
discover_node("A")
print(color)
print(parent)
print(trav_time)
print(dfs_travesal_output)

for node in adj_list.keys():
    print(node, ':', trav_time[node])
