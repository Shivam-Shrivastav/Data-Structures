## 🔹 Problem: Minimum Obstacle Removal to Reach Corner

---

### 1. **Problem Statement with Example**

You are given a `m x n` grid where:

* `0` = empty cell (can move freely)
* `1` = obstacle (can remove it with cost = 1)

You start at `(0,0)` and want to reach `(m-1,n-1)`.

👉 Return the **minimum number of obstacles you need to remove** to reach the destination.

#### Constraints:

* `1 ≤ m, n ≤ 10^5` (total cells ≤ 10^5)
* Movement allowed: up, down, left, right

---

### 2. **Diagram**

```
Grid:
0 1 1
1 1 0
1 1 0

Start → (0,0)
End   → (2,2)

Paths:
(0,0) → (0,1)[1] → (0,2)[1] → (1,2)[0] → (2,2)[0]
Cost = 2

Better path:
(0,0) → (1,0)[1] → (1,1)[1] → (1,2)[0] → (2,2)[0]
Cost = 2
```

We want **minimum cost path**.

---

### 3. **Example I/O**

#### Example 1 (Typical)

```
Input:
grid = [[0,1,1],
        [1,1,0],
        [1,1,0]]

Output: 2
```

#### Example 2 (Edge Case)

```
Input:
grid = [[0,0,0],
        [0,0,0]]

Output: 0
```

👉 No obstacles → straight path

---

### 4. **Intuition & Pattern Recognition**

💡 Key signals:

* Grid + shortest path → think BFS / Dijkstra
* Edge weights are **only 0 or 1**

👉 This screams: **0-1 BFS**

---

### Why not normal BFS?

* BFS assumes equal cost edges
* Here:

  * Move to `0` → cost 0
  * Move to `1` → cost 1

---

### Why 0-1 BFS works?

* Use **deque**
* If cost = 0 → push front
* If cost = 1 → push back

👉 Guarantees shortest path in **O(V + E)**

---

### 5. **Simpler Version**

#### Step 1: Classic BFS

👉 Problem: *Shortest Path in Binary Matrix*

* All moves cost = 1

#### Step 2: Dijkstra

👉 Weighted graph shortest path

#### Step 3: Optimization

👉 If weights are only `{0,1}` → use **0-1 BFS**

---

### Mapping:

| Problem Type     | Algorithm |
| ---------------- | --------- |
| All weights = 1  | BFS       |
| Any weights      | Dijkstra  |
| Only 0/1 weights | 0-1 BFS ✅ |

---

### 6. **Brute Force**

👉 Try all paths (DFS)

```
Explore all paths and track minimum cost
```

❌ Time: Exponential
❌ Not feasible

---

### 7. **Optimal Solution (0-1 BFS)**

```python
from collections import deque

def minimumObstacles(grid):
    m, n = len(grid), len(grid[0])
    
    dq = deque()
    dq.append((0, 0, 0))  # (cost, row, col)
    
    visited = [[float('inf')] * n for _ in range(m)]
    visited[0][0] = 0
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while dq:
        cost, r, c = dq.popleft()
        
        # reached destination
        if r == m-1 and c == n-1:
            return cost
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < m and 0 <= nc < n:
                new_cost = cost + grid[nr][nc]
                
                # relax condition
                if new_cost < visited[nr][nc]:
                    visited[nr][nc] = new_cost
                    
                    if grid[nr][nc] == 0:
                        dq.appendleft((new_cost, nr, nc))  # priority
                    else:
                        dq.append((new_cost, nr, nc))
    
    return -1
```

### Complexity:

* Time: **O(m * n)**
* Space: **O(m * n)**

---

### 8. **Step-by-Step Trace**

Take:

```
grid = [[0,1],
        [1,0]]
```

| Step | Deque             | Current           | Action |
| ---- | ----------------- | ----------------- | ------ |
| 1    | [(0,0,0)]         | (0,0)             | start  |
| 2    | [(1,0,1),(1,1,0)] | move to obstacles |        |
| 3    | [(1,1,0),(1,0,1)] | explore           |        |
| 4    | [(1,1,1)]         | reached end       |        |

✅ Answer = 1

---

### 9. **Related Problems**

1. **Shortest Path in Binary Matrix**
   → BFS with equal weights

2. **Path With Minimum Effort**
   → Dijkstra but with max edge weight

3. **Network Delay Time**
   → Classic Dijkstra

4. **Swim in Rising Water**
   → Priority Queue (min-max path)

5. **Shortest Path in a Grid with Obstacles Elimination**
   → BFS + state (k obstacles allowed)

---

## 🔥 Interview One-Liner

👉 *“Since edges have only 0/1 weights, I’ll use 0-1 BFS with deque instead of Dijkstra.”*

---

If you want, I can also show:

* 🔥 How to derive 0-1 BFS from Dijkstra mentally (very useful in interviews)
* 🔥 Common traps in this problem (visited vs distance confusion)
