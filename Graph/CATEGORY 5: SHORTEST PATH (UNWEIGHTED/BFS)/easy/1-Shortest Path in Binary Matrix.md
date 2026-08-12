## **Shortest Path in Binary Matrix (LeetCode 1091)**

---

### **1. Problem statement with example**

You are given an `n x n` binary matrix `grid` where:

* `0` → open cell
* `1` → blocked cell

You start at **top-left (0,0)** and want to reach **bottom-right (n-1,n-1)**.

You can move in **8 directions**:

* up, down, left, right
* 4 diagonals

👉 Return the **length of the shortest path** from start to end.
👉 If no such path exists → return `-1`.

**Constraints:**

* `1 <= n <= 100`
* BFS fits (since unweighted shortest path)
* Grid size manageable → O(n²)

---

### **2. Diagram**

Example grid:

```
0 1 0
0 0 0
1 0 0
```

Movement (8 directions allowed):

```
Start (0,0)

   ↘
      ↘
         → End (2,2)
```

Shortest path visually:

```
(0,0) → (1,1) → (2,2)
```

---

### **3. Example I/O**

#### **Example 1**

```
Input:
grid = [[0,1],[1,0]]

Output: 2

Explanation:
(0,0) → (1,1)
```

#### **Example 2**

```
Input:
grid = [[0,0,0],
        [1,1,0],
        [1,1,0]]

Output: 4

Explanation:
(0,0) → (0,1) → (1,2) → (2,2)
```

#### **Edge Case**

```
Input:
grid = [[1]]

Output: -1

Explanation:
Start is blocked
```

---

### **4. Intuition & pattern recognition**

🔑 Signals:

* "Shortest path"
* "Unweighted grid"
* "Move in directions"

👉 Immediately think: **BFS**

Why?

* BFS guarantees shortest path in **unweighted graphs**
* Each move = cost 1

👉 Grid = Graph:

* Each cell = node
* Edges = 8 directions

---

### **5. Simpler version**

#### **Simpler Problem**

👉 "Shortest path in grid with only 4 directions"

Example:

* Number of Islands (exploration)
* Rotting Oranges (BFS layering)
* 01 Matrix (distance BFS)

---

#### **How this builds up**

| Simpler Step          | What you learn      |
| --------------------- | ------------------- |
| DFS grid traversal    | how to move in grid |
| BFS in grid           | shortest path       |
| Multi-direction moves | handle neighbors    |
| This problem          | + diagonal moves    |

👉 Only difference here:

* **8 directions instead of 4**
* **Return path length, not traversal**

---

### **6. Brute force**

👉 Try all paths using DFS

* Explore all possible paths
* Track minimum length

❌ Problem:

* Exponential time
* TLE

**Time:** O(8^(n²))
**Space:** recursion stack

---

### **7. Optimal solution (BFS)**

```python
from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    
    # If start or end blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    # 8 directions
    directions = [
        (1,0), (-1,0), (0,1), (0,-1),
        (1,1), (1,-1), (-1,1), (-1,-1)
    ]
    
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    grid[0][0] = 1  # mark visited
    
    while queue:
        r, c, dist = queue.popleft()
        
        # reached destination
        if r == n-1 and c == n-1:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # valid cell and not visited
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                queue.append((nr, nc, dist + 1))
                grid[nr][nc] = 1  # mark visited
    
    return -1
```

---

### **Complexity**

* **Time:** O(n²) → each cell visited once
* **Space:** O(n²) → queue

---

### **8. Step-by-step trace**

Grid:

```
0 1 0
0 0 0
1 0 0
```

#### Initial:

```
Queue = [(0,0,1)]
```

---

#### Step 1:

```
Pop (0,0,1)

Push neighbors:
(1,0,2), (1,1,2)
```

Queue:

```
[(1,0,2), (1,1,2)]
```

---

#### Step 2:

```
Pop (1,0,2)

Push:
(2,1,3)
```

Queue:

```
[(1,1,2), (2,1,3)]
```

---

#### Step 3:

```
Pop (1,1,2)

Push:
(2,2,3) ← destination
```

---

#### Step 4:

```
Pop (2,2,3) → return 3
```

---

### **9. Related problems**

* Rotting Oranges
  → BFS layer expansion across grid

* 01 Matrix
  → Distance from nearest zero

* Walls and Gates
  → BFS from multiple sources

* Shortest Path in Grid with Obstacles Elimination
  → BFS + extra state (k obstacles)

* Minimum Knight Moves
  → BFS with custom movement pattern

---

### **Interview takeaway**

👉 Whenever you see:

* shortest path
* grid
* equal cost moves

💡 Say immediately:

> "This is BFS on grid (unweighted shortest path)"

---

If you want, I can give you a **pattern template for all BFS grid problems** so you can solve 90% of them instantly.
