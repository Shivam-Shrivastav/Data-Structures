## 🧩 **LeetCode: Find if Path Exists in Graph (Graph / Connectivity)**

---

## 1. **Problem statement with example**

You are given:

* `n` nodes labeled from `0` to `n-1`
* A list of **undirected edges**
* Two nodes: `source` and `destination`

👉 Return **true if there is a path** from `source` to `destination`, otherwise false.

---

### Constraints (important)

* `1 <= n <= 2 * 10^5`
* `0 <= edges.length <= 2 * 10^5`
* Graph may be **disconnected**

---

## 2. **Diagram**

```text
Component 1:        Component 2:

0 —— 1 —— 2         3 —— 4 —— 5
```

👉 `0 → 2` ✅ reachable
👉 `0 → 5` ❌ not reachable

---

## 3. **Example I/O**

### Example 1 (Reachable)

```text
Input:
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0, destination = 2

Output: true
```

👉 Same component

---

### Example 2 (Not reachable)

```text
Input:
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0, destination = 5

Output: false
```

👉 Different components

---

## 4. **Intuition & pattern recognition**

### 🔍 Signals:

* "Path exists?" → **reachability**
* Undirected graph → no direction constraint
* No weights → no need for Dijkstra

---

### 💡 Core idea:

👉 Check if both nodes are in the **same connected component**

---

### 🧠 Interview thinking:

> "This is a pure connectivity problem — traversal or union-find works."

---

## 5. **Simpler version**

### Step 1 (Simplest thinking):

👉 "From a node, what all nodes can I reach?"

→ Basic DFS/BFS traversal

---

### Closely related:

👉 **Number of Islands**

* There: count components
* Here: check if 2 nodes belong to same component

---

### Transition thinking:

```text
Traversal → Components → Connectivity check
```

---

## 6. **Brute force**

### Idea:

* Try all possible paths (backtracking)

### Complexity:

* Time: **Exponential** ❌
* Not feasible

---

## 7. **Optimal solution**

---

### ✅ Approach 1: DFS (most intuitive)

```python
def validPath(n, edges, source, destination):
    graph = [[] for _ in range(n)]

    # Build adjacency list
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node):
        if node == destination:
            return True

        visited.add(node)

        for nei in graph[node]:
            if nei not in visited:
                if dfs(nei):
                    return True

        return False

    return dfs(source)
```

---

### ✅ Approach 2: BFS (iterative)

```python
from collections import deque

def validPath(n, edges, source, destination):
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([source])
    visited = set([source])

    while queue:
        node = queue.popleft()

        if node == destination:
            return True

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)

    return False
```

---

### ✅ Approach 3: Union-Find (best for large constraints)

```python
def validPath(n, edges, source, destination):
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # path compression
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    # Build components
    for u, v in edges:
        union(u, v)

    return find(source) == find(destination)
```

---

### Complexity:

* DFS/BFS → **O(n + e)**
* Union-Find → **~O(e α(n))**

---

## 8. **Step-by-step trace (BFS)**

### Input:

```text
edges = [[0,1],[1,2],[2,0]]
source = 0, destination = 2
```

---

### Step 1:

```text
queue = [0]
visited = {0}
```

---

### Step 2:

```text
pop 0 → neighbors: 1,2
queue = [1,2]
visited = {0,1,2}
```

---

### Step 3:

```text
pop 1 → not target
pop 2 → target found ✅
```

---

### Final:

```text
True
```

---

## 9. **Related problems**

1. **Number of Connected Components in an Undirected Graph**
   → Count components

2. **Graph Valid Tree**
   → Connectivity + cycle

3. **Redundant Connection**
   → Detect extra edge

4. **Clone Graph**
   → Graph traversal

5. **Is Graph Bipartite?**
   → DFS with coloring

---

## ⚡ Final takeaway

👉 This is **the most fundamental graph problem**

### 🔥 Core pattern:

```text
Connectivity check
→ DFS / BFS / Union-Find
```

---

### 🚀 Interview one-liner:

> "I’ll treat this as a connected components problem — if source and destination belong to the same component, return true."

---

If you want, I can next:

* Show **when DFS fails but Union-Find shines (interview trick)**
* Or give a **1-page cheat sheet for all graph patterns**
