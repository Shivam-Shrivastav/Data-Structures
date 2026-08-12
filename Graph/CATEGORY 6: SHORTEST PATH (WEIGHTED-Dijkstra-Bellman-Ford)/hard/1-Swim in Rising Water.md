## 🧠 LeetCode: **Swim in Rising Water**

---

### 1. **Problem Statement with Example**

You are given an `n x n` grid where:

* `grid[i][j]` = elevation of that cell.
* Water level rises over time `t`.

At time `t`, you can enter any cell with elevation ≤ `t`.

👉 You start at `(0,0)` and want to reach `(n-1,n-1)`.

Return the **minimum time `t`** such that you can reach the destination.

---

### 2. **Diagram**

```
grid = [
 [0, 2],
 [1, 3]
]

Time progression:

t = 0 → only (0,0)
t = 1 → (1,0)
t = 2 → (0,1)
t = 3 → (1,1) ← reachable
```

Graph view (weights = max elevation seen so far):

```
(0)
 / \
1   2
 \ /
 (3)
```

---

### 3. **Example I/O**

#### Example 1:

```
Input:
[[0,2],
 [1,3]]

Output: 3
```

**Why?**

* You must eventually step on `3`
* So minimum time = `3`

---

#### Example 2:

```
Input:
[[0,1,2,3,4],
 [24,23,22,21,5],
 [12,13,14,15,16],
 [11,17,18,19,20],
 [10,9,8,7,6]]

Output: 16
```

**Why?**

* Optimal path avoids large elevations early
* Max elevation encountered = 16

---

### 4. **Intuition & Pattern Recognition**

🚨 Key signals:

* "Minimum time to reach"
* Constraint depends on **maximum value along path**

👉 Equivalent to:

> Minimize the **maximum elevation encountered on the path**

---

### 🔥 Interview Thought

> "This is NOT shortest path sum. It's minimizing the worst cell → Minimax path → Dijkstra variant."

---

### 5. **Simpler Version**

#### Step 1:

👉 Just check reachability if water = `t`

* BFS/DFS allowed

#### Step 2:

👉 Try all `t` → Binary Search

#### Final:

👉 Optimize with Dijkstra

---

### Related simpler problems:

* Path With Minimum Effort
  → Same idea: minimize maximum edge

---

### Bridge Thinking:

```
This problem:
cost = max(grid cell along path)

Path With Minimum Effort:
cost = max(edge difference)

Same pattern → Minimax Dijkstra
```

---

### 6. **Brute Force**

Try all paths:

* Track max elevation
* Return min of all paths

❌ Time: exponential
❌ Not feasible

---

### 7. **Optimal Solution (Dijkstra Variant)**

👉 Use Min Heap:

* `(time, r, c)`
* time = max elevation seen so far

---

#### Code (Python)

```python
import heapq

def swimInWater(grid):
    n = len(grid)
    
    visited = set()
    heap = [(grid[0][0], 0, 0)]  # (time, r, c)
    
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    
    while heap:
        time, r, c = heapq.heappop(heap)
        
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        # reached destination
        if r == n-1 and c == n-1:
            return time
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                new_time = max(time, grid[nr][nc])
                heapq.heappush(heap, (new_time, nr, nc))
```

---

### ⏱ Complexity:

* Time: `O(n^2 log n)`
* Space: `O(n^2)`

---

### 8. **Step-by-Step Trace**

Example:

```
[[0,2],
 [1,3]]
```

| Step | Cell  | Time | Explanation |
| ---- | ----- | ---- | ----------- |
| 1    | (0,0) | 0    | start       |
| 2    | (1,0) | 1    | max(0,1)    |
| 3    | (0,1) | 2    | max(0,2)    |
| 4    | (1,1) | 3    | max(1,3)    |

✅ Answer = 3

---

### 9. **Related Problems**

1. Path With Minimum Effort
   → Same minimax idea (edges instead of nodes)

2. Minimum Obstacle Removal to Reach Corner
   → 0-1 BFS variant

3. Network Delay Time
   → Classic Dijkstra

4. Cheapest Flights Within K Stops
   → Dijkstra with constraints

5. Path With Maximum Probability
   → Maximize instead of minimize

---

## 🚀 Final Interview Summary

* Recognize:

  ```
  "Minimum time" BUT depends on max elevation
  → Minimax Path
  ```
* Replace:

  ```
  sum → max
  ```
* Use:

  * Dijkstra with `max()` transition

---

If you want next level:
👉 Binary Search + BFS approach (very common follow-up)
👉 Union-Find (Kruskal) interpretation (super powerful insight)
