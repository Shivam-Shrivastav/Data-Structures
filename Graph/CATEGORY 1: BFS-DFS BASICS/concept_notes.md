# BFS / DFS Basics (Graph)

## 1. Pattern in One Minute

### Core Idea

Graphs represent **connections** between nodes. BFS and DFS are the two fundamental ways to traverse every reachable node.

* **BFS (Breadth-First Search):** Explore level by level using a **queue**.
* **DFS (Depth-First Search):** Explore one path completely before backtracking using **recursion or a stack**.

### Why does this pattern exist?

Many graph problems reduce to:

* Visit every node once.
* Find connected components.
* Check reachability.
* Find shortest path (unweighted).
* Detect cycles.
* Traverse trees/graphs systematically.

### Immediately think of BFS/DFS when...

* Graph is given explicitly (edges/adjacency list).
* Grid problems ("islands", "maze", "rooms")—treat cells as graph nodes.
* Need to visit all connected nodes.
* Need path existence.
* Need connected components.

---

# 2. Recognition Signals

### Strong BFS Clues

* Minimum number of moves
* Fewest steps
* Shortest path in **unweighted** graph
* Level-order traversal
* Distance from source
* Multi-source expansion

Examples:

* Word Ladder
* Rotting Oranges
* Open the Lock
* Walls and Gates

---

### Strong DFS Clues

* Explore all possibilities
* Connected components
* Islands
* Cycle detection
* Topological ordering (with modifications)
* Backtracking-style graph traversal

Examples:

* Number of Islands
* Clone Graph
* Keys and Rooms
* Flood Fill

---

### Common Disguises

Graph isn't always given.

Could be:

* Grid
* Maze
* Rooms & keys
* Courses
* Airports
* Social network
* Dependencies
* Roads
* Friend circles

Everything becomes:

```
Node
Neighbors
Visit
```

---

### Don't use BFS/DFS when

* Graph has weighted edges → Dijkstra/Bellman-Ford
* Need MST → Prim/Kruskal
* DP problem
* Greedy ordering

---

# 3. Mental Model

Think of graph traversal like exploring a city.

### BFS

* Stand at one city.
* Visit all immediate neighbors.
* Then neighbors' neighbors.
* Expands like circles in water.
* First time reaching a node = shortest distance.

---

### DFS

* Keep walking until stuck.
* Then backtrack.
* Explore another road.
* Naturally recursive.
* Excellent for exploring components.

---

Quick Recall:

```
BFS

1
|
2 3
| |
4 5

Visit:

1
2 3
4 5
```

```
DFS

1
|
2
|
4
(backtrack)
3
5
```

---

# 4. Boilerplate Templates

## BFS

```python
from collections import deque

def bfs(graph, start):
    q = deque([start])
    visited = {start}

    while q:
        node = q.popleft()

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
```

### Complexity

```
Time: O(V + E)

Space: O(V)
```

---

## DFS (Recursive)

```python
def dfs(node):
    visited.add(node)

    for nei in graph[node]:
        if nei not in visited:
            dfs(nei)

visited = set()
dfs(start)
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

## 1. BFS Shortest Path

Store distance.

```python
q.append((start, 0))
```

---

## 2. Multi-source BFS

Push every source initially.

Examples

* Rotting Oranges
* Walls and Gates

```python
for src in sources:
    q.append(src)
```

---

## 3. Grid DFS

Neighbors are directions.

```python
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
```

---

## 4. Connected Components

Outer loop.

```python
for node in range(n):
    if node not visited:
        dfs(node)
        components += 1
```

---

## 5. Path Exists

Stop when target found.

---

## 6. Cycle Detection

Maintain parent (undirected) or recursion stack (directed).

---

# 6. Common Pitfalls

### ❌ Forgetting visited

Infinite loops.

---

### ❌ Mark visited after popping

Better:

```python
visited.add(neighbor)
q.append(neighbor)
```

Otherwise duplicates enter queue.

---

### ❌ Assuming graph is connected

Need:

```python
for node in graph:
    if node not visited:
        dfs(node)
```

---

### ❌ Wrong BFS level handling

For shortest path:

```python
for _ in range(len(q)):
    ...
distance += 1
```

when level-based processing is required.

---

### ❌ Recursion limit

Large graphs:

Use iterative DFS.

---

### ❌ Grid boundary mistakes

Always check:

```
0 <= r < ROWS
0 <= c < COLS
```

---

# 7. Interview Checklist

✅ Problem mentions graph/grid.

✅ Need to visit connected nodes.

✅ Need reachability.

→ DFS/BFS.

---

✅ Need minimum edges/moves.

→ BFS.

---

✅ Need all components.

→ DFS/BFS + outer loop.

---

✅ Need shortest path in **unweighted** graph.

→ BFS.

---

✅ Need exhaustive exploration.

→ DFS.

---

# 8. Must-Do Problems

## Easy

⭐ **Top 3**

* **733. Flood Fill** ⭐
* **1971. Find if Path Exists in Graph** ⭐
* **841. Keys and Rooms** ⭐

Others

* 1791. Find Center of Star Graph

---

## Medium

⭐ **Top 3**

* **200. Number of Islands** ⭐
* **133. Clone Graph** ⭐
* **994. Rotting Oranges** ⭐

Others

* 695. Max Area of Island
* 417. Pacific Atlantic Water Flow
* 547. Number of Provinces

---

## Hard (Only if Important)

* 127. Word Ladder ⭐
* 329. Longest Increasing Path in Matrix (DFS + Memoization)

---

# 9. 30-Second Cheat Sheet

### Recognition

* Graph
* Grid
* Connected nodes
* Reachability
* Components
* Shortest path (unweighted)

---

### Core Idea

**BFS**

* Queue
* Level-by-level
* Shortest path (unweighted)

**DFS**

* Stack/Recursion
* Go deep, then backtrack
* Component exploration

---

### Templates

**BFS**

```python
queue → pop left → visit neighbors
```

**DFS**

```python
visit
for neighbor:
    dfs(neighbor)
```

---

### Complexity

* **Time:** `O(V + E)`
* **Space:** `O(V)`

---

### Common Variations

* Connected Components
* Multi-source BFS
* Grid Traversal
* Shortest Path (Unweighted)
* Cycle Detection
* Flood Fill

---

### Pitfalls

* Forgetting `visited`
* Duplicate queue entries
* Missing outer loop for disconnected graphs
* Recursion depth overflow
* Grid boundary errors
