## 1277. Count Square Submatrices with All Ones
**Category:** **MATRIX/RECTANGLE DP**

**Problem:** Given a `m x n` binary matrix, return the **number of square submatrices** that contain all `1`s.

**Example:**
```
Input: matrix = 
[ [1,0,1],
  [1,1,0],
  [1,1,0] ]
Output: 7
Explanation: 
- 6 squares of size 1 (individual 1's)
- 1 square of size 2 (at positions (1,1) and (1,2)? Wait)
Actually let's count:
Size 1: all 1's at (0,0), (0,2), (1,0), (1,1), (2,0), (2,1) → 6
Size 2: only one 2x2 square at top-left? (0,0),(0,1),(1,0),(1,1) are all 1's → 1
Total = 7
```

```
Input: matrix = 
[ [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1] ]
Output: 15
Explanation:
Size 1: 10 ones
Size 2: 4 squares of size 2
Size 3: 1 square of size 3
Total = 10+4+1 = 15
```

```
Input: matrix = [[1]]
Output: 1
```

---

### **Relation to Maximal Square**
**Similar to:** **Maximal Square (221)** but **count all squares** instead of largest
**How it's different:**
1. **Maximal Square:** Find largest square, track max side
2. **Count Square Submatrices:** Count **all** squares of all sizes
3. **Key Insight:** Same DP formula, but sum all `dp[i][j]`

**Key Insight:** 
- Let `dp[i][j]` = side length of largest square ending at `(i,j)`
- This also tells us **how many squares end at (i,j)**
- Because if largest square ending at (i,j) has side k, then there are squares of sizes 1..k ending there
- So total squares = sum of all `dp[i][j]`

---

### DP Intuition
- **State:** `dp[i][j]` = side length of largest square with bottom-right corner at `(i,j)`
- **Transition:**
  ```
  if matrix[i][j] == 1:
      if i == 0 or j == 0:
          dp[i][j] = 1
      else:
          dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
  else:
      dp[i][j] = 0
  ```
- **Answer:** `sum(dp[i][j] for all i,j)`

**Why sum works:** 
- If `dp[i][j] = 3`, then squares of size 1, 2, and 3 end at (i,j)
- Each contributes to the count, so add 3 to total

---

### 1. Recursive Solution
```python
def countSquares(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    
    def dfs(i, j):
        if i < 0 or j < 0 or matrix[i][j] == 0:
            return 0
        
        up = dfs(i-1, j)
        left = dfs(i, j-1)
        up_left = dfs(i-1, j-1)
        
        return 1 + min(up, left, up_left)
    
    total = 0
    for i in range(m):
        for j in range(n):
            total += dfs(i, j)
    
    return total
```
**TC:** O(3ᵐⁿ) terrible | **SC:** O(m+n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def countSquares(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    memo = [[-1] * n for _ in range(m)]
    
    def dfs(i, j):
        if i < 0 or j < 0 or matrix[i][j] == 0:
            return 0
        if memo[i][j] != -1:
            return memo[i][j]
        
        up = dfs(i-1, j)
        left = dfs(i, j-1)
        up_left = dfs(i-1, j-1)
        
        memo[i][j] = 1 + min(up, left, up_left)
        return memo[i][j]
    
    total = 0
    for i in range(m):
        for j in range(n):
            total += dfs(i, j)
    
    return total
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 3. Tabulation (Bottom-Up DP)
```python
def countSquares(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    total = 0
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                total += dp[i][j]
    
    return total
```
**TC:** O(m × n) | **SC:** O(m × n)

---

### 4. Space Optimized (1D DP)
```python
def countSquares(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    dp = [0] * (n + 1)  # +1 for easier handling
    prev = 0  # dp[i-1][j-1]
    total = 0
    
    for i in range(m):
        for j in range(n):
            temp = dp[j+1]  # store for next iteration's prev
            if matrix[i][j] == 1:
                dp[j+1] = 1 + min(dp[j], dp[j+1], prev)
                total += dp[j+1]
            else:
                dp[j+1] = 0
            prev = temp
    
    return total
```
**TC:** O(m × n) | **SC:** O(n)

---

### 5. In-Place Modification (If allowed)
```python
def countSquares(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    total = 0
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                if i > 0 and j > 0:
                    matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                total += matrix[i][j]
    
    return total
```
**TC:** O(m × n) | **SC:** O(1) (modifies input)

---

**Key Formula:**
```
dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])  if matrix[i][j] == 1
Total = sum(dp[i][j] for all i,j)
```

**Example Walkthrough:**
```
matrix = 
[1,0,1]
[1,1,0]
[1,1,0]

DP table construction:

i=0: 
  j=0: matrix[0][0]=1, border → dp[0][0]=1, total=1
  j=1: matrix[0][1]=0 → dp[0][1]=0
  j=2: matrix[0][2]=1, border → dp[0][2]=1, total=2

i=1:
  j=0: matrix[1][0]=1, border → dp[1][0]=1, total=3
  j=1: matrix[1][1]=1 → min(dp[0][1]=0, dp[1][0]=1, dp[0][0]=1) = 0 → dp[1][1]=1, total=4
  j=2: matrix[1][2]=0 → dp[1][2]=0

i=2:
  j=0: matrix[2][0]=1, border → dp[2][0]=1, total=5
  j=1: matrix[2][1]=1 → min(dp[1][1]=1, dp[2][0]=1, dp[1][0]=1) = 1 → dp[2][1]=2, total=7
  j=2: matrix[2][2]=0 → dp[2][2]=0

Total = 7
```

**Visual DP Table:**
```
Original:    DP:
1 0 1        1 0 1
1 1 0        1 1 0
1 1 0        1 2 0

Sum = 1+0+1 + 1+1+0 + 1+2+0 = 7
```

**Another Example:**
```
matrix = 
[1,1,1]
[1,1,1]
[1,1,1]

DP:
[1,1,1]
[1,2,2]
[1,2,3]

Sum = 1+1+1 + 1+2+2 + 1+2+3 = 14
Which equals: size1=9, size2=4, size3=1 → 9+4+1=14 ✓
```

**Comparison Table:**

| Aspect | Maximal Square (221) | Count Square Submatrices (1277) |
|--------|---------------------|-------------------------------|
**Objective** | Largest square area | Count all squares |
**DP State** | Same dp[i][j] | Same dp[i][j] |
**Result** | max(dp[i][j])² | sum(dp[i][j]) |
**Interpretation** | Side length | Number of squares ending at (i,j) |
**Time** | O(m×n) | O(m×n) |
**Space** | O(n) | O(n) |

**Matrix/Rectangle DP Family:**

| Problem | Type | Key Difference |
|---------|------|---------------|
**221. Maximal Square** | Largest square | Find max area |
**1277. Count Square Submatrices** | Count all squares | Sum of dp values |
**1504. Count Submatrices With All Ones** | Count rectangles | More complex counting |
**85. Maximal Rectangle** | Largest rectangle | Histogram approach |

**Edge Cases:**
- Empty matrix → 0
- Single cell → 1 if 1 else 0
- All zeros → 0
- All ones → sum of 1..min(m,n) for each position

**Why Sum Works:**
- If `dp[i][j] = k`, it means there are squares of size 1..k ending at (i,j)
- Each such square is counted exactly once (by its bottom-right corner)
- Therefore, total squares = sum of all dp values

**Mathematical Formula for All Ones Matrix:**
For m×n all ones matrix:
- Number of squares = sum_{k=1 to min(m,n)} (m-k+1) × (n-k+1)
- DP approach automatically computes this