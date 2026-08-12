## 463. Island Perimeter
**Category:** **GRAPH / MATRIX TRAVERSAL**

**Problem:** You are given a 2D grid map of `1`s (land) and `0`s (water). Grid cells are connected horizontally/vertically. The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). Determine the **perimeter** of the island.

**Example:**
```
Input: grid = [[0,1,0,0],
               [1,1,1,0],
               [0,1,0,0],
               [1,1,0,0]]
Output: 16
```

```
Input: grid = [[1]]
Output: 4
```

```
Input: grid = [[1,0]]
Output: 4
```

---

### **Relation to Number of Islands**
**Similar to:** **Number of Islands (200)** but calculate perimeter instead of count
**How it's different:**
1. **Number of Islands:** Count connected components
2. **Island Perimeter:** Calculate boundary length of single island
3. **Key Insight:** Each land cell contributes 4 to perimeter, but subtract 2 for each adjacent land cell (shared edge counted twice)

**Key Insight:** 
- Each land cell has 4 sides
- For each adjacent land cell, 2 sides are shared (one from each cell)
- Total perimeter = (4 × number of land cells) - (2 × number of adjacent land pairs)

---

### 1. Brute Force (Count cells and adjacencies)
```python
def islandPerimeter(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    land_cells = 0
    adjacent_pairs = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                land_cells += 1
                
                # Check right neighbor
                if j + 1 < n and grid[i][j+1] == 1:
                    adjacent_pairs += 1
                
                # Check down neighbor
                if i + 1 < m and grid[i+1][j] == 1:
                    adjacent_pairs += 1
    
    return 4 * land_cells - 2 * adjacent_pairs
```
**TC:** O(m × n) | **SC:** O(1)

---

### 2. DFS Approach (Count exposed sides)
```python
def islandPerimeter(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    perimeter = 0
    
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return 1  # Water or boundary contributes 1 to perimeter
        
        if visited[i][j]:
            return 0  # Already counted
        
        visited[i][j] = True
        
        # Count exposed sides from 4 directions
        return (dfs(i+1, j) + 
                dfs(i-1, j) + 
                dfs(i, j+1) + 
                dfs(i, j-1))
    
    # Find first land cell
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                return dfs(i, j)
    
    return 0
```
**TC:** O(m × n) | **SC:** O(m × n) worst case

---

### 3. BFS Approach
```python
from collections import deque

def islandPerimeter(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    perimeter = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    # Find first land cell
    start_i, start_j = -1, -1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                start_i, start_j = i, j
                break
        if start_i != -1:
            break
    
    if start_i == -1:
        return 0
    
    queue = deque([(start_i, start_j)])
    visited[start_i][start_j] = True
    
    while queue:
        i, j = queue.popleft()
        
        # Check all 4 neighbors
        for di, dj in directions:
            ni, nj = i + di, j + dj
            
            if ni < 0 or ni >= m or nj < 0 or nj >= n or grid[ni][nj] == 0:
                perimeter += 1  # Water or boundary contributes
            elif not visited[ni][nj]:
                visited[ni][nj] = True
                queue.append((ni, nj))
    
    return perimeter
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 4. Simple Iterative (Count edges to water)
```python
def islandPerimeter(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    perimeter = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                # Check 4 directions for water or boundary
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1  # Top edge
                if i == m-1 or grid[i+1][j] == 0:
                    perimeter += 1  # Bottom edge
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1  # Left edge
                if j == n-1 or grid[i][j+1] == 0:
                    perimeter += 1  # Right edge
    
    return perimeter
```
**TC:** O(m × n) | **SC:** O(1)

---

### 5. Optimized Counting
```python
def islandPerimeter(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    perimeter = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                perimeter += 4
                
                # Subtract 2 for each adjacent land (since shared edge counted twice)
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    
    return perimeter
```
**TC:** O(m × n) | **SC:** O(1)

---

**Key Formula:**
```
Method 1: perimeter = 4*land - 2*adjacent_pairs
Method 2: For each land cell, count sides adjacent to water/boundary
```

**Example Walkthrough:**
```
grid = [
  [0,1,0,0],
  [1,1,1,0],
  [0,1,0,0],
  [1,1,0,0]
]

Method 1 (Count cells and adjacencies):
Land cells = 7
Adjacent pairs (right + down):
  (0,1)-(0,2): no (0,2 is 0)
  (0,1)-(1,1): yes
  (1,0)-(1,1): yes
  (1,1)-(1,2): yes
  (1,1)-(2,1): yes
  (1,2)-(1,3): no (1,3 is 0)
  (1,2)-(2,2): yes
  (2,1)-(2,2): no (2,2 is 0)
  (2,1)-(3,1): yes
  (3,0)-(3,1): yes
  (3,1)-(3,2): no (3,2 is 0)
Count = 8 adjacent pairs
Perimeter = 4*7 - 2*8 = 28 - 16 = 12? Wait that's wrong! Let's recount:

Actually adjacent_pairs count each shared edge once.
Right neighbors:
  (0,1)-(0,2): 0
  (1,0)-(1,1): 1
  (1,1)-(1,2): 1
  (1,2)-(1,3): 0
  (2,1)-(2,2): 0
  (3,0)-(3,1): 1
  (3,1)-(3,2): 0
Down neighbors:
  (0,1)-(1,1): 1
  (1,0)-(2,0): 0 (2,0 is 0)
  (1,1)-(2,1): 1
  (1,2)-(2,2): 0 (2,2 is 0)
  (2,1)-(3,1): 1
  (3,0)-(4,0): out
  (3,1)-(4,1): out
Total adjacent_pairs = 1+1+1+1+1+1 = 6? Let's list systematically:

Right adjacencies (j+1):
  (0,1) with (0,2): 0
  (1,0) with (1,1): 1
  (1,1) with (1,2): 1
  (1,2) with (1,3): 0
  (2,1) with (2,2): 0
  (3,0) with (3,1): 1
  (3,1) with (3,2): 0
Right total = 3

Down adjacencies (i+1):
  (0,1) with (1,1): 1
  (1,0) with (2,0): 0
  (1,1) with (2,1): 1
  (1,2) with (2,2): 0
  (2,1) with (3,1): 1
  (3,0) with (4,0): out
  (3,1) with (4,1): out
Down total = 3

Total adjacent_pairs = 6
Perimeter = 4*7 - 2*6 = 28 - 12 = 16 ✓

Method 4 (Count edges to water):
For each land cell, count sides with water/boundary:
(0,1): top=boundary(1), bottom=(1,1)land(0), left=(0,0)water(1), right=(0,2)water(1) → 3
(1,0): top=(0,0)water(1), bottom=(2,0)water(1), left=boundary(1), right=(1,1)land(0) → 3
(1,1): top=(0,1)land(0), bottom=(2,1)land(0), left=(1,0)land(0), right=(1,2)land(0) → 0
(1,2): top=(0,2)water(1), bottom=(2,2)water(1), left=(1,1)land(0), right=(1,3)water(1) → 3
(2,1): top=(1,1)land(0), bottom=(3,1)land(0), left=(2,0)water(1), right=(2,2)water(1) → 2
(3,0): top=(2,0)water(1), bottom=boundary(1), left=boundary(1), right=(3,1)land(0) → 3
(3,1): top=(2,1)land(0), bottom=boundary(1), left=(3,0)land(0), right=(3,2)water(1) → 2
Sum = 3+3+0+3+2+3+2 = 16 ✓
```

**Comparison Table:**

| Aspect | Number of Islands | Island Perimeter |
|--------|------------------|------------------|
**Objective** | Count components | Calculate boundary length |
**Approach** | DFS/BFS to mark visited | Count edges to water |
**Key Insight** | Connected components | Each land cell contributes 4 minus adjacencies |
**Time** | O(m×n) | O(m×n) |
**Space** | O(m×n) or O(1) with modification | O(1) |

**Graph Traversal Family:**

| Problem | Type | Key Difference |
|---------|------|---------------|
**200. Number of Islands** | Count components | Find all islands |
**463. Island Perimeter** | Perimeter | Single island, calculate boundary |
**695. Max Area of Island** | Largest component | Track size |
**130. Surrounded Regions** | Capture regions | Border-connected |
**1254. Number of Closed Islands** | Closed islands | Island completely surrounded by water |

**Edge Cases:**
- Single cell → 4
- Single row: [1,1,1] → 3×4 - 2×2 = 12-4=8? Actually: cells=3, adj=2, perimeter=12-4=8 ✓
- Single column similar
- No land → 0

**Why Method 5 (subtract 2) works:**
- Each land cell initially contributes 4 sides
- When two land cells are adjacent, they share 2 sides (one from each cell)
- So total perimeter reduces by 2 for each adjacency
- Only need to check right and down to avoid double counting