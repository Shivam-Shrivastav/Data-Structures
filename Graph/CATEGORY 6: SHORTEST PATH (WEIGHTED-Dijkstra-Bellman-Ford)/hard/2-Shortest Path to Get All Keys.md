## 🧠 LeetCode: **Shortest Path to Get All Keys**

---

### 1. **Problem Statement with Example**

You are given a 2D grid where:

* `'.'` = empty cell
* `'#'` = wall
* `'@'` = starting point
* `'a'–'f'` = keys
* `'A'–'F'` = locks

👉 You can:

* Move in 4 directions
* Pick up keys
* Open a lock **only if you have its corresponding key**

🎯 Goal: Return the **minimum number of steps** to collect **all keys**

#### Constraints:

* Max 6 keys → important (bitmask possible)
* Grid size ≤ 30 x 30

---

### 2. **Diagram**

```
["@.a",
 "###",
 "b.A"]

Grid:

(0,0) @ → start
(0,2) a → key
(2,0) b → key
(2,2) A → lock (needs 'a')
```

State is NOT just position → it’s:

```
(row, col, keys_collected)
```

---

### 3. **Example I/O**

#### Example 1:

```
Input:
["@.a.#","###.#","b.A.B"]

Output: 8
```

**Why?**

* Need to collect both `a` and `b`
* Must unlock `A` using `a`

---

#### Edge Case:

```
Input:
["@Aa"]

Output: -1
```

❌ Can't open `A` (no `a` reachable)

---

### 4. **Intuition & Pattern Recognition**

🚨 Key signals:

* "Shortest path"
* But state changes (keys collected)
* Constraints small → 6 keys → bitmask

👉 Classic:

> **BFS + State Compression (Bitmask BFS)**

---

### 🔥 Interview Thought

> "Position alone is not enough — same cell with different keys is different state → BFS on (r, c, mask)"

---

### 5. **Simpler Version**

#### Step 1:

👉 Normal shortest path in grid
→ BFS

#### Step 2:

👉 Add obstacles (walls)
→ Still BFS

#### Step 3:

👉 Add keys & locks
→ Need **state tracking**

---

### Related simpler problems:

* Shortest Path in Binary Matrix
  → BFS in grid

* Shortest Path with Alternating Colors
  → State-based BFS

---

### Bridge Thinking:

```
Normal BFS:
visited[r][c]

This problem:
visited[r][c][keys_mask]
```

---

### 6. **Brute Force**

* Try all paths
* Track keys manually

❌ Exponential → impossible

---

### 7. **Optimal Solution (BFS + Bitmask)**

👉 State:

```
(r, c, mask)
```

👉 Mask:

* 6 bits → each bit = key collected

Example:

```
a → 000001
b → 000010
mask = 000011 → both collected
```

---

#### Code (Python)

```python
from collections import deque

def shortestPathAllKeys(grid):
    m, n = len(grid), len(grid[0])
    
    # find start + count keys
    total_keys = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':
                start = (i, j)
            elif grid[i][j].islower():
                total_keys = max(total_keys, ord(grid[i][j]) - ord('a') + 1)
    
    final_mask = (1 << total_keys) - 1
    
    queue = deque([(start[0], start[1], 0, 0)])  
    # (r, c, keys_mask, steps)
    
    visited = set()
    visited.add((start[0], start[1], 0))
    
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    
    while queue:
        r, c, mask, steps = queue.popleft()
        
        # collected all keys
        if mask == final_mask:
            return steps
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < m and 0 <= nc < n:
                cell = grid[nr][nc]
                
                if cell == '#':
                    continue
                
                new_mask = mask
                
                # pick key
                if cell.islower():
                    new_mask |= (1 << (ord(cell) - ord('a')))
                
                # lock
                if cell.isupper():
                    if not (mask & (1 << (ord(cell) - ord('A')))):
                        continue
                
                state = (nr, nc, new_mask)
                
                if state not in visited:
                    visited.add(state)
                    queue.append((nr, nc, new_mask, steps + 1))
    
    return -1
```

---

### ⏱ Complexity:

* Time: `O(m * n * 2^k)`
* Space: `O(m * n * 2^k)`
* k ≤ 6 → manageable

---

### 8. **Step-by-Step Trace**

Example:

```
["@.a",
 "###",
 "b.A"]
```

| Step | Position  | Keys | Action        |
| ---- | --------- | ---- | ------------- |
| 1    | (0,0)     | 000  | start         |
| 2    | (0,1)     | 000  | move          |
| 3    | (0,2)     | 001  | pick 'a'      |
| 4    | backtrack | 001  | revisit cells |
| 5    | reach 'A' | 001  | unlock        |
| 6    | reach 'b' | 011  | done          |

---

### 9. **Related Problems**

1. Shortest Path in Binary Matrix
   → Basic BFS grid

2. Minimum Moves to Reach Target with Rotations
   → State BFS (position + orientation)

3. Sliding Puzzle
   → BFS with state encoding

4. Shortest Path with Alternating Colors
   → BFS with extra state

5. Minimum Obstacle Removal to Reach Corner
   → BFS + cost variation

---

## 🚀 Final Interview Summary

* Recognize:

  ```
  Grid + shortest path + changing state
  → BFS + Bitmask
  ```
* Key idea:

  ```
  (r, c, mask) not just (r, c)
  ```
* Why BFS?
  → uniform cost (1 step)

---

If you want, next level:
👉 Optimization tricks (pruning states faster)
👉 How to identify bitmask problems instantly (very important pattern)
