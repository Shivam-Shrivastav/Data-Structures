## **Largest Color Value in a Directed Graph (LeetCode)**

---

## 1. **Problem statement with example**

You are given:

* A **directed graph** with `n` nodes (0 → n-1)
* A string `colors` where `colors[i]` is the color of node `i`
* An array `edges` where `edges[i] = [u, v]` means a directed edge `u → v`

### Goal:

Return the **maximum number of nodes of the same color** in any **valid path**.

👉 If the graph contains a **cycle**, return `-1`.

### Constraints:

* `1 <= n <= 10^5`
* `0 <= edges.length <= 10^5`
* Colors are lowercase English letters

---

## 2. **Diagram**

```
colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]

Graph:

    0(a)
   /   \
  v     v
 1(b)  2(a)
         |
         v
        3(c)
         |
         v
        4(a)
```

👉 Path: `0 → 2 → 3 → 4`
Colors: `a → a → c → a` → count of `a = 3`

---

## 3. **Example I/O**

### Example 1 (Typical)

```
Input:
colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]

Output:
3
```

**Why:** Path `0 → 2 → 3 → 4` has 3 `'a'`

---

### Example 2 (Cycle case)

```
Input:
colors = "a"
edges = [[0,0]]

Output:
-1
```

**Why:** Self-loop → cycle → invalid

---

## 4. **Intuition & pattern recognition**

### 🔑 Key signals:

* Directed graph
* Path-based maximum
* Cycle invalidates result
* Frequency of colors along path

👉 This screams:

> **Topological Sort + DP on DAG**

### Core idea:

* If **cycle exists → return -1**
* Otherwise:

  * Process nodes in **topological order**
  * Maintain:

    ```
    dp[node][color] = max count of that color till this node
    ```

### Why this works:

* DAG ensures **no revisiting**
* Topo order ensures **dependencies processed first**
* Each node aggregates best counts from parents

---

## 5. **Simpler version**

### Simplest problem:

👉 "Find longest path in DAG"

* No colors → just length
* Solve using **topological + DP**

---

### Slightly harder:

👉 "Track max frequency of one fixed color in path"

* Only 1 color → easier DP

---

### This problem:

👉 Track **26 colors simultaneously**

```
Instead of:
dp[node] = max length

We do:
dp[node][26] = frequency of each color
```

---

### Related simpler problems:

* **Longest Path in DAG**
* **Course Schedule II** → topo sort
* **Parallel Courses III** → DP + topo

---

## 6. **Brute force**

### Idea:

* Try all paths using DFS
* Track frequency map
* Take max

### Problem:

* Exponential paths → TLE

### Complexity:

* Time: **O(2^n)** (worst)
* Space: **O(n)** recursion

❌ Not feasible

---

## 7. **Optimal solution (Topo + DP)**

### Steps:

1. Build graph + indegree
2. Start BFS (Kahn's algo)
3. Maintain:

   ```
   dp[node][26]
   ```
4. For each node:

   * Increment its own color
   * Push updates to neighbors

---

### Code (Python)

```python
from collections import deque, defaultdict

def largestPathValue(colors, edges):
    n = len(colors)
    graph = defaultdict(list)
    indegree = [0] * n
    
    # Build graph
    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1
    
    # dp[node][color]
    dp = [[0] * 26 for _ in range(n)]
    
    # Queue for topo sort
    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    
    visited = 0
    res = 0
    
    while q:
        node = q.popleft()
        visited += 1
        
        # Update current node color
        color_idx = ord(colors[node]) - ord('a')
        dp[node][color_idx] += 1
        
        res = max(res, dp[node][color_idx])
        
        # Visit neighbors
        for nei in graph[node]:
            for c in range(26):
                dp[nei][c] = max(dp[nei][c], dp[node][c])
            
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)
    
    # Cycle check
    return res if visited == n else -1
```

---

### Complexity:

* Time: **O((V + E) * 26)** ≈ O(V + E)
* Space: **O(V * 26)**

---

## 8. **Step-by-step trace**

### Input:

```
colors = "abaca"
edges = [[0,1],[0,2],[2,3],[3,4]]
```

### Initial:

```
indegree = [0,1,1,1,1]
queue = [0]
```

---

### Step 1: Node 0

```
dp[0]['a'] = 1

→ push to 1 and 2
dp[1]['a'] = 1
dp[2]['a'] = 1
```

---

### Step 2: Node 1

```
dp[1]['b'] = 1
(no outgoing edges)
```

---

### Step 3: Node 2

```
dp[2]['a'] = 2
→ push to 3
dp[3]['a'] = 2
```

---

### Step 4: Node 3

```
dp[3]['c'] = 1
→ push to 4
dp[4]['a'] = 2
```

---

### Step 5: Node 4

```
dp[4]['a'] = 3
```

---

### Final:

```
max = 3
```

---

## 9. **Related problems**

1. **Course Schedule II**
   → Classic topo sort ordering

2. **Parallel Courses III**
   → DP + topo (time accumulation)

3. **Longest Increasing Path in Matrix**
   → DAG + DP on paths

4. **All Paths From Source to Target**
   → Path exploration in DAG

5. **Shortest Path in DAG**
   → DP propagation across topo order

---

## 🚀 Interview takeaway

If you see:

* **Directed graph**
* **Path optimization**
* **Cycle invalid**
* **Aggregate values along path**

👉 Immediately think:

> **Topo Sort + DP over nodes (state propagation)**

---

If you want, I can give you:

* Java version
* Memory optimization trick (reduce 26 factor thinking)
* Or how to derive this in interview step-by-step without memorizing
