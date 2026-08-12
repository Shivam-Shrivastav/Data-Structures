## 994. Rotting Oranges
**Category:** **GRAPH / BFS / MULTI-SOURCE BFS**

**Problem:** Given an `m x n` grid where:
- `0` = empty cell
- `1` = fresh orange
- `2` = rotten orange

Every minute, rotten oranges rot adjacent (4-directionally) fresh oranges. Return the **minimum number of minutes** until no fresh oranges remain. If impossible, return `-1`.

**Example:**
```
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Explanation: 
Minute 1: Rotten spreads to (0,1), (1,0)
Minute 2: Rotten spreads to (0,2), (1,1), (2,1)
Minute 3: Rotten spreads to (1,2)
Minute 4: Rotten spreads to (2,2)
```

```
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: Orange at (2,2) never gets rotten
```

```
Input: grid = [[0,2]]
Output: 0
Explanation: No fresh oranges
```

---

### **Relation to Other BFS Problems**
**Similar to:** **542. 01 Matrix** (multi-source BFS) but with **spreading process**
**How it's different:**
1. **01 Matrix:** Find distance to nearest 0 from each cell
2. **Rotting Oranges:** Track time when each orange rots (level in BFS)

**Key Insight:** 
- This is a **multi-source BFS** problem
- All initial rotten oranges are sources at time 0
- BFS level = minutes taken to rot
- Track total fresh oranges; if remaining > 0 after BFS → return -1

---

### 1. BFS (Multi-Source) - Optimal
```python
from collections import deque

def orangesRotting(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0
    
    # Step 1: Find all rotten oranges and count fresh ones
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))  # (row, col, time)
            elif grid[i][j] == 1:
                fresh_count += 1
    
    # No fresh oranges to rot
    if fresh_count == 0:
        return 0
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    max_time = 0
    
    # Step 2: BFS to rot oranges
    while queue:
        i, j, time = queue.popleft()
        max_time = max(max_time, time)
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                grid[ni][nj] = 2  # Rot the orange
                fresh_count -= 1
                queue.append((ni, nj, time + 1))
    
    # Step 3: Check if all oranges are rotten
    return max_time if fresh_count == 0 else -1
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 2. BFS Without Time in Queue
```python
from collections import deque

def orangesRotting(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh_count += 1
    
    if fresh_count == 0:
        return 0
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    minutes = -1  # Start at -1 because first level is initial rotten
    
    while queue:
        minutes += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            i, j = queue.popleft()
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    fresh_count -= 1
                    queue.append((ni, nj))
    
    return minutes if fresh_count == 0 else -1
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 3. DFS (Not Recommended - BFS is better)
```python
def orangesRotting(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    INF = 10**9
    dist = [[INF] * n for _ in range(m)]
    
    def dfs(i, j, time):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or time >= dist[i][j]:
            return
        dist[i][j] = time
        
        if grid[i][j] == 1 or grid[i][j] == 2:
            dfs(i+1, j, time+1)
            dfs(i-1, j, time+1)
            dfs(i, j+1, time+1)
            dfs(i, j-1, time+1)
    
    # Initialize with rotten oranges
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                dfs(i, j, 0)
    
    # Check all fresh oranges
    max_time = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                if dist[i][j] == INF:
                    return -1
                max_time = max(max_time, dist[i][j])
    
    return max_time
```
**TC:** O(m × n × 4ᵈⁱˢᵗ) | **SC:** O(m × n)

---

### 4. BFS Using List as Queue (Less Efficient)
```python
def orangesRotting(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    queue = []
    fresh_count = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh_count += 1
    
    if fresh_count == 0:
        return 0
    
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    idx = 0
    max_time = 0
    
    while idx < len(queue):
        i, j, time = queue[idx]
        idx += 1
        max_time = max(max_time, time)
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                grid[ni][nj] = 2
                fresh_count -= 1
                queue.append((ni, nj, time + 1))
    
    return max_time if fresh_count == 0 else -1
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 5. With Fresh Orange Count Tracking
```python
from collections import deque

def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1
    
    # Track rotten count instead of fresh count
    rotten = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    time = 0
    
    while queue:
        i, j, t = queue.popleft()
        time = t
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                grid[ni][nj] = 2
                rotten += 1
                queue.append((ni, nj, t + 1))
    
    if fresh > 0 and rotten == 0:
        return -1
    
    return time if fresh == rotten else -1
```

---

**Key Insight (Multi-Source BFS):**
```
Initial rotten oranges = sources at level 0
BFS spreads to adjacent fresh oranges
Each level = 1 minute
All fresh oranges rotten = BFS visited all reachable fresh oranges
```

**Example Walkthrough:**
```
Initial grid:
2 1 1
1 1 0
0 1 1

Step 1: Queue = [(0,0,0)], fresh_count=6

Minute 0: Pop (0,0,0)
  Rot (0,1): grid[0][1]=2, fresh=5, queue.append((0,1,1))
  Rot (1,0): grid[1][0]=2, fresh=4, queue.append((1,0,1))
  Queue = [(0,1,1), (1,0,1)]

Minute 1: Pop (0,1,1)
  Rot (0,2): grid[0][2]=2, fresh=3, queue.append((0,2,2))
  Rot (1,1): grid[1][1]=2, fresh=2, queue.append((1,1,2))
  Queue = [(1,0,1), (0,2,2), (1,1,2)]

Minute 1: Pop (1,0,1)
  Rot (2,0): grid[2][0]=2? grid[2][0]=0 → skip
  Rot (1,1): already rotten
  Queue = [(0,2,2), (1,1,2)]

Minute 2: Pop (0,2,2)
  Rot (1,2): grid[1][2]=2, fresh=1, queue.append((1,2,3))
  Queue = [(1,1,2), (1,2,3)]

Minute 2: Pop (1,1,2)
  Rot (2,1): grid[2][1]=2, fresh=0, queue.append((2,1,3))
  Queue = [(1,2,3), (2,1,3)]

Minute 3: Pop (1,2,3)
  Rot (2,2): grid[2][2]=2, fresh=-1? Already 0
  Queue = [(2,1,3)]

Minute 3: Pop (2,1,3)
  Check neighbors, no fresh
  Queue empty

Result: max_time = 3? But example says 4. Let me recount:

Actually after minute 1: grid becomes
2 2 1
2 1 0
0 1 1
fresh=4

After minute 2:
2 2 2
2 2 0
0 2 1
fresh=1 (only (2,2))

After minute 3:
2 2 2
2 2 0
0 2 2
fresh=0

So minutes = 3? But example says 4. Let me re-read example...

The example shows:
Minute 1: (0,1),(1,0) rot
Minute 2: (0,2),(1,1),(2,1) rot
Minute 3: (1,2) rot
Minute 4: (2,2) rot

Wait, (2,1) rots at minute 2, then (2,2) rots at minute 4? That's because (2,2) is adjacent to (2,1) which rots at minute 2, so (2,2) would rot at minute 3, not 4. The example seems to have a discrepancy.

Let's trust the BFS logic: BFS finds the shortest path from any rotten orange. For (2,2):
- Path from (0,0) to (2,2): (0,0)→(1,0)→(2,0)? (2,0)=0 blocked
- Path from (0,0) to (2,2): (0,0)→(0,1)→(1,1)→(2,1)→(2,2): 4 steps
So (2,2) rots at time 4. Yes! That's correct because (2,1) rots at time 3, then (2,2) at time 4.

So BFS correctly gives max_time = 4.
```

**Comparison Table:**

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
**Multi-Source BFS** | O(m×n) | O(m×n) | Optimal, standard | None |
**Level-wise BFS** | O(m×n) | O(m×n) | Clear minute tracking | Slightly more code |
**DFS** | O(m×n×4ᵈ) | O(m×n) | Not recommended | Exponential in worst case |

**BFS Family:**

| Problem | Key Difference |
|---------|---------------|
**994. Rotting Oranges** | Multi-source BFS, track time |
**542. 01 Matrix** | Distance to nearest 0 |
**286. Walls and Gates** | Distance to nearest gate |
**1162. As Far from Land as Possible** | Multi-source BFS, max distance |
**1926. Nearest Exit from Entrance** | BFS in maze |

**Edge Cases:**
- No oranges → 0
- No fresh oranges → 0
- No rotten oranges but fresh exist → -1
- Disconnected fresh oranges → -1
- All rotten already → 0

**Why BFS over DFS:**
- BFS finds shortest time (level) naturally
- DFS would need to track minimum time
- BFS processes level by level, matching "minute" concept

**Common Pitfalls:**
- Forgetting to count fresh oranges initially
- Not handling case with no rotten oranges
- Using BFS without multi-source initialization
- Off-by-one in minute counting