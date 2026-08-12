## 🔹 Unique Paths III (Backtracking + Grid DFS)

---

## 1. Problem Statement with Example

You are given a grid where:

* `1` = starting square (exactly one)
* `2` = ending square (exactly one)
* `0` = empty square (walkable)
* `-1` = obstacle (blocked)

👉 Return the number of **unique paths** from start → end such that:

* You visit **every non-obstacle cell exactly once**
* You move in **4 directions (up, down, left, right)**

---

### Example

```id="8q8c3x"
Input:
grid = [
 [1,0,0,0],
 [0,0,0,0],
 [0,0,2,-1]
]

Output: 2
```

---

### Constraints

* Grid size ≤ 20 cells (very small → backtracking)
* Must visit **all empty cells exactly once**

---

## 2. Diagram (Path Coverage Idea)

```id="3xgaf4"
Grid:

1 . . .
. . . .
. . 2 X

Valid path example:

1 → → ↓ ↓ ← ↓ → → ↑ → 2

(Every empty cell visited exactly once)
```

👉 This is like **Hamiltonian path on grid**

---

## 3. Example I/O

### Example 1 (Typical)

```id="2ns5dp"
Input:
[[1,0,0,0],
 [0,0,0,0],
 [0,0,2,-1]]

Output: 2
```

---

### Example 2

```id="3ry6y3"
Input:
[[1,0,0],
 [0,0,0],
 [0,2,-1]]

Output: 1
```

---

### Example 3 (Edge Case)

```id="ivulmp"
Input:
[[1,2]]
Output: 1
```

---

## 4. Intuition & Pattern Recognition

### 🚨 Signals

* “Visit all cells exactly once”
* “Count number of valid paths”
* “Small grid”

👉 This screams:

> **Backtracking + DFS with state tracking**

---

### Core Idea

We need:

* Start from `1`
* Walk through all `0`s
* End at `2`
* Ensure all non-obstacle cells are visited

---

### Key Trick

👉 Count total walkable cells (`empty + start`)

Then during DFS:

* Decrease count when visiting
* When reaching `2`, check:

  ```
  remaining_cells == 0
  ```

---

### Interview Thought

> “This is a DFS where I explore all paths but only count those that visit every empty cell exactly once.”

---

## 5. Simpler Version

### Step 1: Basic Grid DFS

👉 **Number of Islands**

* Explore connected cells

---

### Step 2: Path Constraints

👉 **Word Search**

* Cannot revisit cells

---

### Step 3: Combine

👉 Current problem =

* DFS + visit all cells exactly once + count paths

---

### Thinking Flow

```id="44smzj"
DFS from start
   ↓
Track visited cells
   ↓
Check if all cells covered when reaching end
```

---

## 6. Brute Force

### Idea

* Try all paths from start to end

### Complexity

* Time: **O(4^n)** (n = cells)

---

## 7. Optimal Solution (Backtracking)

---

### Code

```python id="uyz0bl"
class Solution:
    def uniquePathsIII(self, grid):
        rows, cols = len(grid), len(grid[0])
        empty = 0
        
        # find start and count empty cells
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    empty += 1
                elif grid[r][c] == 1:
                    start = (r, c)
        
        def dfs(r, c, remain):
            # out of bounds or obstacle
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == -1):
                return 0
            
            # reached end
            if grid[r][c] == 2:
                return 1 if remain == -1 else 0
            
            # mark visited
            temp = grid[r][c]
            grid[r][c] = -1
            
            total = 0
            
            # explore 4 directions
            total += dfs(r+1, c, remain-1)
            total += dfs(r-1, c, remain-1)
            total += dfs(r, c+1, remain-1)
            total += dfs(r, c-1, remain-1)
            
            # backtrack
            grid[r][c] = temp
            
            return total
        
        return dfs(start[0], start[1], empty)
```

---

### Complexity

* Time: **O(4^n)**
* Space: O(n)

---

## 8. Step-by-Step Trace

### Input

```id="5gn3or"
[[1,0,2]]
```

---

### Setup

```id="hkvp6a"
empty = 1
start = (0,0)
```

---

### DFS

| Step | Position | Remaining | Action |
| ---- | -------- | --------- | ------ |
| 1    | (0,0)    | 1         | start  |
| 2    | (0,1)    | 0         | visit  |
| 3    | (0,2)    | -1        | end ✔  |

👉 Valid path → count = 1

---

## 9. Related Problems

1. **Word Search**
   → DFS + backtracking on grid

2. **Path with Maximum Gold**
   → Visit cells once, maximize score

3. **Number of Islands**
   → Basic DFS traversal

4. **Shortest Path in Binary Matrix**
   → Grid traversal (BFS)

5. **The Maze**
   → Pathfinding with constraints

---

## 🔥 Interview One-Liner

👉 *“I perform DFS from the start, marking cells as visited and only count paths that reach the end after visiting every empty cell exactly once.”*

---

If you want, I can next show:

* ⚡ **Bitmask optimization (advanced)**
* ⚡ Why this is similar to **Hamiltonian path (graph theory insight)**
* ⚡ Common mistakes (VERY frequently asked in interviews)
