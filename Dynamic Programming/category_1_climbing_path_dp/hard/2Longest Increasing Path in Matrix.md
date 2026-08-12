## Longest Increasing Path in Matrix
**Problem:** Given m×n matrix, find length of longest increasing path where you can move to adjacent cells (up, down, left, right) but only to cells with greater value.

**Example:**
```
Input: matrix = [[9,9,4],
                 [6,6,8],
                 [2,1,1]]
Output: 4
Explanation: Longest path is [1, 2, 6, 9]
```

```
Input: matrix = [[3,4,5],
                 [3,2,6],
                 [2,2,1]]
Output: 4
Path: [3, 4, 5, 6]
```

---

### DP Intuition
- **DFS + Memoization (Topological DP):** 
  - Each cell is a node, edges point to larger values → DAG
  - Longest path in DAG
- **State:** `dp[i][j]` = longest increasing path starting from (i,j)
- **Transition:** `dp[i][j] = 1 + max(dp[neighbors])` where neighbor > current
- **Base:** Cell with no larger neighbors = 1

---

### 1. DFS Solution (No Memo)
```python
def longestIncreasingPath(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    
    def dfs(i, j):
        max_len = 1
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            x, y = i+di, j+dj
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                max_len = max(max_len, 1 + dfs(x, y))
        return max_len
    
    result = 0
    for i in range(m):
        for j in range(n):
            result = max(result, dfs(i, j))
    return result
```
**TC:** O(4ᵐⁿ) | **SC:** O(mn) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def longestIncreasingPath(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    dp = [[-1]*n for _ in range(m)]
    
    def dfs(i, j):
        if dp[i][j] != -1:
            return dp[i][j]
        
        max_len = 1
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            x, y = i+di, j+dj
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                max_len = max(max_len, 1 + dfs(x, y))
        
        dp[i][j] = max_len
        return max_len
    
    result = 0
    for i in range(m):
        for j in range(n):
            result = max(result, dfs(i, j))
    return result
```
**TC:** O(mn) | **SC:** O(mn)

---

### 3. Alternative: DP with Sorting
```python
def longestIncreasingPath(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    
    # Sort cells by value
    cells = [(i, j, matrix[i][j]) for i in range(m) for j in range(n)]
    cells.sort(key=lambda x: x[2])
    
    dp = [[1]*n for _ in range(m)]
    max_len = 1
    
    for i, j, val in cells:
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            x, y = i+di, j+dj
            if 0 <= x < m and 0 <= y < n and matrix[x][y] < val:
                dp[i][j] = max(dp[i][j], dp[x][y] + 1)
        max_len = max(max_len, dp[i][j])
    
    return max_len
```
**TC:** O(mn log(mn)) | **SC:** O(mn)

---

**Key Formula:**
```
dp[i][j] = 1 + max(dp[x][y]) for all neighbors (x,y) > (i,j)
```

**Why Memoization works:**
- Each cell's result depends only on cells with larger values
- No cycles (strictly increasing)
- Once computed, result for cell never changes

**Example Walkthrough:**
```
Matrix:        DP:
9 9 4         1 1 2
6 6 8   →     2 2 1
2 1 1         3 4 2

Start from (2,0)=2: neighbors=6,1 → max(2,4)+1=3
From (2,1)=1: neighbors=6,6,2,1 → max(2,2,3,2)+1=4
```

**Optimization Notes:**
1. **Memoization is optimal:** O(mn) time
2. **No tabulation:** Hard to define processing order
3. **DAG property:** Can also use Kahn's algorithm with topological sort

**Edge Cases:**
- Single cell matrix → return 1
- All same values → return 1 (no increasing moves)
- Strictly increasing row/col → path length = mn