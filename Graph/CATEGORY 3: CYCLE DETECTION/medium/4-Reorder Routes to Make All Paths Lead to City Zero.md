## 🧩 Reorder Routes to Make All Paths Lead to City Zero (LeetCode 1466)

---

## 1. **Problem statement with example**

You are given:

* `n` cities labeled `0 → n-1`
* `n-1` directed roads (`connections[i] = [a, b]`) meaning **a → b**

You can **reverse any road direction**.

👉 Goal: **Minimum number of edges to reverse** so that **every city can reach city 0**

---

### Example:

```
Input:
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

Output: 3
```

---

## 2. **Diagram**

```
Original graph (directed):

0 → 1 → 3 ← 2
↑
4 → 5

We want all paths → 0

Correct orientation should be:

1 → 0
3 → 1
2 → 3
5 → 4 → 0

Edges to reverse = 3
```

---

## 3. **Example I/O**

### Example 1 (Typical)

```
Input:
n = 3
connections = [[1,0],[2,0]]

Output: 0
```

✔ Already all nodes can reach 0

---

### Example 2 (Edge case)

```
Input:
n = 3
connections = [[0,1],[2,0]]

Output: 1
```

👉 Reverse edge (0 → 1)

---

## 4. **Intuition & pattern recognition**

### 🔑 Signals:

* Tree structure (`n-1` edges)
* Need all nodes to reach **one root (0)**
* Min edge reversals → **count wrong directions**

---

### 💡 Key Idea:

Treat the graph as **undirected**, but:

* Mark original direction
* Traverse from **node 0**
* Count edges pointing **away from 0** (these must be reversed)

---

### 🧠 Interview thought:

> “Root the tree at 0. Every edge going outward from root needs reversal.”

---

## 5. **Simpler version**

### Step 1: Undirected tree traversal

* Just DFS/BFS from node 0

### Step 2: Add direction info

* Each edge has:

  * original direction → cost = 1 (needs reversal)
  * reverse direction → cost = 0

---

### Related simpler problems:

* **Find if Path Exists in Graph** → traversal
* **Number of Provinces** → components
* **Minimum Spanning Tree** → weighted decisions

---

### 🔁 Simpler thinking → actual thinking:

```
Ignore direction → traverse tree
Add direction → count edges pointing wrong way
```

---

## 6. **Brute force**

### Idea:

* Try reversing combinations of edges
* Check if all nodes reach 0

### Complexity:

* ❌ Exponential (2^(n-1))

👉 Not feasible

---

## 7. **Optimal solution (DFS / BFS)**

### ✅ Approach:

1. Build adjacency list:

   * Store `(neighbor, cost)`
   * cost = 1 → original edge (u → v)
   * cost = 0 → reverse edge (v → u)

2. DFS from node `0`

3. Sum all costs

---

### Code (Python)

```python
from collections import defaultdict

def minReorder(n, connections):
    graph = defaultdict(list)
    
    # Build graph
    for u, v in connections:
        graph[u].append((v, 1))  # original direction → needs reversal
        graph[v].append((u, 0))  # reverse direction → correct
    
    visited = set()
    
    def dfs(node):
        visited.add(node)
        changes = 0
        
        for nei, cost in graph[node]:
            if nei not in visited:
                changes += cost  # add if wrong direction
                changes += dfs(nei)
        
        return changes
    
    return dfs(0)
```

---

### Complexity:

* **Time:** O(n)
* **Space:** O(n)

---

## 8. **Step-by-step trace**

### Input:

```
n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
```

---

### Graph representation:

```
0 → 1 (cost 1)
1 → 3 (cost 1)
2 → 3 (cost 1)
4 → 0 (cost 1)
4 → 5 (cost 1)

Reverse edges:
1 → 0 (0), 3 → 1 (0), 3 → 2 (0), 0 → 4 (0), 5 → 4 (0)
```

---

### DFS from 0:

| Step | Node | Neighbor | Cost | Action         | Total |
| ---- | ---- | -------- | ---- | -------------- | ----- |
| 1    | 0    | 1        | 1    | reverse needed | 1     |
| 2    | 1    | 3        | 1    | reverse needed | 2     |
| 3    | 3    | 2        | 0    | ok             | 2     |
| 4    | 0    | 4        | 0    | ok             | 2     |
| 5    | 4    | 5        | 1    | reverse needed | 3     |

---

✅ Final Answer = **3**

---

## 9. **Related problems**

1. **Number of Provinces**
   → Same DFS traversal, no direction

2. **Find if Path Exists in Graph**
   → Basic graph traversal

3. **Minimum Height Trees**
   → Rooting a tree problem

4. **Course Schedule**
   → Directed graph cycle detection

5. **0-1 BFS problems (like Minimum Cost Path)**
   → Edge weights 0/1 similar idea

---

## 🔥 Final Interview Punchline

> “Convert the graph into an undirected one with cost = 1 for original direction and 0 for reverse. Then DFS from node 0 and sum up all costs.”

---

If you want, I can also show:

* ⚡ BFS version (cleaner in interviews)
* 🧠 Trick to solve this in **1 pass without recursion**
