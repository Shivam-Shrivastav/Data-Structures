
from collections import defaultdict

vertices, edges = input("Enter number of vertices and edges: ").split()
vertices = int(vertices)
edges = int(edges)
arr = defaultdict(list)
for _ in range(0, edges):
	x, y = input("Enter the two nodes which are going to have connections: ").split()
	arr[x].append(y)
	arr[y].append(x)

for key, value in arr.items():
	print(f'{key} -->{value}')

# print(arr)
