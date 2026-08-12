## 🔷 **Max Area of Island (LeetCode 695)**

---

## 1. **Problem statement with example**

You are given a 2D grid of size `m x n` containing only `0`s and `1`s:

* `1` → land
* `0` → water

An **island** is a group of connected `1`s (connected **4-directionally**: up, down, left, right).

👉 Return the **maximum area** of an island in the grid.
If no island exists → return `0`.

### **Constraints**

* `1 <= m, n <= 50`
* Grid contains only `0` or `1`
* Must visit each cell efficiently → avoid reprocessing

---

## 2. **Diagram**

```
Grid:
[
  [0,0,1,0],
  [1,1,1,0],
  [0,1,0,0]
]

Island shape:

      1
    1 1 1
      1

Area = 5
```

👉 You explore connected `1`s and count size.

---

## 3. **Example I/O**

### ✅ Example 1 (Typical)

```
Input:
grid = [
  [0,0,1,0],
  [1,1,1,0],
  [0,1,0,0]
]

Output: 5
```

**Explanation:** One island of size 5.

---

### ⚠️ Example 2 (Edge case)

```
Input:
grid = [
  [0,0,0],
  [0,0,0]
]

Output: 0
```

**Explanation:** No land.

---

## 4. **Intuition & pattern recognition**

### 🔍 Signals:

* Grid → think **Graph**
* Connected components → **DFS / BFS**
* Need size → **count nodes in component**

👉 Key idea:

> “For every unvisited `1`, explore its full island and compute its area.”

### 🧠 Interview thought:

* "This is a connected components problem in a grid"
* "Use DFS to expand island"
* "Track visited to avoid cycles"

---

## 5. **Simpler version**

### 🔹 Simpler problem:

👉 “Count number of islands” → Number of Islands

### 🔗 Relation:

* That problem → count islands
* This problem → **measure island size**

### ⚡ Difference:

* Instead of just marking visited → also **count area**

---

## 6. **Brute force**

### Idea:

* For each cell:

  * If `1`, do DFS
  * Use a separate visited matrix
  * Compute area

### Complexity:

* Time: `O(m * n)`
* Space: `O(m * n)` (visited + recursion)

👉 Not optimal due to extra space.

---

## 7. **Optimal solution (DFS - in-place marking)**

### ✅ Approach:

* Traverse grid
* When `1` found:

  * Run DFS
  * Convert visited `1 → 0` (mark visited)
  * Count area
* Track max

---

### 💻 Code (Python)

```python
class Solution:
    def maxAreaOfIsland(self, grid):
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # boundary + water check
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                return 0
            
            # mark visited
            grid[r][c] = 0
            
            # explore all directions
            area = 1
            area += dfs(r+1, c)  # down
            area += dfs(r-1, c)  # up
            area += dfs(r, c+1)  # right
            area += dfs(r, c-1)  # left
            
            return area
        
        max_area = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area
```

### ⏱ Complexity:

* Time: `O(m * n)` (each cell visited once)
* Space: `O(m * n)` worst-case recursion stack

---

## 8. **Step-by-step trace**

### Input:

```
[
 [0,0,1,0],
 [1,1,1,0],
 [0,1,0,0]
]
```

### Steps:

| Step | Cell   | Action    | Area |
| ---- | ------ | --------- | ---- |
| 1    | (0,2)  | Start DFS | 1    |
| 2    | (1,2)  | Expand    | 2    |
| 3    | (1,1)  | Expand    | 3    |
| 4    | (1,0)  | Expand    | 4    |
| 5    | (2,1)  | Expand    | 5    |
| 6    | Others | Stop      | 5    |

👉 Max area = **5**

---

## 9. **Related problems**

1. Number of Islands
   → Same DFS pattern, but count components instead of size.

2. Island Perimeter
   → Instead of area, compute boundary.

3. Surrounded Regions
   → DFS from borders to protect regions.

4. Flood Fill
   → Same traversal, just recoloring.

5. Max Area of Island II
   → Uses Union-Find for dynamic updates.

---

## ⚡ Final Interview Takeaway

👉 Whenever you see:

* Grid + connected cells + max/min size
  → Think **DFS + connected component size**

👉 Mental shortcut:

> “Start DFS on every unvisited land, count size, take max.”

---

If you want, I can also give **BFS version + Union-Find version + iterative DFS (no recursion)** — these are follow-up interview questions.
