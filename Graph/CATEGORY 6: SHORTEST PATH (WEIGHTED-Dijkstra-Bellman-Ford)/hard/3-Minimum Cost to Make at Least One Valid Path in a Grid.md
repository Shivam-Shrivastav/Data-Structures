## 🧠 LeetCode: **Minimum Cost to Make at Least One Valid Path in a Grid**

---

### 1. **Problem Statement with Example**

You are given an `m x n` grid where each cell contains a direction:

* `1 →` right
* `2 ←` left
* `3 ↓` down
* `4 ↑` up

👉 You start at `(0,0)` and want to reach `(m-1,n-1)`.

Rules:

* Moving in the **given direction** → cost = `0`
* Moving in any **other direction** → cost = `1` (you change the arrow)

🎯 Return the **minimum cost** to make at least one valid path.

---

### 2. **Diagram**

```
grid = [
 [1,1,3],
 [3,2,2],
 [1,1,4]
]

Arrows:

→  →  ↓
↓  ←  ←
→  →  ↑
```

You want a path where arrows guide you correctly (or you pay cost to fix them)

---

### 3. **Example I/O**

#### Example 1:

```
Input:
[[1,1,3],
 [3,2,2],
 [1,1,4]]

Output: 0
```

**Why?**

* Already a valid path exists following arrows

---

#### Example 2:

```
Input:
[[1,2],
 [4,3]]

Output: 1
```

**Why?**

* Need to change at least one direction

---

### 4. **Intuition & Pattern Recognition**

🚨 Key signals:

* Grid + shortest path
* Edge weights are only `0` or `1`

👉 This screams:

> **0-1 BFS (Deque BFS)**

---

### 🔥 Interview Thought

> "Weights are only 0 and 1 → use deque instead of heap → 0-1 BFS"

---

### 5. **Simpler Version**

#### Step 1:

👉 Normal BFS (all edges weight = 1)

#### Step 2:

👉 Weighted graph → Dijkstra

#### Step 3:

👉 Only weights {0,1} → optimize Dijkstra → **0-1 BFS**

---

### Related simpler problems:

* Minimum Obstacle Removal to Reach Corner
  → Same 0-1 BFS pattern

* Shortest Path in Binary Matrix
  → Basic BFS

---

### Bridge Thinking:

```
Dijkstra:
  use heap

0-1 BFS:
  use deque
  cost 0 → push front
  cost 1 → push back
```

---

### 6. **Brute Force**

Try all paths:

* Modify directions arbitrarily
* Track cost

❌ Exponential → not feasible

---

### 7. **Optimal Solution (0-1 BFS)**

👉 Use deque:

* If moving in correct direction → push **front**
* Else → push **back**

---

#### Code (Python)

```python
from collections import deque

def minCost(grid):
    m, n = len(grid), len(grid[0])
    
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
    dq = deque([(0, 0, 0)])  # (cost, r, c)
    dist = [[float('inf')] * n for _ in range(m)]
    dist[0][0] = 0
    
    while dq:
        cost, r, c = dq.popleft()
        
        for i, (dr, dc) in enumerate(directions):
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < m and 0 <= nc < n:
                # check if direction matches
                if grid[r][c] == i + 1:
                    new_cost = cost
                else:
                    new_cost = cost + 1
                
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    
                    if new_cost == cost:
                        dq.appendleft((new_cost, nr, nc))
                    else:
                        dq.append((new_cost, nr, nc))
    
    return dist[m-1][n-1]
```

---

### ⏱ Complexity:

* Time: `O(m * n)`
* Space: `O(m * n)`

---

### 8. **Step-by-Step Trace**

Example:

```
[[1,2],
 [4,3]]
```

| Step | Cell  | Cost | Action            |
| ---- | ----- | ---- | ----------------- |
| 1    | (0,0) | 0    | start             |
| 2    | (0,1) | 0    | correct direction |
| 3    | (1,1) | 1    | change direction  |
| 4    | done  | 1    | answer            |

---

### 9. **Related Problems**

1. Minimum Obstacle Removal to Reach Corner
   → Exact same 0-1 BFS idea

2. Path With Minimum Effort
   → Dijkstra variant (minimax)

3. Swim in Rising Water
   → Minimax path

4. Network Delay Time
   → Classic Dijkstra

5. Cheapest Flights Within K Stops
   → Dijkstra with constraints

---

## 🚀 Final Interview Summary

* Recognize:

  ```
  weights ∈ {0,1}
  → 0-1 BFS
  ```
* Replace:

  ```
  heap → deque
  ```
* Key trick:

  ```
  cost 0 → front
  cost 1 → back
  ```

---

If you want, next level:
👉 Convert this into Dijkstra mentally
👉 When NOT to use 0-1 BFS (important trap)
