# Graph Representation & Traversal (Graph Pattern)

## 1. Pattern in One Minute

### Core Idea

Before solving any graph problem, you need to:

1. Represent the graph efficiently.
2. Traverse every required node using **BFS** or **DFS**.

Almost every graph interview problem starts here.

### Why does this pattern exist?

Graphs don't have a natural ordering like arrays or trees.

Traversal helps answer questions like:

* Can I reach node X?
* Are all nodes connected?
* How many connected components exist?
* Is there a path?
* Explore every vertex exactly once.

### Immediately think of this pattern when...

* Nodes + edges are given
* "Visit all reachable nodes"
* Connectivity
* Components
* Path existence
* Grid traversal (matrix = implicit graph)

---

# 2. Recognition Signals

### Keywords

* Graph
* Network
* Roads
* Flights
* Friends
* Dependencies
* Connected
* Reachable
* Component
* Island
* Traverse
* Visit

---

### Constraints

Usually

```
N <= 2e5
M <= 2e5
```

Need

```
O(V + E)
```

---

### Common disguises

* Number of Islands
* Friend Circles
* Provinces
* Maze
* Word Ladder
* Clone Graph
* Flood Fill
* Course graph

---

### Don't use this when

* Need shortest weighted path → Dijkstra
* Need minimum spanning tree → Kruskal/Prim
* Need topological ordering → Topological Sort
* Need repeated shortest paths → Floyd Warshall

---

# 3. Mental Model

Think:

* Every node has neighbors.
* Store neighbors.
* Start somewhere.
* Visit neighbor.
* Continue.
* Never revisit visited nodes.
* Repeat until nothing left.
* If graph disconnected → start traversal again.

---

### BFS Mental Model

```
Layer by layer

0
|
1
|\
2 3
|
4
```

Visit

```
0
1
2
3
4
```

Uses **Queue**

---

### DFS Mental Model

```
Go as deep as possible

0
|
1
|
2
|
3
|
4
```

Uses **Recursion / Stack**

---

# 4. Boilerplate Template

## Graph Representation (Adjacency List)

```python
from collections import defaultdict

graph = defaultdict(list)

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)      # remove for directed graph
```

---

## BFS

```python
from collections import deque

visited = set()

def bfs(start):
    q = deque([start])
    visited.add(start)

    while q:
        node = q.popleft()

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
```

Time

```
O(V + E)
```

---

## DFS (Recursive)

```python
visited = set()

def dfs(node):
    visited.add(node)

    for nei in graph[node]:
        if nei not in visited:
            dfs(nei)
```

---

## DFS (Iterative)

```python
stack = [start]
visited = {start}

while stack:
    node = stack.pop()

    for nei in graph[node]:
        if nei not in visited:
            visited.add(nei)
            stack.append(nei)
```

---

# 5. Variations

## 1. Disconnected Graph

Loop over every node.

```python
for node in range(n):
    if node not in visited:
        dfs(node)
```

---

## 2. Grid Graph

Instead of adjacency list

```
4 directions

(-1,0)
(1,0)
(0,-1)
(0,1)
```

Neighbors generated dynamically.

---

## 3. Directed Graph

Only

```python
graph[u].append(v)
```

No reverse edge.

---

## 4. Multi-source BFS

Initialize queue with multiple sources.

```
Rotting Oranges
01 Matrix
Walls and Gates
```

---

## 5. Path Reconstruction

Store parent.

```python
parent[child] = node
```

Recover path backwards.

---

# 6. Common Pitfalls

### ❌ Forgetting visited

Infinite loop.

---

### ❌ Mark visited after popping

Instead

```python
visited.add(nei)

q.append(nei)
```

Mark **before enqueue/push**.

---

### ❌ Missing disconnected components

Need

```python
for every node:
```

---

### ❌ Wrong graph construction

Undirected

```
u -> v
v -> u
```

Directed

```
u -> v only
```

---

### ❌ Recursion overflow

Large graph

```
DFS recursion may fail.

Use iterative DFS.
```

---

# 7. Interview Checklist

✓ Nodes and edges given

✓ Need traversal

✓ Reachability

✓ Connectivity

✓ Components

✓ Explore neighbors

↓

Represent graph

↓

Need shortest levels?

→ BFS

Need deep exploration?

→ DFS

---

# 8. Must-Do Problems

## Easy

⭐ **Top 3**

* ✅ LeetCode 733 — Flood Fill
* ✅ LeetCode 1971 — Find if Path Exists in Graph
* LeetCode 841 — Keys and Rooms

---

## Medium

⭐ **Top 3**

* ✅ LeetCode 200 — Number of Islands
* ✅ LeetCode 547 — Number of Provinces
* ✅ LeetCode 133 — Clone Graph

Other important:

* LeetCode 695 — Max Area of Island
* LeetCode 130 — Surrounded Regions
* LeetCode 417 — Pacific Atlantic Water Flow

---

## Hard (only if important)

* LeetCode 127 — Word Ladder *(BFS classic)*
* LeetCode 126 — Word Ladder II

---

# 9. 30-Second Cheat Sheet

### Recognition

* Nodes + edges
* Connectivity
* Reachability
* Components
* Grid traversal

---

### Core Idea

Represent graph as **Adjacency List**.

Traverse using

* BFS → Queue
* DFS → Stack/Recursion

Always maintain **visited**.

---

### Templates

```
Adjacency List

graph[u].append(v)
graph[v].append(u)
```

```
BFS

Queue
Visited
Level order
```

```
DFS

Recursion / Stack
Visited
Go deep first
```

---

### Complexity

| Operation   | Complexity   |
| ----------- | ------------ |
| Build Graph | **O(E)**     |
| BFS         | **O(V + E)** |
| DFS         | **O(V + E)** |
| Space       | **O(V + E)** |

---

### Common Variations

* Connected Components
* Grid DFS/BFS
* Directed Graph
* Multi-source BFS
* Path Reconstruction

---

### Pitfalls

* Forget `visited`
* Wrong graph direction
* Miss disconnected nodes
* Mark visited too late
* Recursive DFS stack overflow on very large graphs
