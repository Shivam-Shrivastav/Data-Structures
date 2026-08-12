## 130. Surrounded Regions
**Category:** **GRAPH / DFS / BFS / MATRIX TRAVERSAL / BOUNDARY TRAVERSAL**

**Problem:** Given an `m x n` matrix `board` containing `'X'` and `'O'`, capture all regions surrounded by `'X'`. A region is captured by flipping all `'O'`s into `'X'`s in that region.

**Example:**
```
Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","X","O","X"],
  ["X","O","X","X"]
]
Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","O","X","X"]
]
Explanation: The 'O' at (3,1) is on the boundary, so it's not surrounded.
All other 'O's are surrounded by 'X's and get flipped.
```

```
Input: board = [["X"]]
Output: [["X"]]
```

---

### **Relation to Number of Islands**
**Similar to:** **Number of Islands (200)** but **flip interior 'O's** instead of counting
**How it's different:**
1. **Number of Islands:** Count connected components of '1's
2. **Surrounded Regions:** Flip 'O's not connected to boundary to 'X'
3. **Key Insight:** 'O's connected to boundary cannot be captured

**Key Insight:** 
- Any 'O' on the boundary (or connected to boundary) is **safe** (not captured)
- All other 'O's are **surrounded** and should become 'X'
- Approach:
  1. Find all 'O's connected to boundary using DFS/BFS
  2. Mark them as safe (e.g., change to '#' or use visited set)
  3. Flip remaining 'O's to 'X'
  4. Restore safe 'O's back to 'O'

---

### 1. DFS on Boundary (Modify in-place)
```python
def solve(board):
    if not board or not board[0]:
        return
    
    m, n = len(board), len(board[0])
    
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return
        
        # Mark as safe (temporarily)
        board[i][j] = '#'
        
        # Explore 4 directions
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    # Step 1: Mark all 'O's connected to boundary
    for i in range(m):
        # First column
        if board[i][0] == 'O':
            dfs(i, 0)
        # Last column
        if board[i][n-1] == 'O':
            dfs(i, n-1)
    
    for j in range(n):
        # First row
        if board[0][j] == 'O':
            dfs(0, j)
        # Last row
        if board[m-1][j] == 'O':
            dfs(m-1, j)
    
    # Step 2: Flip remaining 'O' to 'X', restore '#' to 'O'
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] = 'O'
```
**TC:** O(m × n) | **SC:** O(m × n) recursion stack worst case

---

### 2. BFS on Boundary
```python
from collections import deque

def solve(board):
    if not board or not board[0]:
        return
    
    m, n = len(board), len(board[0])
    queue = deque()
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    # Step 1: Add all boundary 'O's to queue
    for i in range(m):
        if board[i][0] == 'O':
            queue.append((i, 0))
            board[i][0] = '#'  # Mark safe
        if board[i][n-1] == 'O':
            queue.append((i, n-1))
            board[i][n-1] = '#'
    
    for j in range(n):
        if board[0][j] == 'O':
            queue.append((0, j))
            board[0][j] = '#'
        if board[m-1][j] == 'O':
            queue.append((m-1, j))
            board[m-1][j] = '#'
    
    # Step 2: BFS to mark all 'O's connected to boundary
    while queue:
        i, j = queue.popleft()
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                board[ni][nj] = '#'
                queue.append((ni, nj))
    
    # Step 3: Flip remaining 'O' to 'X', restore '#' to 'O'
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] = 'O'
```
**TC:** O(m × n) | **SC:** O(m × n) for queue

---

### 3. DFS with Visited Set (No input modification until end)
```python
def solve(board):
    if not board or not board[0]:
        return
    
    m, n = len(board), len(board[0])
    visited = [[False] * n for _ in range(m)]
    safe_cells = []
    
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] != 'O':
            return
        
        visited[i][j] = True
        safe_cells.append((i, j))
        
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)
    
    # Mark all 'O's connected to boundary
    for i in range(m):
        if board[i][0] == 'O' and not visited[i][0]:
            dfs(i, 0)
        if board[i][n-1] == 'O' and not visited[i][n-1]:
            dfs(i, n-1)
    
    for j in range(n):
        if board[0][j] == 'O' and not visited[0][j]:
            dfs(0, j)
        if board[m-1][j] == 'O' and not visited[m-1][j]:
            dfs(m-1, j)
    
    # Flip all unvisited 'O's to 'X'
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O' and not visited[i][j]:
                board[i][j] = 'X'
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 4. Iterative DFS (Using Stack)
```python
def solve(board):
    if not board or not board[0]:
        return
    
    m, n = len(board), len(board[0])
    stack = []
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    # Step 1: Add all boundary 'O's to stack
    for i in range(m):
        if board[i][0] == 'O':
            stack.append((i, 0))
            board[i][0] = '#'
        if board[i][n-1] == 'O':
            stack.append((i, n-1))
            board[i][n-1] = '#'
    
    for j in range(n):
        if board[0][j] == 'O':
            stack.append((0, j))
            board[0][j] = '#'
        if board[m-1][j] == 'O':
            stack.append((m-1, j))
            board[m-1][j] = '#'
    
    # Step 2: DFS to mark all 'O's connected to boundary
    while stack:
        i, j = stack.pop()
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                board[ni][nj] = '#'
                stack.append((ni, nj))
    
    # Step 3: Flip remaining 'O' to 'X', restore '#' to 'O'
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] = 'O'
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 5. Union Find (Disjoint Set)
```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

def solve(board):
    if not board or not board[0]:
        return
    
    m, n = len(board), len(board[0])
    dsu = DSU(m * n + 1)  # Extra node for boundary
    boundary_node = m * n
    
    def index(i, j):
        return i * n + j
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    # Union boundary 'O's with boundary_node
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    dsu.union(index(i, j), boundary_node)
                else:
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O':
                            dsu.union(index(i, j), index(ni, nj))
    
    # Flip all 'O's not connected to boundary
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O' and dsu.find(index(i, j)) != dsu.find(boundary_node):
                board[i][j] = 'X'
```
**TC:** O(m × n × α(mn)) | **SC:** O(m × n)

---

**Key Insight:**
- 'O's on boundary and connected to boundary are **safe**
- Start DFS/BFS from all boundary 'O's
- Mark all reachable 'O's as safe (temporary marker '#')
- Flip remaining 'O's to 'X'
- Restore safe 'O's

**Example Walkthrough (DFS):**
```
Original board:
X X X X
X O O X
X X O X
X O X X

Step 1: Mark boundary 'O's:
- (3,1) is boundary 'O' → dfs(3,1)
  Mark (3,1) as '#'
  Check neighbors: (2,1) is 'X', (3,0) is 'X', (3,2) is 'X', (4,1) out
  No other 'O's reachable

Board after marking:
X X X X
X O O X
X X O X
X # X X

Step 2: Flip remaining 'O' to 'X':
(1,1) → 'X'
(1,2) → 'X'
(2,2) → 'X'

Step 3: Restore '#' to 'O':
(3,1) → 'O'

Final:
X X X X
X X X X
X X X X
X O X X
```

**Comparison Table:**

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
**DFS Boundary** | O(m×n) | O(m×n) | Simple, intuitive | Recursion limit |
**BFS Boundary** | O(m×n) | O(m×n) | No recursion, level order | Slightly more code |
**Union Find** | O(m×n×α) | O(m×n) | Good for dynamic connectivity | More complex |

**Graph Traversal Family:**

| Problem | Key Difference |
|---------|---------------|
**130. Surrounded Regions** | Flip interior 'O's |
**200. Number of Islands** | Count connected components |
**695. Max Area of Island** | Largest island area |
**733. Flood Fill** | Change color of connected region |
**1254. Number of Closed Islands** | Islands not touching boundary |

**Edge Cases:**
- Empty board → no change
- Single cell → unchanged (boundary)
- All 'X's → no change
- All 'O's → all safe (on boundary), no flip
- Board with no interior → no flip

**Why Mark Safe 'O's First:**
- If we flip interior 'O's directly, we lose information
- Marking safe 'O's prevents them from being flipped
- Temporary marker '# ' allows distinction

**Common Pitfalls:**
- Forgetting to mark visited cells (infinite recursion)
- Only checking top/bottom rows and left/right columns separately (correct)
- Flipping boundary 'O's (they should remain 'O')
- Using 8-directional connectivity (problem requires 4-directional)