## 🧩 Shortest Cycle in a Graph (LeetCode 2608)

---

## 1. **Problem statement with example**

You are given:

* `n` nodes (0 → n-1)
* `edges` (undirected graph)

👉 Return the **length of the shortest cycle** in the graph.
If no cycle exists → return `-1`

---

### Example:

```
Input:
n = 7
edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]

Output: 3
```

👉 Cycle: `0 → 1 → 2 → 0` (length = 3)

---

### Constraints:

* 2 ≤ n ≤ 1000
* Undirected graph
* Can be disconnected

---

## 2. **Diagram**

```
Component 1:
0 — 1
 \  |
   2   → cycle length = 3

Component 2:
3 — 4
|   |
6 — 5   → cycle length = 4

Answer = min(3,4) = 3
```

---

## 3. **Example I/O**

### Example 1 (Typical)

```
Input:
n = 4
edges = [[0,1],[1,2],[2,3]]

Output: -1
```

❌ No cycle

---

### Example 2 (Edge case)

```
Input:
n = 3
edges = [[0,1],[1,2],[2,0]]

Output: 3
```

✔ Smallest possible cycle

---

## 4. **Intuition & pattern recognition**

### 🔑 Signals:

* “Shortest cycle” → **minimum path forming a loop**
* Unweighted graph → **BFS**
* Need shortest → BFS beats DFS

---

### 💡 Key idea:

👉 Run **BFS from every node**

While BFS:

* Track `parent`
* If you visit an already visited node **not parent → cycle**
* Compute cycle length using distances

---

### 🧠 Interview thought:

> “Shortest path + cycle → BFS from every node with parent tracking”

---

## 5. **Simpler version**

### Step 1:

* Detect if cycle exists → DFS

### Step 2:

* Find shortest path → BFS

### Step 3:

* Combine both → BFS with cycle detection

---

### Related simpler problems:

* **Detect Cycle in Undirected Graph** → DFS/BFS
* **Shortest Path in Unweighted Graph** → BFS
* **Number of Provinces** → traversal

---

### 🔁 Thinking progression:

```
Cycle detection → shortest path → BFS + parent → shortest cycle
```

---

## 6. **Brute force**

### Idea:

* Try all paths
* Check cycles

### Complexity:

* ❌ Exponential

---

## 7. **Optimal solution (BFS from every node)**

---

### ✅ Algorithm:

For each node:

1. Run BFS
2. Maintain:

   * `distance[]`
   * `parent[]`
3. If neighbor is visited AND not parent:
   → cycle found
   → length = dist[u] + dist[v] + 1

Take minimum over all

---

### Code (Python)

```python
from collections import defaultdict, deque

def findShortestCycle(n, edges):
    graph = defaultdict(list)
    
    # build graph
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    ans = float('inf')
    
    for start in range(n):
        dist = [-1] * n
        parent = [-1] * n
        
        q = deque([start])
        dist[start] = 0
        
        while q:
            node = q.popleft()
            
            for nei in graph[node]:
                if dist[nei] == -1:
                    dist[nei] = dist[node] + 1
                    parent[nei] = node
                    q.append(nei)
                elif parent[node] != nei:
                    # cycle found
                    cycle_len = dist[node] + dist[nei] + 1
                    ans = min(ans, cycle_len)
    
    return ans if ans != float('inf') else -1
```

---

### Complexity:

* **Time:** O(n * (n + e))
* **Space:** O(n + e)

👉 Works because n ≤ 1000

---

## 8. **Step-by-step trace**

### Input:

```
n = 3
edges = [[0,1],[1,2],[2,0]]
```

---

### BFS from node 0:

| Step | Node | Neighbor | Action                       | Dist | Cycle? |
| ---- | ---- | -------- | ---------------------------- | ---- | ------ |
| 1    | 0    | 1        | visit                        | 1    | -      |
| 2    | 0    | 2        | visit                        | 1    | -      |
| 3    | 1    | 2        | already visited & not parent | -    | ✅      |

Cycle length:

```
dist[1] + dist[2] + 1 = 1 + 1 + 1 = 3
```

---

## 9. **Related problems**

1. **Detect Cycle in Undirected Graph**
   → Same logic without shortest constraint

2. **Shortest Path in Binary Matrix**
   → BFS shortest path

3. **Minimum Height Trees**
   → Tree center logic

4. **Word Ladder**
   → BFS shortest transformation

5. **Bus Routes**
   → BFS on graph with layers

---

## 🔥 Final Interview Punchline

> “Run BFS from every node, track parent to avoid trivial back edges, and compute cycle length using distances when revisiting a node.”

---

If you want, I can also show:

* ⚡ Optimization tricks (reduce BFS runs)
* 🧠 Why DFS fails for shortest cycle (important insight)
