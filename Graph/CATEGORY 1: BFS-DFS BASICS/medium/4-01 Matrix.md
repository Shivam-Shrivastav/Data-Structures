## 542. 01 Matrix
**Category:** **GRAPH / BFS / MULTI-SOURCE BFS / DYNAMIC PROGRAMMING**

**Problem:** Given an `m x n` binary matrix `mat`, return the distance of the nearest `0` for each cell. The distance between two adjacent cells (horizontal/vertical) is `1`.

**Example:**
```
Input: mat = [[0,0,0],
              [0,1,0],
              [0,0,0]]
Output: [[0,0,0],
         [0,1,0],
         [0,0,0]]
```

```
Input: mat = [[0,0,0],
              [0,1,1],
              [0,1,1]]
Output: [[0,0,0],
         [0,1,1],
         [0,1,2]]
Explanation: 
- (1,1) is distance 1 from (1,0) or (0,1)
- (1,2) is distance 1 from (0,2) or (2,2)? Actually (0,2)=0 so distance 1
- (2,2) is distance 2 from (0,2)=0 via (1,2) or (2,1)
```

---

### **Relation to Rotting Oranges**
**Similar to:** **994. Rotting Oranges** but **distance to nearest 0** instead of rotting time
**How it's different:**
1. **Rotting Oranges:** Multi-source BFS from rotten (2), track time
2. **01 Matrix:** Multi-source BFS from all 0s, track distance

**Key Insight:** 
- Treat all `0` cells as sources at distance 0
- BFS outward to fill distances for `1` cells
- This gives shortest path to any `0` because BFS explores level by level

---

### 1. Multi-Source BFS (Optimal)
```python
from collections import deque

def updateMatrix(mat):
    if not mat or not mat[0]:
        return mat
    
    m, n = len(mat), len(mat[0])
    dist = [[-1] * n for _ in range(m)]
    queue = deque()
    
    # Initialize: all 0 cells are sources with distance 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                queue.append((i, j))
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    # BFS from all 0s simultaneously
    while queue:
        i, j = queue.popleft()
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and dist[ni][nj] == -1:
                dist[ni][nj] = dist[i][j] + 1
                queue.append((ni, nj))
    
    return dist
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 2. Dynamic Programming (Two Passes)
```python
def updateMatrix(mat):
    if not mat or not mat[0]:
        return mat
    
    m, n = len(mat), len(mat[0])
    INF = 10**9
    dist = [[INF] * n for _ in range(m)]
    
    # First pass: top-left to bottom-right
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
            else:
                if i > 0:
                    dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                if j > 0:
                    dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
    
    # Second pass: bottom-right to top-left
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if mat[i][j] == 1:
                if i < m-1:
                    dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                if j < n-1:
                    dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
    
    return dist
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 3. BFS with Level Tracking (Alternative)
```python
from collections import deque

def updateMatrix(mat):
    if not mat or not mat[0]:
        return mat
    
    m, n = len(mat), len(mat[0])
    dist = [[-1] * n for _ in range(m)]
    queue = deque()
    
    # Initialize all 0 cells as sources
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                dist[i][j] = 0
                queue.append((i, j))
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    
    while queue:
        i, j = queue.popleft()
        current_dist = dist[i][j]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and dist[ni][nj] == -1:
                dist[ni][nj] = current_dist + 1
                queue.append((ni, nj))
    
    return dist
```

---

### 4. DFS with Memoization (Less Efficient)
```python
def updateMatrix(mat):
    if not mat or not mat[0]:
        return mat
    
    m, n = len(mat), len(mat[0])
    memo = [[-1] * n for _ in range(m)]
    
    def dfs(i, j):
        if memo[i][j] != -1:
            return memo[i][j]
        
        if mat[i][j] == 0:
            memo[i][j] = 0
            return 0
        
        # Try all 4 directions
        min_dist = float('inf')
        for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n:
                min_dist = min(min_dist, 1 + dfs(ni, nj))
        
        memo[i][j] = min_dist
        return min_dist
    
    result = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            result[i][j] = dfs(i, j)
    
    return result
```
**TC:** O(m × n × 4) with memoization | **SC:** O(m × n)

---

### 5. BFS with All Cells Initially (Not Optimal)
```python
from collections import deque

def updateMatrix(mat):
    if not mat or not mat[0]:
        return mat
    
    m, n = len(mat), len(mat[0])
    result = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                # BFS from this cell to find nearest 0
                visited = [[False] * n for _ in range(m)]
                queue = deque([(i, j, 0)])
                visited[i][j] = True
                
                while queue:
                    x, y, d = queue.popleft()
                    if mat[x][y] == 0:
                        result[i][j] = d
                        break
                    
                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny, d + 1))
    
    return result
```
**TC:** O((m × n)²) worst case | **SC:** O(m × n)

---

**Key Insight (Multi-Source BFS):**
```
All 0s are sources at distance 0
BFS expands outward like waves
First time a 1 is reached = shortest distance to any 0
```

**Example Walkthrough (BFS):**
```
mat = [[0,0,0],
       [0,1,1],
       [0,1,1]]

Initialize queue with all 0s:
(0,0) dist=0
(0,1) dist=0
(0,2) dist=0
(1,0) dist=0
(2,0) dist=0

Process (0,0): 
  neighbors: (1,0) already visited, (0,1) visited
Process (0,1):
  neighbors: (1,1)=1 → set dist[1][1]=1, queue.append((1,1))
Process (0,2):
  neighbors: (1,2)=1 → set dist[1][2]=1, queue.append((1,2))
Process (1,0):
  neighbors: (2,0) visited, (1,1) already set to 1
Process (2,0):
  neighbors: (2,1)=1 → set dist[2][1]=1, queue.append((2,1))

Now queue has (1,1), (1,2), (2,1) all at distance 1

Process (1,1):
  neighbors: (2,1) already set, (1,2) already set, (0,1) visited
  (1,0) visited, (1,2) already set
Process (1,2):
  neighbors: (2,2)=1 → set dist[2][2]=2, queue.append((2,2))
Process (2,1):
  neighbors: (2,2) already set to 2, (1,1) visited

Result distances:
[0,0,0]
[0,1,1]
[0,1,2]
```

**Visual BFS Waves:**
```
Level 0 (0s):     Level 1:          Level 2:
0 0 0             0 0 0             0 0 0
0 0 0             0 1 1             0 1 1
0 0 0             0 1 1             0 1 2
```

**Comparison Table:**

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
**Multi-Source BFS** | O(m×n) | O(m×n) | Optimal, intuitive | Extra space for queue |
**Two-pass DP** | O(m×n) | O(m×n) | No queue, uses local info | Two passes needed |
**DFS with Memo** | O(m×n) | O(m×n) | Simple recursion | Stack overflow risk |
**Per-cell BFS** | O((m×n)²) | O(m×n) | Brute force | Very slow for large grids |

**BFS Family:**

| Problem | Key Difference |
|---------|---------------|
**542. 01 Matrix** | Distance to nearest 0 |
**994. Rotting Oranges** | Time to rot (multi-source BFS) |
**286. Walls and Gates** | Distance to nearest gate |
**1162. As Far from Land as Possible** | Max distance to nearest land |
**1926. Nearest Exit from Entrance** | BFS in maze to exit |

**Edge Cases:**
- Single cell `0` → `[[0]]`
- Single cell `1` → `[[1]]` (but with constraints, there should be at least one 0)
- All zeros → all distances 0
- All ones → distances increase from nearest 0
- Large grid with only one 0 → distances radiate outward

**Why Multi-Source BFS Works:**
- If we BFS from each 1 individually, it's O((m×n)²)
- Starting BFS from all 0s gives O(m×n)
- BFS ensures shortest path because it explores level by level
- First time a cell is visited = shortest distance

**DP Approach Explanation:**
```
First pass (top-left to bottom-right):
  dist[i][j] = min(up, left) + 1 if cell is 1

Second pass (bottom-right to top-left):
  dist[i][j] = min(dist[i][j], down+1, right+1)

This works because shortest path to a 0 can come from any direction
Two passes cover all 4 directions
```

**Common Pitfalls:**
- Not initializing distances for 0 cells
- Using BFS from each 1 (too slow)
- Forgetting that BFS distance is number of steps
- Not handling empty grid