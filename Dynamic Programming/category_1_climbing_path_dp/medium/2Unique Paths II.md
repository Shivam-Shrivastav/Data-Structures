## Unique Paths II
**Problem:** Same as Unique Paths but with **obstacles** in the grid. `obstacleGrid[i][j] = 1` means obstacle, `0` means empty. Find number of unique paths from (0,0) to (m-1,n-1), avoiding obstacles.

**Example:**
```
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation:
Path 1: Right → Right → Down → Down
Path 2: Down → Down → Right → Right
The obstacle (1) blocks the center.
```

```
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
Only path: Down → Right
```

---

### DP Intuition
- **Optimal Substructure:** Same as before, but if cell has obstacle: paths = 0
- **Base Cases:**
  - First row: paths = 1 until first obstacle, then 0
  - First column: paths = 1 until first obstacle, then 0
- **State:** `dp[i][j]` = unique paths to (i,j), 0 if obstacle

---

### 1. Recursive Solution
```python
def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    
    def dfs(i, j):
        if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
            return 0
        if i == 0 and j == 0:
            return 1
        return dfs(i-1, j) + dfs(i, j-1)
    
    return dfs(m-1, n-1)
```
**TC:** O(2ᵐ⁺ⁿ) | **SC:** O(m+n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    memo = {}
    
    def dfs(i, j):
        if i < 0 or j < 0 or obstacleGrid[i][j] == 1:
            return 0
        if i == 0 and j == 0:
            return 1
        if (i, j) in memo:
            return memo[(i, j)]
        memo[(i, j)] = dfs(i-1, j) + dfs(i, j-1)
        return memo[(i, j)]
    
    return dfs(m-1, n-1)
```
**TC:** O(m×n) | **SC:** O(m×n)

---

### 3. Tabulation (Bottom-Up DP)
```python
def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    
    # Start cell blocked
    if obstacleGrid[0][0] == 1:
        return 0
    
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = 1
    
    # First row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
    
    # First column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
    
    # Fill DP table
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            else:
                dp[i][j] = 0
    
    return dp[m-1][n-1]
```
**TC:** O(m×n) | **SC:** O(m×n)

---

### 4. Space Optimized (1D DP)
```python
def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    
    if obstacleGrid[0][0] == 1:
        return 0
    
    dp = [0] * n
    dp[0] = 1
    
    # First row initialization
    for j in range(1, n):
        dp[j] = dp[j-1] if obstacleGrid[0][j] == 0 else 0
    
    # Process rows
    for i in range(1, m):
        # First column of current row
        if obstacleGrid[i][0] == 1:
            dp[0] = 0
        
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[j] = dp[j] + dp[j-1]
            else:
                dp[j] = 0
    
    return dp[n-1]
```
**TC:** O(m×n) | **SC:** O(n)

---

**Key Differences from Unique Paths I:**
1. **Start/End cells can be obstacles** → return 0 immediately
2. **First row/column not always 1** → reset to 0 after first obstacle
3. **dp[i][j] = 0** if obstacleGrid[i][j] = 1

**Base Cases:**
```
if obstacleGrid[0][0] == 1: return 0
dp[0][0] = 1

First row: dp[0][j] = dp[0][j-1] if grid[0][j]==0 else 0
First col: dp[i][0] = dp[i-1][0] if grid[i][0]==0 else 0
```

**Example Walkthrough (3×3 with center obstacle):**
```
Grid:      DP:
0 0 0     1 1 1
0 1 0  →  1 0 1  
0 0 0     1 1 2
Answer = 2
```

**Edge Cases:**
- Start cell blocked → return 0
- End cell blocked → return 0
- Single cell grid (1×1) → return 1 if empty, 0 if obstacle