## 417. Pacific Atlantic Water Flow
**Category:** **GRAPH / DFS / BFS / MULTI-SOURCE TRAVERSAL**

**Problem:** Given an `m x n` matrix `heights` representing the height of each cell, water can flow from a cell to adjacent cells (up, down, left, right) **if the adjacent cell's height is less than or equal to** the current cell's height. The Pacific Ocean touches the **top and left** edges, and the Atlantic Ocean touches the **bottom and right** edges. Return the list of coordinates where water can flow to **both** oceans.

**Example:**
```
Input: heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: These cells can reach both Pacific and Atlantic oceans.
```

```
Input: heights = [[1]]
Output: [[0,0]]
```

---

### **Relation to Surrounded Regions**
**Similar to:** **130. Surrounded Regions** but **two oceans** and **reverse flow**
**How it's different:**
1. **Surrounded Regions:** Start from boundary, mark safe 'O's
2. **Pacific Atlantic:** Start from **two boundaries**, find cells reachable to both
3. **Key Insight:** Reverse thinking - start from oceans and flow **uphill**

**Key Insight:** 
- Instead of checking if a cell can reach ocean (many paths), reverse:
- Start from ocean cells and do DFS/BFS **uphill** (to higher or equal heights)
- Cells reachable from Pacific and Atlantic are the answer
- This avoids O(m²n²) complexity

---

### 1. DFS from Both Oceans (Optimal)
```python
def pacificAtlantic(heights):
    if not heights or not heights[0]:
        return []
    
    m, n = len(heights), len(heights[0])
    pacific = [[False] * n for _ in range(m)]
    atlantic = [[False] * n for _ in range(m)]
    
    def dfs(i, j, visited):
        visited[i][j] = True
        
        # Explore 4 directions
        for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
            ni, nj = i + di, j + dj
            # Check boundaries and if cell is higher or equal (reverse flow uphill)
            if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                if heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, visited)
    
    # Start DFS from Pacific boundary (top and left edges)
    for i in range(m):
        dfs(i, 0, pacific)          # Left edge
    for j in range(n):
        dfs(0, j, pacific)          # Top edge
    
    # Start DFS from Atlantic boundary (bottom and right edges)
    for i in range(m):
        dfs(i, n-1, atlantic)       # Right edge
    for j in range(n):
        dfs(m-1, j, atlantic)       # Bottom edge
    
    # Find cells reachable by both oceans
    result = []
    for i in range(m):
        for j in range(n):
            if pacific[i][j] and atlantic[i][j]:
                result.append([i, j])
    
    return result
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 2. BFS from Both Oceans
```python
from collections import deque

def pacificAtlantic(heights):
    if not heights or not heights[0]:
        return []
    
    m, n = len(heights), len(heights[0])
    pacific = [[False] * n for _ in range(m)]
    atlantic = [[False] * n for _ in range(m)]
    
    def bfs(queue, visited):
        while queue:
            i, j = queue.popleft()
            visited[i][j] = True
            
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    if heights[ni][nj] >= heights[i][j]:
                        visited[ni][nj] = True
                        queue.append((ni, nj))
    
    # Initialize BFS from Pacific boundary
    pacific_queue = deque()
    for i in range(m):
        pacific_queue.append((i, 0))
    for j in range(n):
        pacific_queue.append((0, j))
    bfs(pacific_queue, pacific)
    
    # Initialize BFS from Atlantic boundary
    atlantic_queue = deque()
    for i in range(m):
        atlantic_queue.append((i, n-1))
    for j in range(n):
        atlantic_queue.append((m-1, j))
    bfs(atlantic_queue, atlantic)
    
    # Find cells reachable by both oceans
    result = []
    for i in range(m):
        for j in range(n):
            if pacific[i][j] and atlantic[i][j]:
                result.append([i, j])
    
    return result
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 3. DFS with Memoization (Forward Thinking)
```python
def pacificAtlantic(heights):
    if not heights or not heights[0]:
        return []
    
    m, n = len(heights), len(heights[0])
    # -1: unvisited, 0: not reachable, 1: reachable
    pacific = [[-1] * n for _ in range(m)]
    atlantic = [[-1] * n for _ in range(m)]
    
    def dfs(i, j, ocean, visited):
        if visited[i][j] != -1:
            return visited[i][j] == 1
        
        # Check if current cell is on ocean boundary
        if ocean == 'pacific' and (i == 0 or j == 0):
            visited[i][j] = 1
            return True
        if ocean == 'atlantic' and (i == m-1 or j == n-1):
            visited[i][j] = 1
            return True
        
        visited[i][j] = 0  # Mark as processing to avoid cycles
        current_height = heights[i][j]
        
        for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n:
                if heights[ni][nj] <= current_height:  # Water can flow down
                    if dfs(ni, nj, ocean, visited):
                        visited[i][j] = 1
                        return True
        
        return visited[i][j] == 1
    
    result = []
    for i in range(m):
        for j in range(n):
            can_reach_pacific = dfs(i, j, 'pacific', pacific)
            can_reach_atlantic = dfs(i, j, 'atlantic', atlantic)
            if can_reach_pacific and can_reach_atlantic:
                result.append([i, j])
    
    return result
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 4. Multi-Source BFS with Single Pass
```python
from collections import deque

def pacificAtlantic(heights):
    if not heights or not heights[0]:
        return []
    
    m, n = len(heights), len(heights[0])
    pacific = [[False] * n for _ in range(m)]
    atlantic = [[False] * n for _ in range(m)]
    
    pacific_queue = deque()
    atlantic_queue = deque()
    
    # Initialize boundaries
    for i in range(m):
        pacific_queue.append((i, 0))
        atlantic_queue.append((i, n-1))
    for j in range(n):
        pacific_queue.append((0, j))
        atlantic_queue.append((m-1, j))
    
    def bfs(queue, visited):
        while queue:
            i, j = queue.popleft()
            visited[i][j] = True
            
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    if heights[ni][nj] >= heights[i][j]:
                        queue.append((ni, nj))
    
    bfs(pacific_queue, pacific)
    bfs(atlantic_queue, atlantic)
    
    return [[i, j] for i in range(m) for j in range(n) if pacific[i][j] and atlantic[i][j]]
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 5. Using Stack (Iterative DFS)
```python
def pacificAtlantic(heights):
    if not heights or not heights[0]:
        return []
    
    m, n = len(heights), len(heights[0])
    pacific = [[False] * n for _ in range(m)]
    atlantic = [[False] * n for _ in range(m)]
    
    def dfs_stack(queue, visited):
        stack = list(queue)
        while stack:
            i, j = stack.pop()
            visited[i][j] = True
            
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    if heights[ni][nj] >= heights[i][j]:
                        stack.append((ni, nj))
    
    # Initialize stacks
    pacific_stack = []
    atlantic_stack = []
    
    for i in range(m):
        pacific_stack.append((i, 0))
        atlantic_stack.append((i, n-1))
    for j in range(n):
        pacific_stack.append((0, j))
        atlantic_stack.append((m-1, j))
    
    dfs_stack(pacific_stack, pacific)
    dfs_stack(atlantic_stack, atlantic)
    
    return [[i, j] for i in range(m) for j in range(n) if pacific[i][j] and atlantic[i][j]]
```
**TC:** O(m × n) | **SC:** O(m × n)

---

**Key Insight (Reverse Flow):**
```
Forward thinking: Can this cell reach ocean? → Too many paths
Reverse thinking: From ocean, which cells can reach me? → Start from boundaries, flow uphill
```

**Example Walkthrough (DFS):**
```
heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]

Pacific boundary cells: top row (0,0)-(0,4) and left col (0,0)-(4,0)
Atlantic boundary cells: bottom row (4,0)-(4,4) and right col (0,4)-(4,4)

Step 1: DFS from Pacific
  Start at (0,0) height=1 → can go to (0,1)=2 (≥1), (1,0)=3 (≥1)
  Continue propagating to higher/equal cells
  Mark all reachable in pacific[][] = True

Step 2: DFS from Atlantic
  Start from bottom/right edges, propagate uphill
  Mark all reachable in atlantic[][] = True

Step 3: Find intersection
  Cells where both pacific[i][j] and atlantic[i][j] are True
```

**Visual Result:**
```
Pacific reachable (P):     Atlantic reachable (A):     Both (P∩A):
P P P P P                  . . . A A                  . . . P A
P . P P P                  . . . A A                  . . . P A
P P P . .                  . . . . .                  . . . . .
P P . . .                  A A . . .                  A A . . .
P . . . .                  A . . . .                  A . . . .
```

**Comparison Table:**

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
**DFS Reverse** | O(m×n) | O(m×n) | Intuitive, standard | Recursion depth |
**BFS Reverse** | O(m×n) | O(m×n) | No recursion | Slightly more code |
**Forward Memo** | O(m×n) | O(m×n) | Direct thinking | More complex |
**Multi-source BFS** | O(m×n) | O(m×n) | Clean, efficient | Same as BFS |

**Graph Traversal Family:**

| Problem | Key Difference |
|---------|---------------|
**417. Pacific Atlantic Water Flow** | Two oceans, reverse flow |
**130. Surrounded Regions** | One boundary, mark safe |
**200. Number of Islands** | Count connected components |
**733. Flood Fill** | Change color from start |
**1254. Number of Closed Islands** | Islands not touching boundary |

**Edge Cases:**
- Single cell → both oceans touch → return [0,0]
- m = 1 or n = 1 → all cells touch at least one ocean
- All cells same height → all cells reach both oceans
- Strictly increasing/decreasing heights

**Why Reverse Flow Works:**
- Instead of O(m²n²) checking every path from every cell
- Start from oceans (m+n cells) and propagate
- Each cell visited once → O(m×n)

**Common Pitfalls:**
- Forgetting to mark visited cells (infinite loops)
- Using > instead of ≥ (water flows to lower or equal height)
- Not handling both oceans separately
- Off-by-one in boundary indices