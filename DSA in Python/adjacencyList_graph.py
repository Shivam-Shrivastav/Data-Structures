vertices, edges = map(int, input("Enter number of vertices and edges: ").split())

adj = [[] for i in range(vertices)]

print(adj)

for _ in range(edges):
	x, y = map(int, input("Enter the two nodes which are going to have connections: ").split())
	adj[x].append(y)

print(adj)