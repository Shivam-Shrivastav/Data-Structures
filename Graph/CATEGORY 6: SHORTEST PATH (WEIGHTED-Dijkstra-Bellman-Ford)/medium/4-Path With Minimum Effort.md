## 🧠 LeetCode: **Path With Minimum Effort**

---

### 1. **Problem Statement with Example**

You are given a 2D grid `heights` where `heights[i][j]` represents the height of a cell.

You start from `(0,0)` and want to reach `(m-1,n-1)`.

* You can move in 4 directions (up, down, left, right).
* The **effort of a path** = **maximum absolute difference between heights of adjacent cells** along the path.

👉 Return the **minimum effort required** to reach the destination.

#### Constraints:

* `1 ≤ m, n ≤ 100`
* Heights up to `10^6`
* Key: **minimize the maximum edge weight (not sum!)**

---

### 2. **Diagram**

```
heights = [
  [1, 2, 2],
  [3, 8, 2],
  [5, 3, 5]
]

Grid with edge differences:

(1)--1--(2)--0--(2)
 |       |       |
2        6       0
 |       |       |
(3)--5--(8)--6--(2)
 |       |       |
2        5       3
 |       |       |
(5)--2--(3)--2--(5)
```

Goal: Path minimizing **maximum edge difference**

---

### 3. **Example I/O**

#### Example 1:

```
Input:
[[1,2,2],
 [3,8,2],
 [5,3,5]]

Output: 2
```

**Why?**
Best path:

```
1 → 2 → 2 → 2 → 5
Differences = [1,0,0,3] → max = 3 ❌

Better:
1 → 3 → 5 → 3 → 5
Differences = [2,2,2,2] → max = 2 ✅
```

---

#### Edge Case:

```
Input: [[1]]
Output: 0
```

Single cell → no effort

---

### 4. **Intuition & Pattern Recognition**

🚨 Key signal:

* "Minimize the **maximum** cost along path"
* NOT sum → NOT normal shortest path

👉 This is a **Minimax Path Problem**

💡 Patterns that fit:

* Modified **Dijkstra**
* OR **Binary Search + BFS**
* OR **Union Find (Kruskal)**

---

### 🔥 Interview Thought:

> "Since cost = max edge, I should minimize worst edge → modify Dijkstra where distance = max so far instead of sum."

---

### 5. **Simpler Version**

#### Simplest:

👉 Normal shortest path (sum of weights)

* e.g. Network Delay Time

#### Next level:

👉 Minimize max edge:

* This problem

#### Related simpler thinking:

* Instead of `dist[u] + weight`
* Think: `max(dist[u], weight)`

---

### Bridge Thinking:

```
Sum problem:     minimize total
This problem:    minimize worst step
```

---

### 6. **Brute Force**

Try all paths (DFS):

* Track max effort for each path
* Return minimum among them

❌ Time: `O(4^(m*n))` → impossible
❌ Space: recursion stack

---

### 7. **Optimal Solution (Dijkstra Variant)**

👉 Use **Min Heap**

* Store `(effort, row, col)`
* Instead of sum → store max effort so far

---

#### Code (Python)

```python
import heapq

def minimumEffortPath(heights):
    m, n = len(heights), len(heights[0])
    
    # effort matrix
    effort = [[float('inf')] * n for _ in range(m)]
    effort[0][0] = 0
    
    heap = [(0, 0, 0)]  # (effort, r, c)
    
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    
    while heap:
        curr_eff, r, c = heapq.heappop(heap)
        
        # reached destination
        if r == m-1 and c == n-1:
            return curr_eff
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < m and 0 <= nc < n:
                # edge weight
                diff = abs(heights[r][c] - heights[nr][nc])
                
                # key logic: take max
                new_eff = max(curr_eff, diff)
                
                if new_eff < effort[nr][nc]:
                    effort[nr][nc] = new_eff
                    heapq.heappush(heap, (new_eff, nr, nc))
    
    return 0
```

---

### ⏱ Complexity:

* Time: `O(m * n * log(m*n))`
* Space: `O(m*n)`

---

### 8. **Step-by-Step Trace**

Example:

```
[[1,2,2],
 [3,8,2],
 [5,3,5]]
```

| Step | Cell  | Current Effort | Action      |
| ---- | ----- | -------------- | ----------- |
| 1    | (0,0) | 0              | Start       |
| 2    | (0,1) | 1              | max(0,1)    |
| 3    | (1,0) | 2              | max(0,2)    |
| 4    | (0,2) | 1              | better path |
| 5    | (1,2) | 1              | continues   |
| 6    | (2,2) | 2              | final       |

✅ Answer = 2

---

### 9. **Related Problems**

1. Network Delay Time
   → Classic Dijkstra (sum instead of max)

2. Path With Maximum Probability
   → Maximize product (similar modification)

3. Swim in Rising Water
   → Same minimax pattern

4. Cheapest Flights Within K Stops
   → Dijkstra variant with constraints

5. Minimum Obstacle Removal to Reach Corner
   → 0-1 BFS variant

---

## 🚀 Final Interview Summary

* Recognize: **Minimize maximum edge → Minimax path**
* Replace:

  ```
  dist + weight   ❌
  max(dist, weight) ✅
  ```
* Use:

  * Dijkstra (most common)
  * OR Binary Search + BFS (follow-up)

---

If you want, I can also give:
👉 Binary Search approach
👉 Union-Find (Kruskal) version (very powerful insight)
