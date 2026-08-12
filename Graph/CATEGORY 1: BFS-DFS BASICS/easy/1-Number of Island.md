## 200. Number of Islands
**Category:** **GRAPH / DFS / BFS / UNION FIND**

**Problem:** Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.

**Example:**
```
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
```

```
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

---

### **Relation to Graph Problems**
**Similar to:** **Connected Components in Grid**
**Key Insight:** 
- Treat each `'1'` as a node, edges to adjacent `'1'`s
- Number of islands = number of connected components
- Can solve with DFS, BFS, or Union Find

---

### DFS Intuition
- Iterate through each cell
- When we find a `'1'`, increment count and **sink the island** (mark all connected `'1'`s as visited)
- DFS to explore all 4 directions

---

### 1. DFS Recursive Solution
```python
def numIslands(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    
    def dfs(i, j):
        # Check boundaries and if cell is land
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
            return
        
        # Mark as visited (sink the island)
        grid[i][j] = '0'
        
        # Explore 4 directions
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    
    return count
```
**TC:** O(m × n) | **SC:** O(m × n) worst case for recursion stack

---

### 2. DFS with Visited Set (without modifying input)
```python
def numIslands(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0' or visited[i][j]:
            return
        
        visited[i][j] = True
        
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1' and not visited[i][j]:
                count += 1
                dfs(i, j)
    
    return count
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 3. BFS Solution (Queue)
```python
from collections import deque

def numIslands(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    count = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                
                # BFS to mark entire island
                queue = deque([(i, j)])
                grid[i][j] = '0'
                
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                            grid[nx][ny] = '0'
                            queue.append((nx, ny))
    
    return count
```
**TC:** O(m × n) | **SC:** O(min(m, n)) for queue

---

### 4. Union Find (Disjoint Set)
```python
def numIslands(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    parent = {}
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False
    
    # Initialize each '1' as its own set
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                parent[(i, j)] = (i, j)
    
    # Union adjacent '1's
    directions = [(1,0), (0,1)]  # only right and down to avoid duplicates
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if ni < m and nj < n and grid[ni][nj] == '1':
                        union((i, j), (ni, nj))
    
    # Count unique roots
    roots = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                roots.add(find((i, j)))
    
    return len(roots)
```
**TC:** O(m × n × α(mn)) | **SC:** O(m × n)

---

### 5. BFS with Level Order Tracking
```python
from collections import deque

def numIslands(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    count = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                
                # BFS with level tracking (optional)
                queue = deque([(i, j, 0)])  # (x, y, level)
                grid[i][j] = '0'
                
                while queue:
                    x, y, level = queue.popleft()
                    
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1':
                            grid[nx][ny] = '0'
                            queue.append((nx, ny, level + 1))
    
    return count
```

---

**Key Insight:**
- Each island is a connected component in the grid graph
- Once we find a '1', we explore all connected '1's and mark them visited
- Count each such exploration as one island

**Example Walkthrough (DFS):**
```
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

Start at (0,0): '1' → count=1, DFS marks all connected:
  (0,0),(0,1),(1,0),(1,1) all become '0'

Next (0,2): '0' skip
(0,3): '0' skip
(0,4): '0' skip

(1,2): '0' skip
...

(2,2): '1' → count=2, DFS marks (2,2) only

(3,3): '1' → count=3, DFS marks (3,3),(3,4)

Result = 3
```

**Comparison Table:**

| Aspect | DFS | BFS | Union Find |
|--------|-----|-----|------------|
**Approach** | Recursive/stack | Queue | Disjoint set |
**Space** | O(m×n) worst | O(min(m,n)) | O(m×n) |
**Modifies input** | Yes/No optional | Yes | No |
**Implementation** | Simple | Simple | More complex |
**Use case** | All around | Large grids | Dynamic connectivity |

**Graph Traversal Family:**

| Problem | Type | Key Difference |
|---------|------|---------------|
**200. Number of Islands** | Count components | Standard |
**695. Max Area of Island** | Largest component | Track size |
**463. Island Perimeter** | Perimeter | Count edges |
**130. Surrounded Regions** | Capture regions | Border-connected |
**417. Pacific Atlantic Water Flow** | Two oceans | Two DFS/BFS |

**Edge Cases:**
- Empty grid → 0
- Single cell → 1 if '1' else 0
- All water → 0
- All land → 1
- Checkerboard pattern → many islands

**Optimization Notes:**
- Modifying input saves space (no visited set)
- BFS better for very deep recursion to avoid stack overflow
- Union Find useful when grid changes dynamically