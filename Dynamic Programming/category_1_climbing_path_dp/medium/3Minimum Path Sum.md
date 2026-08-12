## Minimum Path Sum
**Problem:** Given m×n grid filled with non-negative numbers, find path from top-left to bottom-right that minimizes sum of numbers along path. Can only move **right** or **down**.

**Example:**
```
Input: grid = [[1,3,1],
               [1,5,1],
               [4,2,1]]
Output: 7
Explanation: 1 → 3 → 1 → 1 → 1
Path: (0,0) → (0,1) → (0,2) → (1,2) → (2,2)
Sum = 1 + 3 + 1 + 1 + 1 = 7
```

```
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
Path: 1 → 2 → 3 → 6
```

---

### DP Intuition
- **Optimal Substructure:** Min sum to reach (i,j) = grid[i][j] + min(above path, left path)
- **Base Cases:**
  - First row: cumulative sum (only right moves)
  - First column: cumulative sum (only down moves)
- **State:** `dp[i][j]` = minimum sum to reach (i,j)

---

### 1. Recursive Solution
```python
def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    
    def dfs(i, j):
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return float('inf')
        return grid[i][j] + min(dfs(i-1, j), dfs(i, j-1))
    
    return dfs(m-1, n-1)
```
**TC:** O(2ᵐ⁺ⁿ) | **SC:** O(m+n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    memo = {}
    
    def dfs(i, j):
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return float('inf')
        if (i, j) in memo:
            return memo[(i, j)]
        memo[(i, j)] = grid[i][j] + min(dfs(i-1, j), dfs(i, j-1))
        return memo[(i, j)]
    
    return dfs(m-1, n-1)
```
**TC:** O(m×n) | **SC:** O(m×n)

---

### 3. Tabulation (Bottom-Up DP)
```python
def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]
    
    # First row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # First column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # Fill rest
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    
    return dp[m-1][n-1]
```
**TC:** O(m×n) | **SC:** O(m×n)

---

### 4. Space Optimized (1D DP)
```python
def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    
    dp = [0] * n
    dp[0] = grid[0][0]
    
    # First row
    for j in range(1, n):
        dp[j] = dp[j-1] + grid[0][j]
    
    # Process remaining rows
    for i in range(1, m):
        dp[0] += grid[i][0]  # first column
        for j in range(1, n):
            dp[j] = grid[i][j] + min(dp[j], dp[j-1])
    
    return dp[n-1]
```
**TC:** O(m×n) | **SC:** O(n)

---

### 5. In-Place Modification (O(1) extra space)
```python
def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    
    # Modify grid in-place to store dp values
    # First row
    for j in range(1, n):
        grid[0][j] += grid[0][j-1]
    
    # First column
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    
    # Fill rest
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
    return grid[m-1][n-1]
```
**TC:** O(m×n) | **SC:** O(1) (if allowed to modify input)

---

**Key Formula:**
```
dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
dp[0][j] = grid[0][j] + dp[0][j-1]  # cumulative first row
dp[i][0] = grid[i][0] + dp[i-1][0]  # cumulative first column
```

**Visual Example:**
```
Grid:         DP:
1 3 1       1 4 5
1 5 1   →   2 7 6
4 2 1       6 8 7
Answer = 7
```

**Why DP works:**
- Each cell's minimum sum depends only on cell above and left
- We consider all paths implicitly through cumulative minimums
- Works because moves are only right/down (no cycles)

**Edge Cases:**
- 1×1 grid → return grid[0][0]
- Single row or column → cumulative sum
- All zeros → answer = 0