## Unique Paths
**Problem:** Find number of unique paths from top-left (0,0) to bottom-right (m-1,n-1) of an m×n grid. You can only move **right** or **down**.

**Example:**
```
Input: m = 3, n = 7
Output: 28
```
Grid (3×7):
```
Start →  →  →  →  →  → End
 ↓   →  →  →  →  →  → End
 ↓   →  →  →  →  →  → End
```
Total paths = 28

```
Input: m = 3, n = 2
Output: 3
Paths: 
1. Right → Down → Down
2. Down → Right → Down  
3. Down → Down → Right
```

---

### DP Intuition
- **Optimal Substructure:** Paths to (i,j) = Paths from above (i-1,j) + Paths from left (i,j-1)
- **Base Cases:** First row and first column have only 1 path (all rights or all downs)
- **State:** `dp[i][j]` = unique paths to reach (i,j)

---

### 1. Recursive Solution
```python
def uniquePaths(m, n):
    def dfs(i, j):
        if i == 0 or j == 0:  # reached first row or column
            return 1
        return dfs(i-1, j) + dfs(i, j-1)
    return dfs(m-1, n-1)
```
**TC:** O(2ᵐ⁺ⁿ) | **SC:** O(m+n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def uniquePaths(m, n):
    memo = {}
    def dfs(i, j):
        if i == 0 or j == 0:
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
def uniquePaths(m, n):
    dp = [[0]*n for _ in range(m)]
    
    # First column: only 1 path (all down)
    for i in range(m):
        dp[i][0] = 1
    
    # First row: only 1 path (all right)
    for j in range(n):
        dp[0][j] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]
```
**TC:** O(m×n) | **SC:** O(m×n)

---

### 4. Space Optimized (1D DP)
```python
def uniquePaths(m, n):
    # Single row DP
    dp = [1] * n  # first row all 1s
    
    for i in range(1, m):
        for j in range(1, n):
            dp[j] = dp[j] + dp[j-1]  # dp[j] = above, dp[j-1] = left
    
    return dp[n-1]
```
**TC:** O(m×n) | **SC:** O(n)

---

### 5. Mathematical Solution (Combinations)
Number of paths = C(m+n-2, m-1) = C(m+n-2, n-1)

You need exactly:
- (m-1) down moves
- (n-1) right moves
Total moves = (m+n-2)
Choose positions for down/right moves

```python
def uniquePaths(m, n):
    from math import comb
    return comb(m+n-2, m-1)
```
**TC:** O(min(m,n)) | **SC:** O(1)

---

**Key Formula:**
```
dp[i][j] = dp[i-1][j] + dp[i][j-1]
dp[i][0] = 1 for all i
dp[0][j] = 1 for all j
```

**Visual Example (3×3):**
```
dp = [[1, 1, 1],
      [1, 2, 3],
      [1, 3, 6]]
Answer = 6
```

**Edge Cases:**
- m=1 or n=1 → return 1
- Large m,n (up to 100) → use DP or combinations