## **Shortest Path in a Grid with Obstacles Elimination (LeetCode 1293)**

---

### **1. Problem statement with example**

You are given a grid `m x n` where:

* `0` → empty cell
* `1` → obstacle

You start at `(0,0)` and want to reach `(m-1,n-1)`.

👉 You can move in **4 directions** (up, down, left, right).
👉 You can eliminate **at most `k` obstacles**.

👉 Return the **minimum number of steps** to reach the destination, or `-1` if impossible.

---

**Constraints:**

* `1 <= m, n <= 40`
* `0 <= k <= m*n`
* BFS needed (but with extra state)

---

### **2. Diagram**

Example:

```text
Grid:
0 1 0
0 1 0
0 0 0

k = 1
```

Without elimination:

```text
Blocked path ❌
```

With elimination:

```text
(0,0) → (0,1)[remove] → (0,2)
                        ↓
                     (1,2)
                        ↓
                     (2,2)
```

---

### **3. Example I/O**

#### **Example 1**

```text
Input:
grid = [[0,1,1],
        [1,1,0],
        [1,1,0]]
k = 1

Output: -1
```

---

#### **Example 2**

```text
Input:
grid = [[0,0,0],
        [1,1,0],
        [0,0,0],
        [0,1,1],
        [0,0,0]]
k = 1

Output: 6
```

---

#### **Edge Case**

```text
grid = [[0]]
k = 0

Output: 0
```

---

### **4. Intuition & pattern recognition**

🔑 Signals:

* "shortest path"
* "grid"
* "can remove obstacles (limited resource)"

👉 Classic BFS, BUT:

💡 State is NOT just `(row, col)`
👉 It becomes:

```text
(row, col, remaining_k)
```

---

👉 Why?

Because:

* Reaching same cell with **more k left is better**
* So `(r,c)` alone is NOT enough

---

### **5. Simpler version**

#### **Base problems**

* Shortest Path in Binary Matrix
  → BFS shortest path

* Nearest Exit from Entrance in Maze
  → BFS with condition

---

#### **Build-up**

| Step            | Concept                |
| --------------- | ---------------------- |
| Normal BFS grid | (r,c)                  |
| Add constraint  | need extra state       |
| Track resource  | (r,c,k)                |
| Final problem   | BFS with state pruning |

---

👉 Key jump:

> From **position-only BFS → state BFS**

---

### **6. Brute force**

👉 DFS:

* Try all paths
* Track k usage

❌ Exponential

**Time:** O(4^(m*n))
**Space:** recursion stack

---

### **7. Optimal solution (BFS + state)**

```python
from collections import deque

def shortestPath(grid, k):
    m, n = len(grid), len(grid[0])
    
    # optimization
    if k >= m + n - 2:
        return m + n - 2
    
    # visited[r][c] = max k remaining seen so far
    visited = [[-1] * n for _ in range(m)]
    
    queue = deque([(0, 0, k, 0)])  # r, c, remaining_k, steps
    visited[0][0] = k
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while queue:
        r, c, remaining_k, steps = queue.popleft()
        
        if r == m - 1 and c == n - 1:
            return steps
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < m and 0 <= nc < n:
                new_k = remaining_k - grid[nr][nc]
                
                # if valid and better state
                if new_k >= 0 and visited[nr][nc] < new_k:
                    visited[nr][nc] = new_k
                    queue.append((nr, nc, new_k, steps + 1))
    
    return -1
```

---

### **Complexity**

* **Time:** O(m × n × k)
* **Space:** O(m × n)

---

### **8. Step-by-step trace (core idea)**

Grid:

```text
0 1 0
0 1 0
0 0 0
k = 1
```

---

#### Step 1:

```text
Queue = [(0,0,1,0)]
```

---

#### Step 2:

```text
From (0,0):

→ (0,1): obstacle → k=0
→ (1,0): free → k=1
```

Queue:

```text
[(0,1,0,1), (1,0,1,1)]
```

---

#### Step 3:

```text
From (0,1,0):

→ (0,2) → continue
```

---

#### Key Insight:

👉 If we reach same cell:

* with k=1 → better than k=0
* so we keep only better states

---

### **9. Related problems**

* Shortest Path in Binary Matrix
  → no extra state

* Cheapest Flights Within K Stops
  → BFS with limit

* Minimum Cost to Reach Destination in Time
  → multiple constraints

* Dungeon Game
  → resource management

* Path with Maximum Probability
  → weighted graph version

---

### **🔥 Interview takeaway**

👉 If problem says:

* shortest path
* BUT also gives a constraint (k, cost, stops)

💡 Say:

> **“We need BFS with extended state (r, c, extra parameter)”**

---

### **💡 Golden line to say**

> “Normal BFS fails because reaching a cell with different remaining k leads to different futures, so we must include k in the state.”

---

If you want next, I can give you a **“State BFS cheat sheet”** (covers this, flights with k stops, word ladder, etc.) — super high ROI for interviews.
