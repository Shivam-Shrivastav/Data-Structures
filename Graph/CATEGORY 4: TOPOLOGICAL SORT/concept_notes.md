# Topological Sort (Graph)

## 1. Pattern in One Minute

### Core Idea

Topological Sort produces a **linear ordering of vertices** such that for every directed edge **u → v**, **u appears before v**.

It only works on a **Directed Acyclic Graph (DAG)**.

### Why does this pattern exist?

Many problems have **dependencies**:

* Course A before Course B
* Compile file X before file Y
* Task 1 before Task 2

Topological Sort finds an order that satisfies all dependencies.

### When should I immediately think of it?

Whenever the problem asks for:

* Order of tasks
* Dependency resolution
* Course scheduling
* Build order
* Recipe execution
* Alien dictionary
* Event ordering

---

# 2. Recognition Signals

### Strong Clues

* "Before / After"
* "Dependency"
* "Prerequisite"
* "Must complete first"
* "Build order"
* "Scheduling"
* "Ordering"
* Directed graph
* DAG

### Common Disguises

* Course Schedule
* Software package installation
* Recipe steps
* Job scheduling
* Character ordering (Alien Dictionary)

### When NOT to use

❌ Undirected graph

❌ Need shortest path

❌ Need connected components

❌ Cyclic graphs (unless checking for cycle)

---

# 3. Mental Model

Think:

* Every node waits for its prerequisites.
* Nodes with **0 prerequisites** can be done immediately.
* Remove completed nodes.
* Their neighbors may now become available.
* Repeat until no nodes remain.

For DFS:

* Finish children first.
* Push node after exploring.
* Reverse the finishing order.

---

# 4. Boilerplate Template

## Kahn's Algorithm (BFS)

```python
from collections import defaultdict, deque

def topoSort(n, edges):
    graph = defaultdict(list)
    indegree = [0] * n

    # Build graph
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    q = deque()

    # Nodes with no prerequisites
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    order = []

    while q:
        node = q.popleft()
        order.append(node)

        for nei in graph[node]:
            indegree[nei] -= 1

            if indegree[nei] == 0:
                q.append(nei)

    return order if len(order) == n else []
```

### Complexity

* Time: **O(V + E)**
* Space: **O(V + E)**

---

## DFS Version

```python
def topoSort(n, graph):

    visited = [0] * n      # 0 = unvisited
                           # 1 = visiting
                           # 2 = visited

    order = []

    def dfs(node):

        if visited[node] == 1:
            return False        # cycle

        if visited[node] == 2:
            return True

        visited[node] = 1

        for nei in graph[node]:
            if not dfs(nei):
                return False

        visited[node] = 2
        order.append(node)

        return True

    for i in range(n):
        if visited[i] == 0:
            if not dfs(i):
                return []

    return order[::-1]
```

---

# 5. Variations

### 1. Return one valid ordering

Standard Topological Sort.

---

### 2. Detect cycle

If:

```
len(order) != number_of_nodes
```

then graph contains a cycle.

---

### 3. Multiple valid orders

Topological sort is **not unique**.

Different queue orders produce different answers.

---

### 4. Lexicographically smallest order

Use

```python
heapq
```

instead of queue.

---

### 5. All Topological Orders

Backtracking.

Rare in interviews.

---

# 6. Common Pitfalls

### ❌ Forgetting indegree updates

Always:

```python
indegree[neighbor] -= 1
```

---

### ❌ Not initializing zero indegree nodes

Need

```python
for i in range(n):
```

---

### ❌ Using on undirected graph

Topological sort is **only for directed graphs**.

---

### ❌ Forgetting cycle check

Return

```python
len(order) == n
```

---

### ❌ DFS without visiting states

Need

```
0 = unvisited
1 = visiting
2 = visited
```

Otherwise cycles aren't detected.

---

# 7. Interview Checklist

✓ Directed graph

✓ Dependency relationship

✓ Before / After

✓ Need valid ordering

✓ Detect impossible ordering

✓ DAG

→ Think **Topological Sort**

---

# 8. Must-Do Problems

### ⭐ Top 3

1. **LC 207 — Course Schedule** ⭐
2. **LC 210 — Course Schedule II** ⭐
3. **LC 269 — Alien Dictionary** ⭐

### Easy

* None that are standard for this pattern.

### Medium

* LC 207 — Course Schedule ⭐
* LC 210 — Course Schedule II ⭐
* LC 1136 — Parallel Courses
* LC 2115 — Find All Possible Recipes from Given Supplies

### Hard

* LC 269 — Alien Dictionary ⭐
* LC 1203 — Sort Items by Groups Respecting Dependencies

---

# 9. 30-Second Cheat Sheet

### Recognition

* Prerequisites
* Dependency graph
* Build order
* Course schedule
* Before → After

### Core Idea

* Maintain indegree.
* Process nodes with indegree = 0.
* Remove edges.
* Repeat.

Or:

* DFS postorder → reverse.

### Template

**Kahn (BFS):**

* Build graph
* Compute indegree
* Queue all 0-indegree nodes
* Pop → reduce neighbors' indegree
* Push new 0-indegree nodes
* Check `len(order) == n`

### Complexity

* **Time:** O(V + E)
* **Space:** O(V + E)

### Common Variations

* Kahn's Algorithm (BFS)
* DFS Topological Sort
* Cycle Detection
* Lexicographically Smallest Order (Min-Heap)
* All Topological Orders (Backtracking)

### Pitfalls

* Forget indegree updates
* Forget cycle check
* Using on undirected graph
* Missing 3-state DFS for cycle detection
