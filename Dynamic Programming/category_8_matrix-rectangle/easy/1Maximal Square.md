## 221. Maximal Square
**Category:** **MATRIX/RECTANGLE DP**

**Problem:** Given an `m x n` binary matrix filled with `0`s and `1`s, find the **largest square** containing only `1`s and return its **area**.

**Example:**
```
Input: matrix = 
[["1","0","1","0","0"],
 ["1","0","1","1","1"],
 ["1","1","1","1","1"],
 ["1","0","0","1","0"]]
Output: 4
Explanation: The largest square of 1's has side length 2, area 4.
```

```
Input: matrix = [["0","1"],["1","0"]]
Output: 1
```

```
Input: matrix = [["0"]]
Output: 0
```

---

### **Relation to Rectangle Problems**
**Similar to:** **Maximal Rectangle (85)** but **square** constraint
**How it's different:**
1. **Maximal Rectangle:** Can be any rectangle, need height arrays + stack
2. **Maximal Square:** All sides equal, simpler DP
3. **Key Insight:** Square's bottom-right corner determines size

**Key Insight:** 
- Let `dp[i][j]` = side length of largest square ending at `(i,j)` (bottom-right corner)
- If `matrix[i][j] == '1'`:
  ```
  dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
  ```
- This works because square at `(i,j)` extends from smaller squares at top, left, and top-left

---

### DP Intuition
- **State:** `dp[i][j]` = side length of largest square with bottom-right corner at `(i,j)`
- **Transition:**
  ```
  if matrix[i][j] == '1':
      dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
  else:
      dp[i][j] = 0
  ```
- **Base:** First row/col: `dp[i][j] = 1` if `matrix[i][j] == '1'` else `0`
- **Answer:** `max(dp[i][j])²` (max side length squared)

---

### 1. Recursive Solution
```python
def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    
    def dfs(i, j):
        if i < 0 or j < 0:
            return 0
        
        if matrix[i][j] == '0':
            return 0
        
        # Current cell is '1'
        up = dfs(i-1, j)
        left = dfs(i, j-1)
        up_left = dfs(i-1, j-1)
        
        return 1 + min(up, left, up_left)
    
    max_side = 0
    for i in range(m):
        for j in range(n):
            max_side = max(max_side, dfs(i, j))
    
    return max_side * max_side
```
**TC:** O(3ᵐⁿ) terrible | **SC:** O(m+n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    memo = [[-1] * n for _ in range(m)]
    
    def dfs(i, j):
        if i < 0 or j < 0 or matrix[i][j] == '0':
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        
        up = dfs(i-1, j)
        left = dfs(i, j-1)
        up_left = dfs(i-1, j-1)
        
        memo[i][j] = 1 + min(up, left, up_left)
        return memo[i][j]
    
    max_side = 0
    for i in range(m):
        for j in range(n):
            max_side = max(max_side, dfs(i, j))
    
    return max_side * max_side
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 3. Tabulation (Bottom-Up DP)
```python
def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                max_side = max(max_side, dp[i][j])
    
    return max_side * max_side
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 4. Space Optimized (1D DP)
```python
def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    dp = [0] * (n + 1)  # +1 for easier handling
    prev = 0  # dp[i-1][j-1]
    max_side = 0
    
    for i in range(m):
        for j in range(n):
            temp = dp[j+1]  # store for next iteration's prev
            if matrix[i][j] == '1':
                dp[j+1] = 1 + min(dp[j], dp[j+1], prev)
                max_side = max(max_side, dp[j+1])
            else:
                dp[j+1] = 0
            prev = temp
    
    return max_side * max_side
```
**TC:** O(m × n) | **SC:** O(n)

---

### 5. With Boundary Check (Explicit first row/col)
```python
def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0
    
    # First row
    for j in range(n):
        if matrix[0][j] == '1':
            dp[0][j] = 1
            max_side = 1
    
    # First column
    for i in range(m):
        if matrix[i][0] == '1':
            dp[i][0] = 1
            max_side = 1
    
    # Rest of matrix
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == '1':
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                max_side = max(max_side, dp[i][j])
    
    return max_side * max_side
```

---

**Key Formula:**
```
dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])  if matrix[i][j] == '1'
dp[i][j] = 0  otherwise
```

**Example Walkthrough:**
```
matrix = 
[1,0,1,0,0]
[1,0,1,1,1]
[1,1,1,1,1]
[1,0,0,1,0]

DP table construction:

i=0: [1,0,1,0,0]
i=1: 
  j=0: [1,1]? Actually:
  j=0: matrix[1][0]=1, not border → min(dp[0][0]=1, dp[1][-1]=0, dp[0][-1]=0) = 0? Wait careful:
  dp[1][0] is first column → if j==0, check i>0? Formula works but need j-1 exists.
  Better to do in code with border conditions.

Let's trace systematically:

Initialize dp[0][j] = matrix[0][j]
dp[0] = [1,0,1,0,0]

dp[i][0] = matrix[i][0]
dp[0][0]=1, dp[1][0]=1, dp[2][0]=1, dp[3][0]=1

Now i=1,j=1: matrix[1][1]=0 → dp[1][1]=0
i=1,j=2: matrix[1][2]=1 → min(dp[0][2]=1, dp[1][1]=0, dp[0][1]=0) = 0 → dp[1][2]=1
i=1,j=3: matrix[1][3]=1 → min(dp[0][3]=0, dp[1][2]=1, dp[0][2]=1) = 0 → dp[1][3]=1
i=1,j=4: matrix[1][4]=1 → min(dp[0][4]=0, dp[1][3]=1, dp[0][3]=0) = 0 → dp[1][4]=1

i=2,j=1: matrix[2][1]=1 → min(dp[1][1]=0, dp[2][0]=1, dp[1][0]=1) = 0 → dp[2][1]=1
i=2,j=2: matrix[2][2]=1 → min(dp[1][2]=1, dp[2][1]=1, dp[1][1]=0) = 0 → dp[2][2]=1
i=2,j=3: matrix[2][3]=1 → min(dp[1][3]=1, dp[2][2]=1, dp[1][2]=1) = 1 → dp[2][3]=2
i=2,j=4: matrix[2][4]=1 → min(dp[1][4]=1, dp[2][3]=2, dp[1][3]=1) = 1 → dp[2][4]=2

i=3,j=1: matrix[3][1]=0 → dp[3][1]=0
i=3,j=2: matrix[3][2]=0 → dp[3][2]=0
i=3,j=3: matrix[3][3]=1 → min(dp[2][3]=2, dp[3][2]=0, dp[2][2]=1) = 0 → dp[3][3]=1
i=3,j=4: matrix[3][4]=0 → dp[3][4]=0

Max dp value = 2 at (2,3) and (2,4)
Area = 2² = 4
```

**Visual DP Table:**
```
Original:    DP:
1 0 1 0 0    1 0 1 0 0
1 0 1 1 1    1 0 1 1 1
1 1 1 1 1    1 1 1 2 2
1 0 0 1 0    1 0 0 1 0
```

**Comparison Table:**

| Aspect | Maximal Rectangle (85) | Maximal Square (221) |
|--------|-----------------------|---------------------|
**Shape** | Any rectangle | Square only |
**DP Approach** | Heights array + stack | 2D DP with min of neighbors |
**State** | heights[j] at each row | dp[i][j] = side length |
**Transition** | Update heights, then compute area | 1 + min(up, left, up-left) |
**Time** | O(m × n) | O(m × n) |
**Space** | O(n) | O(n) optimized |

**Matrix/Rectangle DP Family:**

| Problem | Type | Key Difference |
|---------|------|---------------|
**221. Maximal Square** | Square | Equal sides, simple DP |
**85. Maximal Rectangle** | Any rectangle | Need histogram approach |
**84. Largest Rectangle in Histogram** | 1D | Stack-based |
**1277. Count Square Submatrices** | Count all | Sum of dp values |
**1504. Count Submatrices With All Ones** | Count rectangles | More complex counting |

**Edge Cases:**
- Empty matrix → 0
- Single row/column → max of single 1s
- No 1s → 0
- All 1s → min(m,n)²

**Why This Formula Works:**
- For a square ending at (i,j), we need:
  - Square ending at (i-1,j) of size at least k-1
  - Square ending at (i,j-1) of size at least k-1
  - Square ending at (i-1,j-1) of size at least k-1
- The limiting factor is the minimum of these three
- Adding current 1 extends the square by 1

**Space Optimization Insight:**
- Only need current row and previous row
- Need to track `dp[i-1][j-1]` which is overwritten
- Use a variable `prev` to store it before update